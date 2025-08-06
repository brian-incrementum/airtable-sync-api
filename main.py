from fastapi import FastAPI, Request, HTTPException, Query
from sync import run_sync
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

app = FastAPI(
    title="Airtable HR Sync API",
    description="Sync HR data from Airtable to Supabase",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Airtable HR Sync API is running"}

@app.get("/cron")
async def cron(sync_mode: Optional[str] = Query(default="incremental", regex="^(full|incremental)$")):
    """Endpoint for automated hourly sync runs.
    
    Args:
        sync_mode: 'full' or 'incremental' (default: incremental)
    """
    try:
        result = await run_sync(sync_mode=sync_mode)
        return {
            "status": "success",
            "message": f"Sync completed successfully (mode: {sync_mode})",
            "rows": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sync failed: {str(e)}"
        )

@app.post("/sync")
async def manual_sync(
    request: Request,
    sync_mode: Optional[str] = Query(default="incremental", regex="^(full|incremental)$")
):
    """Manual sync endpoint with authentication via x-sync-key header.
    
    Args:
        sync_mode: 'full' or 'incremental' (default: incremental)
    """
    # Check authentication
    sync_key = request.headers.get("x-sync-key")
    expected_key = os.getenv("SYNC_KEY")
    
    if not expected_key:
        raise HTTPException(
            status_code=500,
            detail="SYNC_KEY not configured"
        )
    
    if sync_key != expected_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing x-sync-key header"
        )
    
    try:
        result = await run_sync(sync_mode=sync_mode)
        return {
            "status": "success", 
            "message": f"Manual sync completed successfully (mode: {sync_mode})",
            "rows": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sync failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)