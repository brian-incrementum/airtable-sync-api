from fastapi import FastAPI, Request, HTTPException
from sync import run_sync
import os
from dotenv import load_dotenv

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
async def cron():
    """Endpoint for automated hourly sync runs."""
    try:
        result = await run_sync()
        return {
            "status": "success",
            "message": "Sync completed successfully",
            "rows": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sync failed: {str(e)}"
        )

@app.post("/sync")
async def manual_sync(request: Request):
    """Manual sync endpoint with authentication via x-sync-key header."""
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
        result = await run_sync()
        return {
            "status": "success", 
            "message": "Manual sync completed successfully",
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