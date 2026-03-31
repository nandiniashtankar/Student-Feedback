# Jenkins Setup Guide - Windows Freestyle Project

## Complete Step-by-Step Configuration

### Prerequisites Checklist
- ✓ Python installed (command: `python`)
- ✓ Chrome browser installed
- ✓ Jenkins running as Windows service at localhost:8090
- ✓ Project path: `C:\Users\MRUDANG WANJARI\DevOps_website\Student-Feedback\student-feedback`

---

## Step 1: Install Selenium on Jenkins Machine

Open Command Prompt as Administrator and run:
```cmd
python -m pip install --upgrade pip
pip install selenium
```

Verify installation:
```cmd
python -c "import selenium; print(selenium.__version__)"
```

---

## Step 2: Create Freestyle Project in Jenkins

1. Open Jenkins: http://localhost:8090
2. Click **"New Item"**
3. Enter name: `student-feedback-test`
4. Select: **Freestyle project**
5. Click **OK**

---

## Step 3: Configure General Settings

In the project configuration page:

### General Section
- **Description**: `Automated testing for Student Feedback Form`
- Leave other options as default

---

## Step 4: Configure Source Code Management

### Option A: No SCM (Recommended for local testing)
- Select: **None**
- Jenkins will use the local filesystem path directly

### Option B: If you want to use Git later
- Select: **Git**
- Repository URL: (your git repo URL)
- Credentials: (add if needed)
- Branch: `*/main` or `*/master`

---

## Step 5: Configure Build Triggers

- **Uncheck all options** (Manual trigger only)
- You'll click "Build Now" to run tests manually

---

## Step 6: Configure Build Environment

- Leave all options unchecked for now
- (Optional) Check "Delete workspace before build starts" for clean runs

---

## Step 7: Configure Build Steps

Click **"Add build step"** → Select **"Execute Windows batch command"**

### Build Script (Copy this exactly):

```batch
@echo off
echo ========================================
echo Student Feedback Form - Selenium Tests
echo ========================================
echo.

REM Change to project directory
cd /d "C:\Users\MRUDANG WANJARI\DevOps_website\Student-Feedback\student-feedback"

echo Current Directory: %CD%
echo.

REM Check if Python is available
echo Checking Python installation...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH
    exit /b 1
)
echo.

REM Check if Selenium is installed
echo Checking Selenium installation...
python -c "import selenium; print('Selenium version:', selenium.__version__)"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Selenium is not installed
    echo Installing Selenium...
    pip install selenium
)
echo.

REM Run the tests
echo Running Selenium tests...
echo.
python test/test_form.py

REM Capture exit code
set TEST_EXIT_CODE=%ERRORLEVEL%

echo.
echo ========================================
if %TEST_EXIT_CODE% EQU 0 (
    echo TESTS PASSED SUCCESSFULLY!
    echo ========================================
    exit /b 0
) else (
    echo TESTS FAILED!
    echo ========================================
    exit /b 1
)
```

---

## Step 8: Configure Post-Build Actions

### Option 1: No Post-Build Actions (Current Setup)
- Leave empty - build will simply pass/fail based on test results

### Option 2: Add Email Notification (If needed later)
- Click "Add post-build action" → "Email Notification"
- Enter recipient email addresses

---

## Step 9: Save Configuration

Click **"Save"** at the bottom of the page

---

## Step 10: Run Your First Build

1. Click **"Build Now"** in the left sidebar
2. Watch the build appear in "Build History"
3. Click on the build number (e.g., #1)
4. Click **"Console Output"** to see live logs
5. Chrome browser will open and run the tests visibly

---

## Expected Console Output

```
Started by user admin
Running as SYSTEM
Building in workspace C:\Users\MRUDANG WANJARI\.jenkins\workspace\student-feedback-test
========================================
Student Feedback Form - Selenium Tests
========================================

Current Directory: C:\Users\MRUDANG WANJARI\DevOps_website\Student-Feedback\student-feedback

Checking Python installation...
Python 3.x.x

Checking Selenium installation...
Selenium version: 4.x.x

Running Selenium tests...

test_empty_fields (test.test_form.TestStudentFeedbackForm) ... ok
test_invalid_email (test.test_form.TestStudentFeedbackForm) ... ok
test_invalid_mobile (test.test_form.TestStudentFeedbackForm) ... ok
test_valid_submission (test.test_form.TestStudentFeedbackForm) ... ok

----------------------------------------------------------------------
Ran 4 tests in 15.234s

OK

========================================
TESTS PASSED SUCCESSFULLY!
========================================
Finished: SUCCESS
```

---

## Troubleshooting

### Issue 1: Python not found
**Error**: `'python' is not recognized as an internal or external command`

**Solution**:
1. Find Python installation path (e.g., `C:\Python39\python.exe`)
2. In Jenkins: Manage Jenkins → Global Tool Configuration → Add Python
3. Or add Python to Windows PATH environment variable

### Issue 2: Selenium not found
**Error**: `ModuleNotFoundError: No module named 'selenium'`

**Solution**:
```cmd
pip install selenium
```

### Issue 3: ChromeDriver not found
**Error**: `selenium.common.exceptions.WebDriverException: 'chromedriver' executable needs to be in PATH`

**Solution**:
- Selenium 4.x automatically manages ChromeDriver
- Ensure Chrome browser is installed
- Update Selenium: `pip install --upgrade selenium`

### Issue 4: Permission denied
**Error**: `Access is denied`

**Solution**:
- Run Jenkins as Administrator
- Or grant Jenkins service account permissions to the project folder

### Issue 5: Tests fail but should pass
**Solution**:
- Check if Chrome browser opens during test
- Verify index.html path is correct
- Run tests manually first: `python test/test_form.py`

---

## Quick Test Commands (Run in CMD)

### Test Python:
```cmd
python --version
```

### Test Selenium:
```cmd
python -c "import selenium; print(selenium.__version__)"
```

### Run tests manually:
```cmd
cd "C:\Users\MRUDANG WANJARI\DevOps_website\Student-Feedback\student-feedback"
python -m unittest test.test_form -v
```

---

## Jenkins Project Structure

```
Jenkins Workspace:
C:\Users\MRUDANG WANJARI\.jenkins\workspace\student-feedback-test\
(Jenkins will create this automatically)

Your Project:
C:\Users\MRUDANG WANJARI\DevOps_website\Student-Feedback\student-feedback\
├── index.html
├── style.css
├── script.js
└── test\
    └── test_form.py
```

---

## Build Status

- **Blue ball** = Success (all tests passed)
- **Red ball** = Failure (one or more tests failed)
- **Gray ball** = Not built yet or aborted

---

## Next Steps

1. ✓ Create the freestyle project
2. ✓ Configure the build script
3. ✓ Click "Build Now"
4. ✓ Watch tests run in Chrome browser
5. ✓ Check Console Output for results

**Your Jenkins is now configured to run Selenium tests on every manual build!**
