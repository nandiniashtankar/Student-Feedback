# GitHub Webhook Setup with ngrok

This guide shows how to automatically trigger Jenkins builds when you push code to GitHub.

## Overview

```
GitHub Push → Webhook → ngrok → Jenkins (localhost:8090) → Run Tests
```

---

## Step 1: Install ngrok

### Download ngrok:
1. Go to: https://ngrok.com/download
2. Download for Windows
3. Extract `ngrok.exe` to a folder (e.g., `C:\ngrok\`)
4. (Optional) Add to PATH for easy access

### Sign up (Free):
1. Create account at: https://ngrok.com/signup
2. Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken
3. Run: `ngrok config add-authtoken YOUR_TOKEN`

---

## Step 2: Start ngrok Tunnel

### Open Command Prompt and run:
```cmd
ngrok http 8090
```

**Note:** Use port 8090 (your Jenkins port), not 8080!

### You'll see output like:
```
ngrok

Session Status                online
Account                       your-email@example.com
Version                       3.x.x
Region                        United States (us)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok.io -> http://localhost:8090

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

### Important:
- Copy your ngrok URL: `https://abc123.ngrok.io`
- Keep this terminal window open (ngrok must stay running)
- URL changes each time you restart ngrok (unless you have paid plan)

---

## Step 3: Configure Jenkins for GitHub Webhook

### 3.1 Install GitHub Plugin (if not installed)
1. Jenkins → Manage Jenkins → Manage Plugins
2. Go to "Available" tab
3. Search for "GitHub Plugin"
4. Install and restart Jenkins

### 3.2 Configure Jenkins Project
1. Open your project: http://localhost:8090/job/student-feedback-test/configure
2. Scroll to **"Build Triggers"** section
3. Check: ☑ **"GitHub hook trigger for GITScm polling"**
4. Click **"Save"**

### 3.3 Configure Source Code Management (Important!)
Since you're using local files, we need to change to Git:

1. In project configuration, go to **"Source Code Management"**
2. Select: **Git**
3. Repository URL: `https://github.com/mrudangwanjari/student-feedback.git`
4. Credentials: (add your GitHub credentials if private repo)
5. Branch Specifier: `*/main`
6. Click **"Save"**

---

## Step 4: Configure GitHub Webhook

### 4.1 Go to Your GitHub Repository
Open: https://github.com/mrudangwanjari/student-feedback

### 4.2 Add Webhook
1. Click **"Settings"** tab
2. Click **"Webhooks"** in left sidebar
3. Click **"Add webhook"** button

### 4.3 Configure Webhook Settings

**Payload URL:**
```
https://abc123.ngrok.io/github-webhook/
```
⚠️ Replace `abc123.ngrok.io` with YOUR ngrok URL
⚠️ Don't forget the trailing slash `/`

**Content type:**
- Select: `application/json`

**Secret:**
- Leave empty (or add for security)

**Which events would you like to trigger this webhook?**
- Select: ☑ **"Just the push event"**

**Active:**
- Check: ☑ **Active**

Click **"Add webhook"**

### 4.4 Verify Webhook
- GitHub will send a test ping
- You should see a green checkmark ✓ if successful
- Click on the webhook to see delivery details

---

## Step 5: Test the Setup

### 5.1 Make a Code Change
```cmd
cd "C:\Users\MRUDANG WANJARI\DevOps_website\Student-Feedback\student-feedback"

REM Make a small change
echo. >> README.md

REM Commit and push
git add .
git commit -m "Test webhook trigger"
git push origin main
```

### 5.2 Watch Jenkins
1. Go to Jenkins: http://localhost:8090/job/student-feedback-test/
2. You should see a new build start automatically!
3. Check "Console Output" to see the build log

### 5.3 Check ngrok Dashboard
- Open: http://127.0.0.1:4040
- See all HTTP requests from GitHub to Jenkins
- Useful for debugging

---

## Step 6: Keep ngrok Running

### Option A: Manual (for testing)
- Keep Command Prompt window open with ngrok running
- Restart when needed

### Option B: Background Service (recommended)
Create `start_ngrok.bat`:
```batch
@echo off
start "ngrok" ngrok http 8090
echo ngrok started in background
echo Check dashboard: http://127.0.0.1:4040
pause
```

### Option C: ngrok as Windows Service (advanced)
Use NSSM (Non-Sucking Service Manager):
1. Download NSSM: https://nssm.cc/download
2. Install ngrok as service:
```cmd
nssm install ngrok "C:\path\to\ngrok.exe" "http 8090"
nssm start ngrok
```

---

## Troubleshooting

### Issue 1: Webhook shows error in GitHub
**Symptoms:** Red X next to webhook, "Connection refused"

**Solutions:**
- Check ngrok is running: `ngrok http 8090`
- Verify ngrok URL is correct in webhook settings
- Check Jenkins is running: http://localhost:8090
- Ensure URL ends with `/github-webhook/`

### Issue 2: Jenkins doesn't trigger
**Symptoms:** Webhook delivers successfully but Jenkins doesn't build

**Solutions:**
- Verify "GitHub hook trigger" is enabled in Jenkins project
- Check Jenkins has GitHub plugin installed
- Ensure project is configured to use Git (not local files)
- Check Jenkins logs: Manage Jenkins → System Log

### Issue 3: ngrok URL changes
**Symptoms:** Webhook stops working after restarting ngrok

**Solutions:**
- Free ngrok URLs change on restart
- Update GitHub webhook with new URL
- Or upgrade to ngrok paid plan for static URL

### Issue 4: Authentication errors
**Symptoms:** Jenkins can't clone from GitHub

**Solutions:**
- Add GitHub credentials in Jenkins
- Use Personal Access Token instead of password
- Generate token: GitHub → Settings → Developer settings → Personal access tokens

### Issue 5: Build fails with "repository not found"
**Symptoms:** Jenkins can't find Git repository

**Solutions:**
- Verify repository URL is correct
- Check repository is public or credentials are added
- Test Git clone manually:
```cmd
git clone https://github.com/mrudangwanjari/student-feedback.git test-clone
```

---

## Workflow Summary

### Every time you push to GitHub:

1. **You push code:**
   ```cmd
   git add .
   git commit -m "Update form"
   git push origin main
   ```

2. **GitHub sends webhook:**
   - POST request to `https://abc123.ngrok.io/github-webhook/`

3. **ngrok forwards to Jenkins:**
   - `https://abc123.ngrok.io` → `http://localhost:8090`

4. **Jenkins receives webhook:**
   - Pulls latest code from GitHub
   - Runs build script
   - Executes Selenium tests

5. **You see results:**
   - Build status in Jenkins dashboard
   - Blue = Success, Red = Failure

---

## Security Best Practices

### 1. Use Webhook Secret
In GitHub webhook settings:
- Add a secret token
- Configure same secret in Jenkins

### 2. Restrict ngrok Access
```cmd
ngrok http 8090 --basic-auth="username:password"
```

### 3. Use GitHub Personal Access Token
Instead of password:
- GitHub → Settings → Developer settings
- Generate token with `repo` scope
- Use in Jenkins credentials

---

## Quick Reference

### Start ngrok:
```cmd
ngrok http 8090
```

### Check ngrok dashboard:
```
http://127.0.0.1:4040
```

### Jenkins webhook URL format:
```
https://YOUR-NGROK-URL.ngrok.io/github-webhook/
```

### Test webhook manually:
```cmd
curl -X POST https://abc123.ngrok.io/github-webhook/
```

---

## Alternative: Polling Instead of Webhooks

If webhooks are too complex, use polling:

1. Jenkins project → Configure
2. Build Triggers → Check "Poll SCM"
3. Schedule: `H/5 * * * *` (check every 5 minutes)
4. Save

Jenkins will check GitHub every 5 minutes for changes.

---

## Next Steps

1. ✓ Install and start ngrok
2. ✓ Configure Jenkins for Git + webhook trigger
3. ✓ Add webhook in GitHub with ngrok URL
4. ✓ Test by pushing code
5. ✓ Watch automatic builds!

**Your CI/CD pipeline is now complete!** 🎉
