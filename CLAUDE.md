# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Airtable to Supabase sync API that synchronizes HR data from three Airtable tables (departments, positions, team_members) to a Supabase database. The sync supports both full and incremental modes, with intelligent change detection based on last modified timestamps.

## Development Setup

### Prerequisites
- Python 3.8+
- Environment variables in `.env` file:
  - `SUPABASE_URL`
  - `SUPABASE_SERVICE_ROLE_KEY`
  - `AIRTABLE_API_KEY`
  - `AIRTABLE_BASE_ID`
  - `SYNC_KEY` (for manual sync authentication)

### Running the Application

**Start the API server:**
```bash
python3 main.py
```

**Run manual sync:**
```bash
# Incremental sync (only modified records)
python3 run_sync.py

# Full sync (all records)
python3 run_sync.py --full
```

**API Endpoints:**
- `GET /` - Health check
- `GET /cron?sync_mode=full|incremental` - Automated sync endpoint
- `POST /sync?sync_mode=full|incremental` - Manual sync (requires x-sync-key header)

## Architecture

### Sync Process
1. **Incremental Sync** (default): Only syncs team_members modified since last sync timestamp
2. **Full Sync**: Syncs all records from all tables
3. **Smart Fallback**: Automatically falls back to full sync if incremental fails

### Data Flow
1. Fetch from Airtable tables (with pagination support)
2. Map Airtable records to Supabase format
3. Upsert to Supabase (using airtable_id for conflict resolution)
4. Update last sync timestamp in system_kv table

### Key Features
- **Intelligent Sync**: Uses "Last Modified" field in team_members table to only sync changed records
- **Relationship Integrity**: Maintains foreign key relationships between tables
- **Error Handling**: Falls back to full sync on incremental sync failures
- **Timestamp Tracking**: Stores last sync time for incremental syncs

### Table Structure
- **departments**: Simple department records
- **positions**: Linked to departments via foreign key
- **team_members**: Complex records with arrays of relationships (departments, positions, managers)

## Important Notes

- Only team_members table has a "Last Modified" field for incremental sync
- Departments and positions always sync fully to maintain relationship integrity
- Sync order matters: departments → positions → team_members
- Team members require two-pass sync for manager relationships
- Last sync timestamp stored in `hr.system_kv` table with key "last_sync_hr"
- Incremental sync significantly reduces API calls (e.g., 1 modified record vs 240 total)