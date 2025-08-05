# Airtable → Supabase HR Sync Service  
_Product Requirements Document_

## 1  Purpose  
Sync three Airtable tables into Supabase’s `hr` schema.  
*Departments*, *Positions*, and *Team Directory* will be mirrored on an hourly schedule and via a manual HTTP trigger.

## 2  Important context  
* The repository already contains three Markdown files in `context/`  
  * `context/departments.md`  
  * `context/positions.md`  
  * `context/team_members.md`  
* Each Markdown file lists **only** the fields that must be copied to Supabase.  
* The sample records inside those docs show Airtable’s full JSON response so the developer can see unused fields too.

## 3  Success metrics  

| Objective | Target |
|-----------|--------|
| Table definitions match Markdown specs | 100 % column parity |
| First full sync row parity | 100 % |
| Incremental sync latency | ≤ 60 minutes |
| Manual endpoint success | 200 OK in < 5 seconds |

## 4  Scope  

1. Create the three tables in `hr` exactly as described in the Markdown specs, plus an `airtable_id` text column and a UUID primary key.  
2. Build a Python FastAPI service that  
   1. runs a full sync at startup,  
   2. performs incremental upserts every hour,  
   3. exposes `/sync` for manual runs (protected by a shared secret header).  
3. Keep relationship integrity:  
   * `positions.department_id` must reference `hr.departments(id)`  
   * `team_members.position_id` must reference `hr.positions(id)`  

_Deployment to Railway is planned but **not required** for initial delivery. The developer should run everything locally until the logic is proven._

## 5  Developer workflow  

1. **Review the specs**  
   * Copy the column lists from the Markdown files.  
2. **Create tables in `hr`**  
   ```sql
   create schema if not exists hr;
   -- each table also gets airtable_id text unique

	3.	Write sync.py
	•	Fetch Airtable pages with requests or pyairtable.
	•	Use Supabase service-role key with supabase-py and table.upsert.
	•	Order of operations: departments → positions → team_members.
	•	Store last_sync_hr timestamp in system_kv table.
	4.	FastAPI endpoints
	•	GET /cron for automated runs.
	•	POST /sync for manual runs, header x-sync-key.
	5.	Local test loop
	•	Place secrets in .env.
	•	Run uvicorn app.main:app --reload.
	•	Call /sync, watch Supabase Studio for results.

6  API design

Route	Method	Auth	Purpose
/cron	GET	none	Hook for local scheduler or future Railway Cron
/sync	POST	header x-sync-key	Manual trigger

Example FastAPI skeleton:

from fastapi import FastAPI, Request, HTTPException
from sync import run_sync
import os

app = FastAPI()

@app.get("/cron")
async def cron():
    rows = await run_sync()
    return {"status": "ok", "rows": rows}

@app.post("/sync")
async def manual(req: Request):
    if req.headers.get("x-sync-key") != os.environ["SYNC_KEY"]:
        raise HTTPException(status_code=401)
    rows = await run_sync()
    return {"status": "ok", "rows": rows}

7  Testing checklist
	•	Unit tests for each mapping function.
	•	Full sync fills all three tables with correct counts.
	•	Editing a record in Airtable then running /sync updates exactly one row.
	•	Unauthorized request to /sync returns 401.


