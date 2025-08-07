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

def get_last_sync_timestamp() -> str:
    """Retrieve the last sync timestamp from system_kv table."""
    try:
        result = supabase.table("system_kv").select("value").eq("key", "last_sync_hr").single().execute()
        if result.data:
            return result.data.get("value")
    except Exception as e:
        print(f"No previous sync timestamp found: {e}")
    return None

def get_airtable_records(table_id: str, view: str = None, modified_since: str = None, table_name: str = None) -> List[Dict[str, Any]]:
    """Fetch records from an Airtable table with pagination and optional filtering.
    
    Args:
        table_id: The Airtable table ID
        view: Optional view name to use
        modified_since: Optional ISO timestamp to filter records modified after this time
        table_name: Optional table name for determining if Last Modified field exists
    """
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{table_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    params = {}
    if view:
        params["view"] = view
    
    # Only apply modified filter for team_members table which has Last Modified field
    if modified_since and table_name == "team_members":
        params["filterByFormula"] = f"{{Last Modified}} >= '{modified_since}'"
        print(f"  Filtering {table_name} for records modified since {modified_since}")
    
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
    
    if modified_since and table_name == "team_members":
        print(f"  Found {len(all_records)} modified records in {table_name}")
    
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

def upload_photo_to_supabase(photo_data: Dict[str, Any], airtable_id: str) -> Dict[str, Any]:
    """Download photo from Airtable and upload to Supabase Storage.
    
    Args:
        photo_data: Airtable photo attachment data
        airtable_id: The Airtable record ID for organizing photos
        
    Returns:
        Dict with Supabase Storage URL or None if upload fails
    """
    try:
        if not photo_data or not isinstance(photo_data, list) or len(photo_data) == 0:
            return None
            
        # Get the first photo
        photo = photo_data[0]
        photo_url = photo.get("url")
        filename = photo.get("filename", "photo.jpg")
        
        if not photo_url:
            return None
            
        # Check if photo already exists in Supabase
        storage_path = f"{airtable_id}/{filename}"
        
        # Try to get existing file
        try:
            existing = supabase.storage.from_("team-photos").list(airtable_id)
            if existing and any(f['name'] == filename for f in existing):
                # Photo already exists, return the URL
                public_url = supabase.storage.from_("team-photos").get_public_url(storage_path)
                print(f"  Photo already exists for {airtable_id}")
                return {
                    "url": public_url,
                    "filename": filename
                }
        except:
            pass  # File doesn't exist, proceed with upload
            
        # Download photo from Airtable with timeout
        print(f"  Downloading photo for {airtable_id}...")
        response = requests.get(photo_url, timeout=30)
        response.raise_for_status()
        
        # Upload to Supabase Storage
        file_data = response.content
        content_type = photo.get("type", "image/jpeg")
        
        print(f"  Uploading photo for {airtable_id} to Supabase...")
        upload_response = supabase.storage.from_("team-photos").upload(
            path=storage_path,
            file=file_data,
            file_options={"content-type": content_type, "upsert": "true"}
        )
        
        # Get the public URL
        public_url = supabase.storage.from_("team-photos").get_public_url(storage_path)
        print(f"  Successfully uploaded photo for {airtable_id}")
        
        return {
            "url": public_url,
            "filename": filename
        }
        
    except requests.exceptions.Timeout:
        print(f"  Warning: Timeout downloading photo for {airtable_id}")
        return None
    except Exception as e:
        print(f"  Warning: Failed to upload photo for {airtable_id}: {str(e)}")
        return None

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
    
    # Handle photo upload to Supabase Storage
    photo_data = fields.get("Photo")
    supabase_photo = upload_photo_to_supabase(photo_data, airtable_record["id"]) if photo_data else None
    
    return {
        "airtable_id": airtable_record["id"],
        "full_name": fields.get("Full Name", ""),
        # Store Supabase UUIDs directly in original fields
        "department": department_uuids,  # Array of Supabase department UUIDs
        "manager": manager_uuids,  # Array of Supabase team_member UUIDs
        "position": position_uuids,  # Array of Supabase position UUIDs
        # Other fields
        "photo": supabase_photo,  # Supabase Storage URL
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

def sync_departments(modified_since: str = None) -> int:
    """Sync department records from Airtable to Supabase.
    
    Args:
        modified_since: Optional ISO timestamp to filter modified records
    """
    print("Syncing departments...")
    
    # Fetch records from Airtable
    airtable_records = get_airtable_records(
        AIRTABLE_TABLES["departments"],
        modified_since=modified_since,
        table_name="departments"
    )
    
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

def sync_positions(modified_since: str = None) -> int:
    """Sync position records from Airtable to Supabase.
    
    Args:
        modified_since: Optional ISO timestamp to filter modified records
    """
    print("Syncing positions...")
    
    # First, get department mapping (Airtable ID -> Supabase UUID)
    dept_response = supabase.table("departments").select("id, airtable_id").execute()
    department_mapping = {dept["airtable_id"]: dept["id"] for dept in dept_response.data}
    
    # Fetch records from Airtable
    airtable_records = get_airtable_records(
        AIRTABLE_TABLES["positions"],
        modified_since=modified_since,
        table_name="positions"
    )
    
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

def sync_team_members(modified_since: str = None, skip_photos: bool = False) -> int:
    """Sync team member records from Airtable to Supabase.
    
    Args:
        modified_since: Optional ISO timestamp to filter modified records
        skip_photos: If True, skip photo processing (useful for incremental syncs)
    """
    print("Syncing team members...")
    
    # Get mapping dictionaries (Airtable ID -> Supabase UUID)
    dept_response = supabase.table("departments").select("id, airtable_id").execute()
    department_mapping = {dept["airtable_id"]: dept["id"] for dept in dept_response.data}
    
    pos_response = supabase.table("positions").select("id, airtable_id").execute()
    position_mapping = {pos["airtable_id"]: pos["id"] for pos in pos_response.data}
    
    # For team members, we need to do a two-pass sync since managers reference other team members
    # First pass: sync basic info without manager relationships
    airtable_records = get_airtable_records(
        AIRTABLE_TABLES["team_members"],
        modified_since=modified_since,
        table_name="team_members"
    )
    
    # Create initial team member mapping from existing records
    existing_tm_response = supabase.table("team_members").select("id, airtable_id").execute()
    team_member_mapping = {tm["airtable_id"]: tm["id"] for tm in existing_tm_response.data}
    
    # Map records to Supabase format
    print(f"  Processing {len(airtable_records)} team member records...")
    if not skip_photos and len(airtable_records) > 0:
        print(f"  Photo processing enabled - this may take several minutes...")
    
    supabase_records = []
    for i, record in enumerate(airtable_records, 1):
        if i % 10 == 0:
            print(f"  Processing record {i}/{len(airtable_records)}...")
        
        # For incremental syncs, skip photo processing to speed things up
        if skip_photos and modified_since:
            # Temporarily remove photo data to skip processing
            original_photo = record.get("fields", {}).get("Photo")
            if "fields" in record:
                record["fields"]["Photo"] = None
            
            mapped_record = map_team_member_record(record, department_mapping, position_mapping, team_member_mapping)
            
            # Restore original photo data (keep existing photo in DB)
            if original_photo and "fields" in record:
                record["fields"]["Photo"] = original_photo
                # Don't update photo field for this record
                del mapped_record["photo"]
        else:
            mapped_record = map_team_member_record(record, department_mapping, position_mapping, team_member_mapping)
        
        supabase_records.append(mapped_record)
    
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
            updated_records = []
            for record in airtable_records:
                # Skip photo processing in second pass
                if "fields" in record:
                    original_photo = record["fields"].get("Photo")
                    record["fields"]["Photo"] = None
                
                mapped_record = map_team_member_record(record, department_mapping, position_mapping, updated_team_member_mapping)
                del mapped_record["photo"]  # Don't update photo in second pass
                
                if "fields" in record and original_photo:
                    record["fields"]["Photo"] = original_photo
                    
                updated_records.append(mapped_record)
            
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

def run_sync(sync_mode: str = "incremental") -> Dict[str, int]:
    """Run the complete sync process in order: departments -> positions -> team_members.
    
    Args:
        sync_mode: Either 'full' for complete sync or 'incremental' for modified records only
    """
    print(f"Starting Airtable sync process (mode: {sync_mode})...")
    
    # Validate sync mode
    if sync_mode not in ["full", "incremental"]:
        print(f"Invalid sync mode '{sync_mode}', defaulting to 'incremental'")
        sync_mode = "incremental"
    
    # Get last sync timestamp for incremental mode
    modified_since = None
    original_sync_mode = sync_mode
    
    if sync_mode == "incremental":
        modified_since = get_last_sync_timestamp()
        if modified_since:
            print(f"Running incremental sync for changes since {modified_since}")
        else:
            print("No previous sync found, running full sync")
            sync_mode = "full"
    
    try:
        # For incremental sync, we need to sync all tables because:
        # 1. Departments/positions might affect team_members relationships
        # 2. We can't easily track dependencies across tables
        # However, only team_members has Last Modified field for filtering
        
        if sync_mode == "full":
            # Full sync - fetch all records and process photos
            dept_count = sync_departments()
            pos_count = sync_positions()
            member_count = sync_team_members(skip_photos=False)  # Process photos in full sync
        else:
            # Incremental sync - still need to sync all tables for relationships
            # But only team_members will actually filter by modified date
            try:
                dept_count = sync_departments()  # Always full for departments
                pos_count = sync_positions()     # Always full for positions
                member_count = sync_team_members(modified_since, skip_photos=True)  # Skip photos for speed
            except Exception as e:
                # If incremental sync fails, fall back to full sync
                print(f"Incremental sync failed: {str(e)}")
                print("Falling back to full sync...")
                dept_count = sync_departments()
                pos_count = sync_positions()
                member_count = sync_team_members(skip_photos=False)  # Process photos in fallback
                sync_mode = "full"  # Update mode to reflect what actually happened
        
        # Update sync timestamp only on successful sync
        update_last_sync_timestamp()
        
        result = {
            "departments": dept_count,
            "positions": pos_count,
            "team_members": member_count,
            "sync_mode": sync_mode,
            "requested_mode": original_sync_mode
        }
        
        if sync_mode != original_sync_mode:
            result["fallback_reason"] = "Incremental sync failed or no previous sync found"
        
        print(f"Sync completed successfully: {result}")
        return result
        
    except Exception as e:
        error_msg = f"Sync failed: {str(e)}"
        print(error_msg)
        # On failure, don't update timestamp so next sync can retry
        # Log additional context for debugging
        import traceback
        print(f"Error traceback: {traceback.format_exc()}")
        raise e

if __name__ == "__main__":
    run_sync()