# Student Feedback Registration Form

A complete web form project with HTML, CSS, JavaScript validation, and Selenium automated testing.

## Project Structure
```
student-feedback/
├── index.html          # Main HTML form
├── style.css           # External CSS styling
├── script.js           # JavaScript validation
├── test/
│   └── test_form.py   # Selenium test suite
├── Jenkinsfile         # Jenkins CI/CD pipeline
└── README.md          # Documentation
```

## Features

### HTML Form Fields
- Name (text input)
- Email (email input)
- Mobile (10-digit number)
- Department (dropdown)
- Gender (radio buttons)
- Feedback (textarea)
- Submit and Reset buttons

### CSS Styling
- External CSS (style.css)
- Internal CSS (in index.html)
- Centered, responsive design
- Modern gradient background
- Clean UI with hover effects

### JavaScript Validation
- Name: Cannot be empty
- Email: Valid email format
- Mobile: Exactly 10 digits
- Department: Must be selected
- Gender: Must be selected
- Feedback: Minimum 10 words

### Selenium Tests
- Test valid form submission
- Test empty field validation
- Test invalid email format
- Test invalid mobile number

## Running the Project

### 1. Open the Form
Simply open `index.html` in a web browser:
```bash
# Windows
start index.html

# Linux/Mac
open index.html
```

### 2. Run Selenium Tests

#### Prerequisites
```bash
pip install selenium
```

#### Run Tests
```bash
cd student-feedback
python -m unittest test.test_form
```

#### Run with Verbose Output
```bash
python test/test_form.py -v
```

### 3. Jenkins Setup

#### Option A: Using Jenkinsfile
1. Create a new Pipeline job in Jenkins
2. Point to your repository
3. Jenkins will automatically use the Jenkinsfile

#### Option B: Manual Configuration
1. Create a new Freestyle project
2. Add build step: Execute shell
```bash
cd student-feedback
pip install selenium
python -m unittest test.test_form
```

#### Jenkins Prerequisites
- Python 3.x installed
- Chrome/Chromium browser
- Selenium Python package

## Test Results

All tests validate:
- ✓ Valid form submission shows success message
- ✓ Empty fields show appropriate error messages
- ✓ Invalid email format is rejected
- ✓ Invalid mobile number is rejected

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Edge
- Safari

## Notes
- Tests run in headless mode by default
- Form data is logged to console (not submitted to server)
- Success message appears for 2 seconds after valid submission
