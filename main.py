from fastapi import FastAPI, Request, HTTPException, Query
from sync import run_sync
from sync_client import run_client_sync
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

app = FastAPI(
    title="Airtable Sync API",
    description="Sync HR and Client data from Airtable to Supabase",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Airtable Sync API is running"}

@app.get("/hr/cron")
async def hr_cron(sync_mode: Optional[str] = Query(default="incremental", regex="^(full|incremental)$")):
    """Endpoint for automated hourly HR sync runs.
    
    Args:
        sync_mode: 'full' or 'incremental' (default: incremental)
    """
    try:
        result = run_sync(sync_mode=sync_mode)
        return {
            "status": "success",
            "message": f"HR sync completed successfully (mode: {sync_mode})",
            "rows": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"HR sync failed: {str(e)}"
        )

@app.post("/hr/sync")
async def manual_hr_sync(
    request: Request,
    sync_mode: Optional[str] = Query(default="incremental", regex="^(full|incremental)$")
):
    """Manual HR sync endpoint with authentication via x-sync-key header.
    
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
        result = run_sync(sync_mode=sync_mode)
        return {
            "status": "success", 
            "message": f"Manual HR sync completed successfully (mode: {sync_mode})",
            "rows": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"HR sync failed: {str(e)}"
        )

# Client sync endpoints
@app.get("/client/cron")
async def client_cron(sync_mode: Optional[str] = Query(default="incremental", regex="^(full|incremental)$")):
    """Endpoint for automated hourly client sync runs.
    
    Args:
        sync_mode: 'full' or 'incremental' (default: incremental)
    """
    try:
        result = run_client_sync(sync_mode=sync_mode)
        return {
            "status": "success",
            "message": f"Client sync completed successfully (mode: {sync_mode})",
            "tables": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Client sync failed: {str(e)}"
        )

@app.post("/client/sync")
async def manual_client_sync(
    request: Request,
    sync_mode: Optional[str] = Query(default="incremental", regex="^(full|incremental)$")
):
    """Manual client sync endpoint with authentication via x-sync-key header.
    
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
        result = run_client_sync(sync_mode=sync_mode)
        return {
            "status": "success", 
            "message": f"Manual client sync completed successfully (mode: {sync_mode})",
            "tables": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Client sync failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)