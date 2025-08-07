import os
import requests
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_CLIENT_BASE_ID = "app36dpFPr84hM8TN"  # Client base ID from context files

# Table configurations from context files
AIRTABLE_CLIENT_TABLES = {
    "companies": "tbl35cnxFSmMnBQYL",
    "services": "tblTYmxXucxldO4Md",
    "marketplaces": "tblsjMd2w00cu5qV8",
    "saas_tools": "tblTWlmmBcZWImDM6",
    "accounts": "tblLb0ek0O4HiB3OY",
    "account_services_details": "tblLK5hswpid4nH8c",
    "contracts": "tblu0LdsOvLh3aaHI",
    "console_login_emails": "tblk7kVfDShzc5S4j",
    "client_meetings": "tblV3ZIKJfdYcUuSG"
}

# Initialize Supabase client with client schema
from supabase.client import ClientOptions
supabase: Client = create_client(
    SUPABASE_URL, 
    SUPABASE_SERVICE_ROLE_KEY,
    options=ClientOptions(schema="client")
)

def get_last_sync_timestamp() -> Optional[str]:
    """Retrieve the last sync timestamp from system_kv table."""
    try:
        result = supabase.table("system_kv").select("value").eq("key", "last_sync_client").single().execute()
        if result.data:
            return result.data.get("value")
    except Exception as e:
        print(f"No previous sync timestamp found: {e}")
    return None

def update_last_sync_timestamp(timestamp: str):
    """Update the last sync timestamp in system_kv table."""
    try:
        supabase.table("system_kv").upsert({
            "key": "last_sync_client",
            "value": timestamp,
            "updated_at": datetime.now(timezone.utc).isoformat()
        }).execute()
    except Exception as e:
        print(f"Error updating sync timestamp: {e}")

def get_airtable_records(table_id: str, modified_since: str = None, table_name: str = None) -> List[Dict[str, Any]]:
    """Fetch records from an Airtable table with pagination and optional filtering."""
    url = f"https://api.airtable.com/v0/{AIRTABLE_CLIENT_BASE_ID}/{table_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    params = {}
    
    # Only apply modified filter for tables with Last Modified field
    if modified_since and table_name in ["account_services_details", "client_meetings"]:
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
    
    if modified_since and table_name in ["account_services_details", "client_meetings"]:
        print(f"  Found {len(all_records)} modified records in {table_name}")
    
    return all_records

def get_id_mapping(table_name: str) -> Dict[str, str]:
    """Get mapping of Airtable IDs to Supabase UUIDs for a table."""
    try:
        result = supabase.table(table_name).select("id, airtable_id").execute()
        return {record["airtable_id"]: record["id"] for record in result.data}
    except Exception as e:
        print(f"Error getting ID mapping for {table_name}: {e}")
        return {}

def map_company_record(airtable_record: Dict[str, Any]) -> Dict[str, Any]:
    """Map Airtable company record to Supabase format."""
    fields = airtable_record.get("fields", {})
    return {
        "airtable_id": airtable_record["id"],
        "company_name": fields.get("Company Name", ""),
        "hubspot_id": fields.get("Hubspot ID", "")
    }

def map_service_record(airtable_record: Dict[str, Any]) -> Dict[str, Any]:
    """Map Airtable service record to Supabase format."""
    fields = airtable_record.get("fields", {})
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", ""),
        "description": fields.get("Description", "")
    }

def map_marketplace_record(airtable_record: Dict[str, Any]) -> Dict[str, Any]:
    """Map Airtable marketplace record to Supabase format."""
    fields = airtable_record.get("fields", {})
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", "")
    }

def map_saas_tool_record(airtable_record: Dict[str, Any]) -> Dict[str, Any]:
    """Map Airtable SaaS tool record to Supabase format."""
    fields = airtable_record.get("fields", {})
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", "")
    }

def map_account_record(airtable_record: Dict[str, Any], company_mapping: Dict[str, str]) -> Dict[str, Any]:
    """Map Airtable account record to Supabase format."""
    fields = airtable_record.get("fields", {})
    
    # Map company reference (take first if multiple)
    company_id = None
    company_refs = fields.get("Companies", [])
    if company_refs and len(company_refs) > 0:
        company_airtable_id = company_refs[0]
        company_id = company_mapping.get(company_airtable_id)
    
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", ""),
        "company_id": company_id,
        "sub_account_hubspot_id": fields.get("Sub Account Hubspot ID", ""),
        "stripe_id": fields.get("Stripe_ID", "")
    }

def map_account_service_detail_record(
    airtable_record: Dict[str, Any],
    account_mapping: Dict[str, str],
    service_mapping: Dict[str, str],
    team_member_mapping: Dict[str, str] = None
) -> Dict[str, Any]:
    """Map Airtable account service detail record to Supabase format."""
    fields = airtable_record.get("fields", {})
    
    # Map account reference
    account_id = None
    account_refs = fields.get("Account", [])
    if account_refs and len(account_refs) > 0:
        account_id = account_mapping.get(account_refs[0])
    
    # Map service reference
    service_id = None
    service_refs = fields.get("Service", [])
    if service_refs and len(service_refs) > 0:
        service_id = service_mapping.get(service_refs[0])
    
    # Map account manager reference
    account_manager_id = None
    account_manager_airtable_id = None
    manager_refs = fields.get("Account Manager", [])
    if manager_refs and len(manager_refs) > 0:
        account_manager_airtable_id = manager_refs[0]
        if team_member_mapping:
            account_manager_id = team_member_mapping.get(account_manager_airtable_id)
    
    # Parse dates
    service_start_date = fields.get("Service Start Date")
    service_cancel_date = fields.get("Service Cancel Date")
    yearly_renewal_date = fields.get("Yearly Renewal Date")
    
    # Parse last modified timestamp
    last_modified = fields.get("Last Modified")
    if last_modified:
        last_modified = datetime.fromisoformat(last_modified.replace('Z', '+00:00')).isoformat()
    
    return {
        "airtable_id": airtable_record["id"],
        "record_id": fields.get("Record ID", ""),
        "account_id": account_id,
        "service_id": service_id,
        "account_manager_id": account_manager_id,
        "account_manager_airtable_id": account_manager_airtable_id,
        "storefront_name": fields.get("Storefront Name", ""),
        "service_start_date": service_start_date,
        "service_cancel_date": service_cancel_date,
        "pricing_terms": fields.get("Pricing Terms", ""),
        "renewal_type": fields.get("Renewal Type", ""),
        "cancellation_reason": fields.get("Cancellation Reason", ""),
        "yearly_renewal_date": yearly_renewal_date,
        "minimum_fee": fields.get("Minimum Fee"),
        "ad_console_name": fields.get("Ad Console Name", ""),
        "seller_type": fields.get("Seller Type", ""),
        "data_owl": fields.get("Data Owl", False),
        "data_owl_title": fields.get("Data Owl Title", ""),
        "partner_network": fields.get("Partner Network", False),
        "last_billing_period_ad_spend": fields.get("Last Billing Period Ad Spend"),
        "billing_day": fields.get("Billing Day"),
        "clickup_onboarding_link": fields.get("ClickUp Onboarding Link", ""),
        "slack_channel_id": fields.get("Slack Channel ID", ""),
        "main_contact_slack_id": fields.get("Main Contact Slack ID", ""),
        "last_modified": last_modified
    }

def map_contract_record(airtable_record: Dict[str, Any]) -> Dict[str, Any]:
    """Map Airtable contract record to Supabase format."""
    fields = airtable_record.get("fields", {})
    
    agreement_date = fields.get("Agreement Date")
    
    return {
        "airtable_id": airtable_record["id"],
        "record_id": fields.get("Record ID", ""),
        "agreement_date": agreement_date,
        "agreement_title": fields.get("Agreement Title", ""),
        "link_to_google_drive": fields.get("Link to Google Drive", "")
    }

def map_console_login_email_record(
    airtable_record: Dict[str, Any],
    account_service_mapping: Dict[str, str]
) -> Dict[str, Any]:
    """Map Airtable console login email record to Supabase format."""
    fields = airtable_record.get("fields", {})
    
    # Map account service reference
    account_service_id = None
    service_refs = fields.get("Brand Services", [])
    if service_refs and len(service_refs) > 0:
        account_service_id = account_service_mapping.get(service_refs[0])
    
    return {
        "airtable_id": airtable_record["id"],
        "name": fields.get("Name", ""),
        "email": fields.get("Email", ""),
        "google_voice": fields.get("Google Voice", ""),
        "account_service_id": account_service_id
    }

def map_client_meeting_record(
    airtable_record: Dict[str, Any],
    account_mapping: Dict[str, str]
) -> Dict[str, Any]:
    """Map Airtable client meeting record to Supabase format."""
    fields = airtable_record.get("fields", {})
    
    # Map account reference
    account_id = None
    account_refs = fields.get("Accounts", [])
    if account_refs and len(account_refs) > 0:
        account_id = account_mapping.get(account_refs[0])
    
    # Parse dates
    meeting_date = fields.get("Meeting Date")
    
    # Parse last modified timestamp
    last_modified = fields.get("Last Modified")
    if last_modified:
        last_modified = datetime.fromisoformat(last_modified.replace('Z', '+00:00')).isoformat()
    
    return {
        "airtable_id": airtable_record["id"],
        "record_id": fields.get("Record ID", ""),
        "submitter": fields.get("Submitter", [""])[0] if fields.get("Submitter") else "",
        "account_id": account_id,
        "meeting_date": meeting_date,
        "meeting_type": fields.get("Meeting Type", ""),
        "transcript": fields.get("Transcript", ""),
        "follow_up_message": fields.get("Follow Up Message", ""),
        "meeting_analysis": fields.get("Meeting Analysis", ""),
        "sentiment": fields.get("Sentiment", ""),
        "sentiment_explained": fields.get("Sentiment Explained", ""),
        "risk_level": fields.get("Risk Level", ""),
        "risk_explained": fields.get("Risk Explained", ""),
        "predicted_intentions": fields.get("Predicted Intentions", ""),
        "share_link": fields.get("Share Link", ""),
        "services_text": fields.get("Services_Text", ""),
        "last_modified": last_modified
    }

def sync_junction_table(
    table_name: str,
    parent_id: str,
    child_ids: List[str],
    parent_field: str,
    child_field: str,
    child_mapping: Dict[str, str]
):
    """Sync records for a junction table (many-to-many relationship)."""
    if not child_ids:
        return
    
    # Delete existing relationships
    supabase.table(table_name).delete().eq(parent_field, parent_id).execute()
    
    # Insert new relationships
    records = []
    for child_airtable_id in child_ids:
        child_uuid = child_mapping.get(child_airtable_id)
        if child_uuid:
            records.append({
                parent_field: parent_id,
                child_field: child_uuid
            })
    
    if records:
        supabase.table(table_name).insert(records).execute()

def run_client_sync(sync_mode: str = "incremental") -> Dict[str, int]:
    """Run the client data sync from Airtable to Supabase.
    
    Args:
        sync_mode: 'full' or 'incremental'
    
    Returns:
        Dictionary with counts of synced records per table
    """
    print(f"\n=== Starting Client Sync ({sync_mode} mode) ===")
    
    # Get last sync timestamp for incremental sync
    last_sync = None
    if sync_mode == "incremental":
        last_sync = get_last_sync_timestamp()
        if last_sync:
            print(f"Last sync: {last_sync}")
        else:
            print("No previous sync found, falling back to full sync")
            sync_mode = "full"
    
    sync_counts = {}
    current_timestamp = datetime.now(timezone.utc).isoformat()
    
    try:
        # 1. Sync root tables (no dependencies)
        print("\n1. Syncing root tables...")
        
        # Companies
        print("  Syncing companies...")
        companies = get_airtable_records(AIRTABLE_CLIENT_TABLES["companies"], table_name="companies")
        for record in companies:
            mapped = map_company_record(record)
            supabase.table("companies").upsert(mapped, on_conflict="airtable_id").execute()
        sync_counts["companies"] = len(companies)
        company_mapping = get_id_mapping("companies")
        
        # Services
        print("  Syncing services...")
        services = get_airtable_records(AIRTABLE_CLIENT_TABLES["services"], table_name="services")
        for record in services:
            mapped = map_service_record(record)
            supabase.table("services").upsert(mapped, on_conflict="airtable_id").execute()
        sync_counts["services"] = len(services)
        service_mapping = get_id_mapping("services")
        
        # Marketplaces
        print("  Syncing marketplaces...")
        marketplaces = get_airtable_records(AIRTABLE_CLIENT_TABLES["marketplaces"], table_name="marketplaces")
        for record in marketplaces:
            mapped = map_marketplace_record(record)
            supabase.table("marketplaces").upsert(mapped, on_conflict="airtable_id").execute()
        sync_counts["marketplaces"] = len(marketplaces)
        marketplace_mapping = get_id_mapping("marketplaces")
        
        # SaaS Tools
        print("  Syncing SaaS tools...")
        saas_tools = get_airtable_records(AIRTABLE_CLIENT_TABLES["saas_tools"], table_name="saas_tools")
        for record in saas_tools:
            mapped = map_saas_tool_record(record)
            supabase.table("saas_tools").upsert(mapped, on_conflict="airtable_id").execute()
        sync_counts["saas_tools"] = len(saas_tools)
        saas_tool_mapping = get_id_mapping("saas_tools")
        
        # 2. Sync accounts (depends on companies)
        print("\n2. Syncing accounts...")
        accounts = get_airtable_records(AIRTABLE_CLIENT_TABLES["accounts"], table_name="accounts")
        for record in accounts:
            mapped = map_account_record(record, company_mapping)
            supabase.table("accounts").upsert(mapped, on_conflict="airtable_id").execute()
        sync_counts["accounts"] = len(accounts)
        account_mapping = get_id_mapping("accounts")
        
        # Create mapping between client team members and HR team members using Source Record ID
        print("\n2.5. Creating team member mapping between client and HR...")
        team_member_mapping = {}
        try:
            # First, get HR team members by airtable_id
            from supabase.client import ClientOptions
            hr_supabase = create_client(
                SUPABASE_URL, 
                SUPABASE_SERVICE_ROLE_KEY,
                options=ClientOptions(schema="hr")
            )
            hr_result = hr_supabase.table("team_members").select("id, airtable_id").execute()
            hr_by_airtable_id = {record["airtable_id"]: record["id"] for record in hr_result.data}
            print(f"  Found {len(hr_by_airtable_id)} HR team members")
            
            # Now fetch client team members from Airtable
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
            matched = 0
            unmatched = []
            for record in all_client_team:
                client_id = record["id"]
                fields = record.get("fields", {})
                source_record_id = fields.get("Source Record ID", "")
                
                if source_record_id and source_record_id in hr_by_airtable_id:
                    team_member_mapping[client_id] = hr_by_airtable_id[source_record_id]
                    matched += 1
                else:
                    name = fields.get("Full Name", "Unknown")
                    if source_record_id:
                        unmatched.append((name, source_record_id))
            
            print(f"  Successfully matched {matched} team members using Source Record ID")
            if unmatched and len(unmatched) <= 5:
                print(f"  Unmatched examples (not found in HR):")
                for name, source_id in unmatched[:5]:
                    print(f"    - {name} (Source ID: {source_id})")
                    
        except Exception as e:
            print(f"  Warning: Could not create team member mapping: {e}")
            import traceback
            traceback.print_exc()
        
        # 3. Sync account service details (depends on accounts, services)
        print("\n3. Syncing account service details...")
        account_services = get_airtable_records(
            AIRTABLE_CLIENT_TABLES["account_services_details"],
            modified_since=last_sync,
            table_name="account_services_details"
        )
        
        for record in account_services:
            fields = record.get("fields", {})
            mapped = map_account_service_detail_record(record, account_mapping, service_mapping, team_member_mapping)
            
            # Upsert the main record
            result = supabase.table("account_services_details").upsert(mapped, on_conflict="airtable_id").execute()
            
            if result.data and len(result.data) > 0:
                service_detail_id = result.data[0]["id"]
                
                # Sync marketplaces (many-to-many)
                marketplace_refs = fields.get("Marketplaces", [])
                sync_junction_table(
                    "account_services_marketplaces",
                    service_detail_id,
                    marketplace_refs,
                    "account_service_id",
                    "marketplace_id",
                    marketplace_mapping
                )
                
                # Sync SaaS tools (many-to-many)
                tool_refs = fields.get("Software Tools", [])
                sync_junction_table(
                    "account_services_saas_tools",
                    service_detail_id,
                    tool_refs,
                    "account_service_id",
                    "saas_tool_id",
                    saas_tool_mapping
                )
        
        sync_counts["account_services_details"] = len(account_services)
        account_service_mapping = get_id_mapping("account_services_details")
        
        # 4. Sync contracts
        print("\n4. Syncing contracts...")
        contracts = get_airtable_records(AIRTABLE_CLIENT_TABLES["contracts"], table_name="contracts")
        for record in contracts:
            fields = record.get("fields", {})
            mapped = map_contract_record(record)
            
            # Upsert the main record
            result = supabase.table("contracts").upsert(mapped, on_conflict="airtable_id").execute()
            
            if result.data and len(result.data) > 0:
                contract_id = result.data[0]["id"]
                
                # Sync services (many-to-many)
                service_refs = fields.get("Services", [])
                sync_junction_table(
                    "contracts_services",
                    contract_id,
                    service_refs,
                    "contract_id",
                    "service_id",
                    service_mapping
                )
                
                # Sync account services (many-to-many)
                account_service_refs = fields.get("Brand Services", [])
                sync_junction_table(
                    "contracts_account_services",
                    contract_id,
                    account_service_refs,
                    "contract_id",
                    "account_service_id",
                    account_service_mapping
                )
        
        sync_counts["contracts"] = len(contracts)
        
        # 5. Sync console login emails
        print("\n5. Syncing console login emails...")
        login_emails = get_airtable_records(AIRTABLE_CLIENT_TABLES["console_login_emails"], table_name="console_login_emails")
        for record in login_emails:
            mapped = map_console_login_email_record(record, account_service_mapping)
            supabase.table("console_login_emails").upsert(mapped, on_conflict="airtable_id").execute()
        sync_counts["console_login_emails"] = len(login_emails)
        
        # 6. Sync client meetings
        print("\n6. Syncing client meetings...")
        meetings = get_airtable_records(
            AIRTABLE_CLIENT_TABLES["client_meetings"],
            modified_since=last_sync,
            table_name="client_meetings"
        )
        
        for record in meetings:
            fields = record.get("fields", {})
            mapped = map_client_meeting_record(record, account_mapping)
            
            # Upsert the main record
            result = supabase.table("client_meetings").upsert(mapped, on_conflict="airtable_id").execute()
            
            if result.data and len(result.data) > 0:
                meeting_id = result.data[0]["id"]
                
                # Sync services (many-to-many)
                service_refs = fields.get("Services", [])
                sync_junction_table(
                    "client_meetings_services",
                    meeting_id,
                    service_refs,
                    "meeting_id",
                    "service_id",
                    service_mapping
                )
        
        sync_counts["client_meetings"] = len(meetings)
        
        # Update last sync timestamp
        if sync_mode == "incremental":
            update_last_sync_timestamp(current_timestamp)
            print(f"\nUpdated sync timestamp to: {current_timestamp}")
        
        print("\n=== Client Sync Complete ===")
        print("Synced records:")
        for table, count in sync_counts.items():
            print(f"  {table}: {count}")
        
        return sync_counts
        
    except Exception as e:
        print(f"\nError during sync: {e}")
        if sync_mode == "incremental":
            print("Falling back to full sync...")
            return run_client_sync(sync_mode="full")
        raise

if __name__ == "__main__":
    import sys
    
    # Check for command line arguments
    sync_mode = "incremental"
    if len(sys.argv) > 1 and sys.argv[1] == "--full":
        sync_mode = "full"
    
    # Run the sync
    result = run_client_sync(sync_mode=sync_mode)
    print(f"\nSync completed. Total records synced: {sum(result.values())}")