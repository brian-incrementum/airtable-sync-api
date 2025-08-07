# Railway Deployment Guide - Airtable Sync API

## Pre-Deployment Checklist

###  Required Files (Already Created)
- [x] `Procfile` - Defines how to start the application
- [x] `railway.json` - Railway-specific configuration
- [x] `requirements.txt` - Python dependencies
- [x] `.gitignore` - Excludes .env and venv/
- [x] Updated `main.py` - Uses dynamic PORT from environment

### =' Configuration Files Explained

#### Procfile
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```
- Railway will use this to start your app
- `$PORT` is automatically provided by Railway
- Alternative to railway.json (use one or the other)

#### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 3
  }
}
```
- More control over deployment settings
- Includes restart policy for reliability
- Takes precedence over Procfile if both exist

## =€ Deployment Steps (Web Interface)

### Step 1: Prepare GitHub Repository
1. Commit all changes:
   ```bash
   git add .
   git commit -m "Add Railway deployment configuration"
   git push origin main
   ```

2. Verify `.gitignore` includes:
   - `.env`
   - `venv/`
   - `__pycache__/`

### Step 2: Create Railway Project
1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Authorize Railway to access your GitHub
5. Select your `airtable-sync-api` repository
6. Railway will auto-detect Python and start initial deployment (will fail without env vars)

### Step 3: Configure Environment Variables
Click on your service card, then go to "Variables" tab and add:

```bash
SUPABASE_URL=https://xyihdxjlbtifnjimaehl.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
AIRTABLE_API_KEY=your_airtable_api_key_here
AIRTABLE_BASE_ID=your_airtable_base_id_here
SYNC_KEY=your_secure_sync_key_here
```

**Important:** 
- Add all variables BEFORE the first successful deployment
- Railway will automatically redeploy when you add/change variables
- Never commit these values to GitHub

### Step 4: Deploy
1. After adding environment variables, Railway will automatically redeploy
2. Watch the build logs for any errors
3. Once deployed, Railway will provide a URL like: `your-app.railway.app`

### Step 5: Verify Deployment
Test your endpoints:

```bash
# Health check
curl https://your-app.railway.app/

# HR Sync endpoints
curl https://your-app.railway.app/hr/cron
curl -X POST https://your-app.railway.app/hr/sync \
  -H "x-sync-key: your_sync_key_here"

# Client Sync endpoints  
curl https://your-app.railway.app/client/cron
curl -X POST https://your-app.railway.app/client/sync \
  -H "x-sync-key: your_sync_key_here"
```

## =Å Setting Up Scheduled Syncs

### Option 1: Railway Cron (Recommended)
1. In Railway dashboard, go to your service
2. Click "Settings" ’ "Cron"
3. Add cron schedules:
   - HR Hourly: `0 * * * *` ’ GET `/hr/cron`
   - Client Hourly: `30 * * * *` ’ GET `/client/cron`

### Option 2: External Cron Service
Use services like:
- cron-job.org
- EasyCron
- UptimeRobot (with webhook)

Point them to:
- `https://your-app.railway.app/hr/cron`
- `https://your-app.railway.app/client/cron`

## = Monitoring & Logs

### View Logs
1. In Railway dashboard, click on your service
2. Go to "Deployments" tab
3. Click on any deployment to view logs

### Useful Log Commands (if using Railway CLI)
```bash
railway logs --tail
railway logs --last 100
```

## =¨ Common Issues & Solutions

### Issue 1: "Application failed to respond"
**Cause:** Not binding to correct PORT
**Solution:** Ensure main.py uses `os.getenv("PORT", 8000)`

### Issue 2: "Module not found" errors
**Cause:** Missing dependencies
**Solution:** Verify all imports are in requirements.txt

### Issue 3: "Connection refused" to Supabase
**Cause:** Missing or incorrect environment variables
**Solution:** Double-check SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY

### Issue 4: 401 Unauthorized on manual sync
**Cause:** Missing or incorrect SYNC_KEY
**Solution:** Verify x-sync-key header matches SYNC_KEY env variable

### Issue 5: Build fails with "No start command found"
**Cause:** Missing Procfile or railway.json
**Solution:** Ensure Procfile exists in root directory

### Issue 6: App crashes immediately after starting
**Cause:** Import errors or missing env vars at startup
**Solution:** Check deployment logs for specific error

## = Updating Your Deployment

1. Make changes locally
2. Test thoroughly
3. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update description"
   git push origin main
   ```
4. Railway auto-deploys from main branch

## =á Security Best Practices

1. **Never commit secrets** - Use environment variables
2. **Use strong SYNC_KEY** - Generate with: `openssl rand -hex 32`
3. **Rotate API keys regularly**
4. **Monitor logs** for unauthorized access attempts
5. **Use Supabase RLS** for additional database security

## =Ê Performance Tips

1. **Use incremental sync** by default (already configured)
2. **Monitor response times** in Railway metrics
3. **Set up alerts** for failed syncs
4. **Review Supabase usage** to optimize queries

## <˜ Rollback Procedure

If deployment fails:
1. Go to Railway dashboard
2. Click "Deployments"
3. Find last working deployment
4. Click "..." menu ’ "Rollback to this deployment"

## =Ý Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| SUPABASE_URL | Your Supabase project URL | https://abc.supabase.co |
| SUPABASE_SERVICE_ROLE_KEY | Service role key (full access) | eyJhbGc... |
| AIRTABLE_API_KEY | Personal access token | patXXXXX... |
| AIRTABLE_BASE_ID | Base identifier | appXXXXX... |
| SYNC_KEY | Authentication for manual sync | any-secure-string |
| PORT | (Auto-provided by Railway) | 3000 |

##  Final Checklist

Before considering deployment complete:
- [ ] All endpoints respond correctly
- [ ] Manual sync works with authentication
- [ ] Cron endpoints accessible
- [ ] Logs show successful syncs
- [ ] Set up scheduled syncs
- [ ] Document Railway URL for team
- [ ] Test rollback procedure
- [ ] Monitor first automated sync

## =Ú Additional Resources

- [Railway Documentation](https://docs.railway.app)
- [Railway Status Page](https://status.railway.app)
- [Nixpacks Documentation](https://nixpacks.com/docs)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)

---

**Last Updated:** August 2024
**Deployment Platform:** Railway
**Framework:** FastAPI with Uvicorn