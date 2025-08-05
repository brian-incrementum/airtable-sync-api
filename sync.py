import os
import requests
from datetime import datetime, timezone
from typing import Dict, List, Any
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")

# Table configurations from context files
AIRTABLE_TABLES = {
    "departments": "tblHhOw2PAG29NIir",
    "positions": "tbldrYoS9nkpqLGoA", 
    "team_members": "tblJiYy00NA25LBpu"
}

# Initialize Supabase client with hr schema
from supabase.client import ClientOptions
supabase: Client = create_client(
    SUPABASE_URL, 
    SUPABASE_SERVICE_ROLE_KEY,
    options=ClientOptions(schema="hr")
)

def get_airtable_records(table_id: str, view: str = None) -> List[Dict[str, Any]]:
    """Fetch all records from an Airtable table with pagination."""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{table_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    params = {}
    if view:
        params["view"] = view
    
    all_records = []
    offset = None
    
    while True:
        if offset:
            params["offset"] = offset
            
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        all_records.extend(data.get("records", []))
        
        offset = data.get("offset")
        if not offset:
            break
            
    return all_records

def map_department_record(airtable_record: Dict[str, Any]) -> Dict[str, Any]:
    """Map Airtable department record to Supabase format."""
    fields = airtable_record.get("fields", {})
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", "")
    }

def map_position_record(airtable_record: Dict[str, Any], department_mapping: Dict[str, str]) -> Dict[str, Any]:
    """Map Airtable position record to Supabase format."""
    fields = airtable_record.get("fields", {})
    
    # Map department reference
    department_id = None
    department_refs = fields.get("Department", [])
    if department_refs and len(department_refs) > 0:
        department_airtable_id = department_refs[0]
        department_id = department_mapping.get(department_airtable_id)
    
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", ""),
        "department_id": department_id
    }

def map_team_member_record(
    airtable_record: Dict[str, Any], 
    department_mapping: Dict[str, str],
    position_mapping: Dict[str, str],
    team_member_mapping: Dict[str, str]
) -> Dict[str, Any]:
    """Map Airtable team member record to Supabase format with UUID relationships."""
    fields = airtable_record.get("fields", {})
    
    # Get Airtable reference arrays
    department_airtable_ids = fields.get("Department", [])
    position_airtable_ids = fields.get("Position", [])
    manager_airtable_ids = fields.get("Manager", [])
    
    # Convert to Supabase UUIDs - store directly in original fields
    department_uuids = [department_mapping.get(aid) for aid in department_airtable_ids if department_mapping.get(aid)]
    position_uuids = [position_mapping.get(aid) for aid in position_airtable_ids if position_mapping.get(aid)]
    manager_uuids = [team_member_mapping.get(aid) for aid in manager_airtable_ids if team_member_mapping.get(aid)]
    
    return {
        "airtable_id": airtable_record["id"],
        "full_name": fields.get("Full Name", ""),
        # Store Supabase UUIDs directly in original fields
        "department": department_uuids,  # Array of Supabase department UUIDs
        "manager": manager_uuids,  # Array of Supabase team_member UUIDs
        "position": position_uuids,  # Array of Supabase position UUIDs
        # Other fields
        "photo": fields.get("Photo"),  # Photo attachment data
        "status": fields.get("Status"),
        "company_email": fields.get("Company email"),
        "phone": fields.get("Phone"),
        "start_date": fields.get("Start date"),
        "last_date": fields.get("Last Date"),
        "dob": fields.get("DOB"),
        "personal_email": fields.get("Personal Email"),
        "country": fields.get("Country"),
        "slack_id": fields.get("Slack ID"),
        "click_up_id": fields.get("Click Up ID"),
        "hs_user_id": fields.get("HS User ID"),
        "government_id": fields.get("Government ID"),
        "id_expiration_date": fields.get("ID Expiration Date"),
        "active_lastpass": fields.get("Active Lastpass")
    }

def sync_departments() -> int:
    """Sync department records from Airtable to Supabase."""
    print("Syncing departments...")
    
    # Fetch records from Airtable
    airtable_records = get_airtable_records(AIRTABLE_TABLES["departments"])
    
    # Map records to Supabase format
    supabase_records = [map_department_record(record) for record in airtable_records]
    
    # Upsert to Supabase
    if supabase_records:
        result = supabase.table("departments").upsert(
            supabase_records,
            on_conflict="airtable_id"
        ).execute()
        
        print(f"Synced {len(supabase_records)} department records")
        return len(supabase_records)
    
    return 0

def sync_positions() -> int:
    """Sync position records from Airtable to Supabase."""
    print("Syncing positions...")
    
    # First, get department mapping (Airtable ID -> Supabase UUID)
    dept_response = supabase.table("departments").select("id, airtable_id").execute()
    department_mapping = {dept["airtable_id"]: dept["id"] for dept in dept_response.data}
    
    # Fetch records from Airtable
    airtable_records = get_airtable_records(AIRTABLE_TABLES["positions"])
    
    # Map records to Supabase format
    supabase_records = [
        map_position_record(record, department_mapping) 
        for record in airtable_records
    ]
    
    # Upsert to Supabase
    if supabase_records:
        result = supabase.table("positions").upsert(
            supabase_records,
            on_conflict="airtable_id"
        ).execute()
        
        print(f"Synced {len(supabase_records)} position records")
        return len(supabase_records)
    
    return 0

def sync_team_members() -> int:
    """Sync team member records from Airtable to Supabase."""
    print("Syncing team members...")
    
    # Get mapping dictionaries (Airtable ID -> Supabase UUID)
    dept_response = supabase.table("departments").select("id, airtable_id").execute()
    department_mapping = {dept["airtable_id"]: dept["id"] for dept in dept_response.data}
    
    pos_response = supabase.table("positions").select("id, airtable_id").execute()
    position_mapping = {pos["airtable_id"]: pos["id"] for pos in pos_response.data}
    
    # For team members, we need to do a two-pass sync since managers reference other team members
    # First pass: sync basic info without manager relationships
    airtable_records = get_airtable_records(AIRTABLE_TABLES["team_members"])
    
    # Create initial team member mapping from existing records
    existing_tm_response = supabase.table("team_members").select("id, airtable_id").execute()
    team_member_mapping = {tm["airtable_id"]: tm["id"] for tm in existing_tm_response.data}
    
    # Map records to Supabase format
    supabase_records = [
        map_team_member_record(record, department_mapping, position_mapping, team_member_mapping) 
        for record in airtable_records
    ]
    
    # Upsert to Supabase
    if supabase_records:
        result = supabase.table("team_members").upsert(
            supabase_records,
            on_conflict="airtable_id"
        ).execute()
        
        # After first upsert, update team member mapping for manager relationships
        updated_tm_response = supabase.table("team_members").select("id, airtable_id").execute()
        updated_team_member_mapping = {tm["airtable_id"]: tm["id"] for tm in updated_tm_response.data}
        
        # Second pass: update manager relationships now that all team members exist
        if updated_team_member_mapping != team_member_mapping:
            updated_records = [
                map_team_member_record(record, department_mapping, position_mapping, updated_team_member_mapping) 
                for record in airtable_records
            ]
            
            supabase.table("team_members").upsert(
                updated_records,
                on_conflict="airtable_id"
            ).execute()
        
        print(f"Synced {len(supabase_records)} team member records")
        return len(supabase_records)
    
    return 0

def update_last_sync_timestamp():
    """Update the sync timestamp in system_kv table."""
    timestamp = datetime.now(timezone.utc).isoformat()
    supabase.table("system_kv").upsert({
        "key": "last_sync_hr",
        "value": timestamp
    }, on_conflict="key").execute()
    
    print(f"Updated last sync timestamp: {timestamp}")

async def run_sync() -> Dict[str, int]:
    """Run the complete sync process in order: departments -> positions -> team_members."""
    print("Starting Airtable sync process...")
    
    try:
        # Sync in dependency order
        dept_count = sync_departments()
        pos_count = sync_positions()
        member_count = sync_team_members()
        
        # Update sync timestamp
        update_last_sync_timestamp()
        
        result = {
            "departments": dept_count,
            "positions": pos_count,
            "team_members": member_count
        }
        
        print(f"Sync completed successfully: {result}")
        return result
        
    except Exception as e:
        print(f"Sync failed: {str(e)}")
        raise e

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_sync())