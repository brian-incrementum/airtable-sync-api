# Airtable HR Sync API

A FastAPI service that syncs HR data from Airtable to Supabase on an hourly schedule and via manual HTTP triggers.

## Features

- **Automated Sync**: Syncs three Airtable tables (Departments, Positions, Team Directory) to Supabase
- **Manual Trigger**: HTTP endpoint for on-demand synchronization
- **Relationship Integrity**: Maintains foreign key relationships between tables
- **Incremental Updates**: Tracks last sync timestamp for efficient updates

## Tables Synced

1. **Departments** (`hr.departments`)
   - Fields: Name
   - Source: Airtable Department table

2. **Positions** (`hr.positions`) 
   - Fields: Name, Department reference
   - Source: Airtable Position table

3. **Team Members** (`hr.team_members`)
   - Fields: Full Name, Department, Position, Status, Contact info, etc.
   - Source: Airtable Team Directory table

## Setup

### 1. Environment Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your actual values:
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY`: Service role key from Supabase dashboard
- `AIRTABLE_API_KEY`: Personal access token from Airtable
- `AIRTABLE_BASE_ID`: Base ID from your Airtable base URL
- `SYNC_KEY`: Secret key for manual sync authentication

### 3. Database Setup

The required tables should already be created in your Supabase `hr` schema:
- `hr.departments`
- `hr.positions` 
- `hr.team_members`
- `hr.system_kv`

### 4. Test Setup

Run the setup test to verify everything is configured correctly:

```bash
python test_setup.py
```

## Usage

### Start the Server

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

### API Endpoints

#### Health Check
```bash
GET /
```

#### Automated Sync (for schedulers)
```bash
GET /cron
```

#### Manual Sync (authenticated)
```bash
POST /sync
Headers: x-sync-key: your_sync_key_here
```

### Example Manual Sync

```bash
curl -X POST http://127.0.0.1:8000/sync \
  -H "x-sync-key: airtable-sync-secure-key-2024"
```

Expected response:
```json
{
  "status": "success",
  "message": "Manual sync completed successfully", 
  "rows": {
    "departments": 25,
    "positions": 150,
    "team_members": 500
  }
}
```

## Sync Process

1. **Departments**: Synced first (no dependencies)
2. **Positions**: Synced second (references departments)
3. **Team Members**: Synced last (references positions and departments)
4. **Timestamp Update**: Records sync completion time

## Data Mapping

### Departments
- `airtable_id` → Unique Airtable record ID
- `name` → Name field from Airtable

### Positions  
- `airtable_id` → Unique Airtable record ID
- `name` → Name field from Airtable
- `department_id` → Foreign key to `hr.departments.id`

### Team Members
- `airtable_id` → Unique Airtable record ID
- `full_name` → Full Name field
- `status` → Status field (Employee, Contractor, etc.)
- Plus 15+ additional fields (email, phone, dates, etc.)

## Error Handling

- Failed syncs return HTTP 500 with error details
- Authentication failures return HTTP 401
- All operations are logged to console
- Partial failures don't affect subsequent table syncs

## Development

### Project Structure
```
├── main.py              # FastAPI application
├── sync.py              # Core sync logic
├── test_setup.py        # Setup verification
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── README.md           # This file
```

### Adding New Fields

1. Update the mapping function in `sync.py`
2. Add the field to the Supabase table schema
3. Test with a manual sync

## Deployment

The service is designed to run locally during development. For production deployment:

1. Set environment variables in your hosting platform
2. Use a production WSGI server like Gunicorn
3. Set up automated scheduling (cron job or platform scheduler)
4. Monitor sync logs and set up alerting

## Troubleshooting

1. **"Missing environment variables"**: Check your `.env` file
2. **"Supabase connection failed"**: Verify URL and service role key
3. **"Airtable connection failed"**: Check API key and base ID
4. **401 Unauthorized**: Verify `x-sync-key` header matches `SYNC_KEY`
5. **Foreign key errors**: Ensure departments sync before positions