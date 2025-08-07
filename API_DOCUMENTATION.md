# Airtable Sync API Documentation

## Overview
This API synchronizes HR and Client data from Airtable to Supabase. It supports both full and incremental sync modes, with automated and manual endpoints for both HR and Client data.

## Base URL
```
http://localhost:8000
```

## Authentication
Manual sync endpoints require authentication via the `x-sync-key` header. The key must match the `SYNC_KEY` environment variable.

## Running the API

### Start the server
```bash
python3 main.py
```

The server will start on port 8000 by default.

### Environment Variables Required
- `SUPABASE_URL` - Your Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY` - Supabase service role key
- `AIRTABLE_API_KEY` - Airtable API key
- `AIRTABLE_BASE_ID` - Airtable base ID for HR data
- `SYNC_KEY` - Authentication key for manual sync endpoints

---

## Endpoints

### 1. Health Check

**GET** `/`

Check if the API is running.

#### Response
```json
{
  "message": "Airtable Sync API is running"
}
```

---

## HR Data Endpoints

### 2. Automated HR Sync

**GET** `/hr/cron`

Endpoint for automated hourly HR sync runs (no authentication required).

#### Query Parameters
- `sync_mode` (optional): `"full"` or `"incremental"` (default: `"incremental"`)

#### Example Request
```bash
curl "http://localhost:8000/hr/cron?sync_mode=incremental"
```

#### Success Response (200)
```json
{
  "status": "success",
  "message": "HR sync completed successfully (mode: incremental)",
  "rows": {
    "departments": 15,
    "positions": 54,
    "team_members": 240,
    "sync_mode": "incremental",
    "requested_mode": "incremental"
  }
}
```

#### Error Response (500)
```json
{
  "detail": "HR sync failed: [error message]"
}
```

---

### 3. Manual HR Sync

**POST** `/hr/sync`

Manual HR sync endpoint with authentication.

#### Headers
- `x-sync-key` (required): Must match the `SYNC_KEY` environment variable

#### Query Parameters
- `sync_mode` (optional): `"full"` or `"incremental"` (default: `"incremental"`)

#### Example Request
```bash
curl -X POST "http://localhost:8000/hr/sync?sync_mode=full" \
  -H "x-sync-key: your-sync-key-here"
```

#### Success Response (200)
```json
{
  "status": "success",
  "message": "Manual HR sync completed successfully (mode: full)",
  "rows": {
    "departments": 15,
    "positions": 54,
    "team_members": 240,
    "sync_mode": "full",
    "requested_mode": "full"
  }
}
```

#### Error Responses
- **401 Unauthorized**: Invalid or missing `x-sync-key` header
- **500 Internal Server Error**: Sync failed or `SYNC_KEY` not configured

---

## Client Data Endpoints

### 4. Automated Client Sync

**GET** `/client/cron`

Endpoint for automated hourly client sync runs (no authentication required).

#### Query Parameters
- `sync_mode` (optional): `"full"` or `"incremental"` (default: `"incremental"`)

#### Example Request
```bash
curl "http://localhost:8000/client/cron?sync_mode=incremental"
```

#### Success Response (200)
```json
{
  "status": "success",
  "message": "Client sync completed successfully (mode: incremental)",
  "tables": {
    "companies": 50,
    "services": 12,
    "marketplaces": 8,
    "saas_tools": 15,
    "accounts": 75,
    "account_services_details": 120,
    "contracts": 45,
    "console_login_emails": 90,
    "client_meetings": 945
  }
}
```

#### Error Response (500)
```json
{
  "detail": "Client sync failed: [error message]"
}
```

---

### 5. Manual Client Sync

**POST** `/client/sync`

Manual client sync endpoint with authentication.

#### Headers
- `x-sync-key` (required): Must match the `SYNC_KEY` environment variable

#### Query Parameters
- `sync_mode` (optional): `"full"` or `"incremental"` (default: `"incremental"`)

#### Example Request
```bash
curl -X POST "http://localhost:8000/client/sync?sync_mode=full" \
  -H "x-sync-key: your-sync-key-here"
```

#### Success Response (200)
```json
{
  "status": "success",
  "message": "Manual client sync completed successfully (mode: full)",
  "tables": {
    "companies": 50,
    "services": 12,
    "marketplaces": 8,
    "saas_tools": 15,
    "accounts": 75,
    "account_services_details": 120,
    "contracts": 45,
    "console_login_emails": 90,
    "client_meetings": 945
  }
}
```

#### Error Responses
- **401 Unauthorized**: Invalid or missing `x-sync-key` header
- **500 Internal Server Error**: Sync failed or `SYNC_KEY` not configured

---

## Sync Modes

### Incremental Sync (Default)
- Only syncs records modified since the last sync
- Uses "Last Modified" field in supported tables
- Faster and more efficient for regular updates
- Automatically falls back to full sync if incremental fails

### Full Sync
- Syncs all records from all tables
- Ensures complete data consistency
- Use when:
  - First time setup
  - After schema changes
  - To resolve data inconsistencies

---

## Data Flow

### HR Data Tables
1. **departments** - Department records
2. **positions** - Position records linked to departments
3. **team_members** - Team member records with relationships to departments, positions, and managers

### Client Data Tables
1. **companies** - Company records
2. **services** - Service types
3. **marketplaces** - Marketplace platforms
4. **saas_tools** - SaaS tool records
5. **accounts** - Account records linked to companies
6. **account_services_details** - Service details linked to accounts and services
   - Maps team members to HR UUIDs via `account_manager_id`
7. **contracts** - Contract records with many-to-many relationships
8. **console_login_emails** - Login credentials linked to account services
9. **client_meetings** - Meeting records linked to accounts
   - Maps submitters to HR UUIDs via `submitter_id`

---

## Testing the API

### Quick Test Commands

1. **Check if API is running:**
```bash
curl http://localhost:8000/
```

2. **Run incremental HR sync (no auth):**
```bash
curl "http://localhost:8000/hr/cron"
```

3. **Run full client sync (with auth):**
```bash
curl -X POST "http://localhost:8000/client/sync?sync_mode=full" \
  -H "x-sync-key: your-sync-key-here"
```

4. **Check sync results in Supabase:**
```sql
-- Check HR team members
SELECT COUNT(*) FROM hr.team_members;

-- Check client meetings with submitter links
SELECT 
    cm.submitter,
    cm.submitter_id,
    tm.full_name as submitter_name
FROM client.client_meetings cm
LEFT JOIN hr.team_members tm ON cm.submitter_id = tm.id
WHERE cm.submitter_id IS NOT NULL
LIMIT 5;
```

---

## Error Handling

The API implements intelligent error handling:
- Incremental syncs automatically fall back to full sync on failure
- Detailed error messages are returned in responses
- All syncs are logged with timestamps
- Last sync timestamps are stored in `system_kv` table

---

## Performance Notes

- Incremental syncs are much faster (typically < 10 seconds)
- Full syncs may take 1-2 minutes depending on data volume
- Client sync with 900+ meetings may take longer
- Use incremental mode for regular updates
- Schedule full syncs during off-peak hours

---

## Deployment Considerations

1. **Production Setup:**
   - Use a process manager like PM2 or systemd
   - Set up proper logging
   - Configure environment variables securely
   - Use HTTPS in production

2. **Cron Job Setup:**
   ```bash
   # Add to crontab for hourly syncs
   0 * * * * curl "http://localhost:8000/hr/cron"
   0 * * * * curl "http://localhost:8000/client/cron"
   ```

3. **Monitoring:**
   - Monitor API health endpoint
   - Track sync execution times
   - Alert on sync failures
   - Monitor Supabase database growth