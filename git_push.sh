#!/bin/bash
# Git push script for student-feedback project

echo "========================================="
echo "Pushing Student Feedback to GitHub"
echo "========================================="
echo ""

# Navigate to project directory
cd "$(dirname "$0")"

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
    echo ""
fi

# Add all files
echo "Adding all files..."
git add .
echo ""

# Commit
echo "Creating commit..."
git commit -m "Initial commit: Student Feedback Form with Selenium tests"
echo ""

# Rename branch to main
echo "Setting branch to main..."
git branch -M main
echo ""

# Add remote origin
echo "Adding remote origin..."
git remote add origin https://github.com/mrudangwanjari/student-feedback.git 2>/dev/null || git remote set-url origin https://github.com/mrudangwanjari/student-feedback.git
echo ""

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main
echo ""

echo "========================================="
echo "Done! Check: https://github.com/mrudangwanjari/student-feedback"
echo "========================================="
