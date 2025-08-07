#!/usr/bin/env python3
"""
Migration script to update existing client_meetings records with submitter_id values.
This script maps the existing submitter (Airtable record ID) to HR team member UUIDs.
"""

import os
import requests
from typing import Dict
from supabase import create_client, Client
from supabase.client import ClientOptions
from dotenv import load_dotenv
import time

load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_CLIENT_BASE_ID = "app36dpFPr84hM8TN"

# Initialize Supabase clients
client_supabase: Client = create_client(
    SUPABASE_URL, 
    SUPABASE_SERVICE_ROLE_KEY,
    options=ClientOptions(schema="client")
)

hr_supabase: Client = create_client(
    SUPABASE_URL, 
    SUPABASE_SERVICE_ROLE_KEY,
    options=ClientOptions(schema="hr")
)

def get_team_member_mapping() -> Dict[str, str]:
    """Create mapping between client team member Airtable IDs and HR team member UUIDs."""
    print("Building team member mapping...")
    
    # Get HR team members by airtable_id
    hr_result = hr_supabase.table("team_members").select("id, airtable_id").execute()
    hr_by_airtable_id = {record["airtable_id"]: record["id"] for record in hr_result.data}
    print(f"  Found {len(hr_by_airtable_id)} HR team members")
    
    # Fetch client team members from Airtable
    client_team_url = f"https://api.airtable.com/v0/{AIRTABLE_CLIENT_BASE_ID}/tbl2t9Ylc9kM7cfUG"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    
    all_client_team = []
    offset = None
    
    while True:
        params = {"pageSize": 100}
        if offset:
            params["offset"] = offset
            
        response = requests.get(client_team_url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        all_client_team.extend(data.get("records", []))
        
        offset = data.get("offset")
        if not offset:
            break
    
    print(f"  Found {len(all_client_team)} client team members in Airtable")
    
    # Create mapping: client_airtable_id -> hr_uuid using Source Record ID
    team_member_mapping = {}
    matched = 0
    unmatched_names = []
    
    for record in all_client_team:
        client_id = record["id"]
        fields = record.get("fields", {})
        source_record_id = fields.get("Source Record ID", "")
        
        if source_record_id and source_record_id in hr_by_airtable_id:
            team_member_mapping[client_id] = hr_by_airtable_id[source_record_id]
            matched += 1
        else:
            name = fields.get("Full Name", "Unknown")
            unmatched_names.append(name)
    
    print(f"  Successfully matched {matched} team members")
    if unmatched_names:
        print(f"  {len(unmatched_names)} unmatched team members (not found in HR)")
        if len(unmatched_names) <= 5:
            for name in unmatched_names[:5]:
                print(f"    - {name}")
    
    return team_member_mapping

def migrate_submitter_ids():
    """Migrate existing client_meetings records to populate submitter_id."""
    
    # Get team member mapping
    team_member_mapping = get_team_member_mapping()
    
    # Get all unique submitter values from client_meetings
    print("\nAnalyzing existing submitter data...")
    
    # Get all records with submitters
    result = client_supabase.table("client_meetings")\
        .select("submitter")\
        .neq("submitter", "")\
        .not_.is_("submitter", "null")\
        .execute()
    
    # Count unique submitters
    submitter_counts = {}
    for record in result.data:
        submitter = record.get('submitter')
        if submitter:
            submitter_counts[submitter] = submitter_counts.get(submitter, 0) + 1
    
    # Sort by count
    unique_submitters = [
        {'submitter': k, 'count': v} 
        for k, v in sorted(submitter_counts.items(), key=lambda x: x[1], reverse=True)
    ]
    
    print(f"  Found {len(unique_submitters)} unique submitter IDs to process")
    
    # Process each unique submitter
    total_updated = 0
    mapped_count = 0
    unmapped_submitters = []
    
    for idx, submitter_data in enumerate(unique_submitters, 1):
        submitter_airtable_id = submitter_data['submitter']
        record_count = submitter_data['count']
        
        print(f"\nProcessing submitter {idx}/{len(unique_submitters)}: {submitter_airtable_id} ({record_count} records)")
        
        # Check if we have a mapping for this submitter
        if submitter_airtable_id in team_member_mapping:
            hr_uuid = team_member_mapping[submitter_airtable_id]
            
            # Update all records with this submitter in batches
            batch_size = 100
            offset = 0
            
            while True:
                # Get batch of records
                batch_result = client_supabase.table("client_meetings")\
                    .select("id")\
                    .eq("submitter", submitter_airtable_id)\
                    .range(offset, offset + batch_size - 1)\
                    .execute()
                
                if not batch_result.data:
                    break
                
                # Update batch
                ids = [record['id'] for record in batch_result.data]
                
                for meeting_id in ids:
                    client_supabase.table("client_meetings")\
                        .update({
                            "submitter_id": hr_uuid
                        })\
                        .eq("id", meeting_id)\
                        .execute()
                
                updated_count = len(ids)
                total_updated += updated_count
                print(f"    Updated batch of {updated_count} records")
                
                if len(batch_result.data) < batch_size:
                    break
                
                offset += batch_size
                time.sleep(0.1)  # Small delay to avoid rate limiting
            
            mapped_count += 1
        else:
            unmapped_submitters.append((submitter_airtable_id, record_count))
            print(f"    No mapping found for {submitter_airtable_id}")
    
    # Summary
    print("\n" + "="*50)
    print("Migration Summary:")
    print(f"  Total unique submitters: {len(unique_submitters)}")
    print(f"  Successfully mapped: {mapped_count}")
    print(f"  Unmapped submitters: {len(unmapped_submitters)}")
    print(f"  Total records updated: {total_updated}")
    
    if unmapped_submitters:
        print("\nUnmapped submitters (need manual review):")
        for airtable_id, count in unmapped_submitters[:10]:
            print(f"    {airtable_id}: {count} records")
        if len(unmapped_submitters) > 10:
            print(f"    ... and {len(unmapped_submitters) - 10} more")

if __name__ == "__main__":
    print("Starting submitter ID migration...")
    try:
        migrate_submitter_ids()
        print("\nMigration completed successfully!")
    except Exception as e:
        print(f"\nError during migration: {e}")
        import traceback
        traceback.print_exc()