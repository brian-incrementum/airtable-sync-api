#!/usr/bin/env python3
"""
Command-line utility for running Airtable sync manually.

Usage:
    python3 run_sync.py           # Run incremental sync (default)
    python3 run_sync.py --full     # Run full sync
    python3 run_sync.py --mode full   # Alternative syntax
    python3 run_sync.py --mode incremental  # Explicit incremental
"""

import argparse
from sync import run_sync


def main():
    parser = argparse.ArgumentParser(
        description='Run Airtable to Supabase sync',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 run_sync.py           # Incremental sync (only modified records)
  python3 run_sync.py --full     # Full sync (all records)
  python3 run_sync.py --mode full   # Alternative syntax for full sync
        """
    )
    
    parser.add_argument(
        '--full',
        action='store_true',
        help='Run a full sync instead of incremental'
    )
    
    parser.add_argument(
        '--mode',
        choices=['full', 'incremental'],
        default='incremental',
        help='Sync mode: full or incremental (default: incremental)'
    )
    
    args = parser.parse_args()
    
    # Determine sync mode
    if args.full:
        sync_mode = 'full'
    else:
        sync_mode = args.mode
    
    print(f"Running {sync_mode} sync...")
    print("-" * 50)
    
    # Run the sync
    result = run_sync(sync_mode=sync_mode)
    
    # Print summary
    print("-" * 50)
    print(f"Sync completed!")
    print(f"  Mode: {result.get('sync_mode', sync_mode)}")
    print(f"  Departments: {result.get('departments', 0)} records")
    print(f"  Positions: {result.get('positions', 0)} records")
    print(f"  Team Members: {result.get('team_members', 0)} records")
    
    if result.get('fallback_reason'):
        print(f"  Note: {result['fallback_reason']}")


if __name__ == "__main__":
    main()