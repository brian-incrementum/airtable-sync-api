#!/usr/bin/env python3
"""
Test script to verify the Airtable sync setup.
"""
import os
import sys
from dotenv import load_dotenv

def test_environment():
    """Test that all required environment variables are set."""
    load_dotenv()
    
    required_vars = [
        "SUPABASE_URL",
        "SUPABASE_SERVICE_ROLE_KEY", 
        "AIRTABLE_API_KEY",
        "AIRTABLE_BASE_ID",
        "SYNC_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var) or os.getenv(var) == f"your_{var.lower()}_here":
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing or placeholder environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        return False
    
    print("✅ All environment variables are set")
    return True

def test_imports():
    """Test that all required packages can be imported."""
    try:
        import fastapi
        import uvicorn
        import supabase
        import requests
        print("✅ All required packages imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_supabase_connection():
    """Test connection to Supabase."""
    try:
        from supabase import create_client
        from supabase.client import ClientOptions
        
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        
        if not url or not key or key == "your_service_role_key_here":
            print("❌ Supabase credentials not properly configured")
            return False
            
        client = create_client(url, key, options=ClientOptions(schema="hr"))
        
        # Test basic connection by checking system_kv table
        result = client.table("system_kv").select("*").limit(1).execute()
        print("✅ Supabase connection successful")
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False

def test_airtable_connection():
    """Test connection to Airtable."""
    try:
        import requests
        
        api_key = os.getenv("AIRTABLE_API_KEY")
        base_id = os.getenv("AIRTABLE_BASE_ID")
        
        if not api_key or not base_id:
            print("❌ Airtable credentials not configured")
            return False
        
        # Test with departments table
        url = f"https://api.airtable.com/v0/{base_id}/tblHhOw2PAG29NIir"
        headers = {"Authorization": f"Bearer {api_key}"}
        
        response = requests.get(url, headers=headers, params={"maxRecords": 1})
        
        if response.status_code == 200:
            print("✅ Airtable connection successful")
            return True
        else:
            print(f"❌ Airtable connection failed: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Airtable connection failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🔧 Testing Airtable HR Sync Setup")
    print("=" * 40)
    
    tests = [
        ("Environment Variables", test_environment),
        ("Package Imports", test_imports),
        ("Supabase Connection", test_supabase_connection),
        ("Airtable Connection", test_airtable_connection)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        try:
            results.append(test_func())
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 40)
    print("📊 Test Summary:")
    
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"   {test_name}: {status}")
    
    if all(results):
        print("\n🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Start the server: uvicorn main:app --reload")
        print("2. Test manual sync: curl -X POST http://127.0.0.1:8000/sync -H 'x-sync-key: airtable-sync-secure-key-2024'")
        return 0
    else:
        print(f"\n⚠️  {sum(1 for r in results if not r)} test(s) failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())