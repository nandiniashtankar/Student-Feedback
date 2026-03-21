// JavaScript Validation
document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Clear previous errors
    clearErrors();
    
    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const mobile = document.getElementById('mobile').value.trim();
    const department = document.getElementById('department').value;
    const gender = document.querySelector('input[name="gender"]:checked');
    const feedback = document.getElementById('feedback').value.trim();
    
    let isValid = true;
    
    // Validate Name
    if (name === '') {
        showError('nameError');
        isValid = false;
    }
    
    // Validate Email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError('emailError');
        isValid = false;
    }
    
    // Validate Mobile (exactly 10 digits)
    const mobileRegex = /^\d{10}$/;
    if (!mobileRegex.test(mobile)) {
        showError('mobileError');
        isValid = false;
    }
    
    // Validate Department
    if (department === '') {
        showError('departmentError');
        isValid = false;
    }
    
    // Validate Gender
    if (!gender) {
        showError('genderError');
        isValid = false;
    }
    
    // Validate Feedback (minimum 10 words)
    const wordCount = feedback.split(/\s+/).filter(word => word.length > 0).length;
    if (wordCount < 10) {
        showError('feedbackError');
        isValid = false;
    }
    
    // If all validations pass
    if (isValid) {
        document.getElementById('successMessage').style.display = 'block';
        console.log('Form Data:', {
            name,
            email,
            mobile,
            department,
            gender: gender.value,
            feedback
        });
        
        // Reset form after 2 seconds
        setTimeout(() => {
            document.getElementById('feedbackForm').reset();
            document.getElementById('successMessage').style.display = 'none';
        }, 2000);
    }
});

// Reset button handler
document.querySelector('.btn-reset').addEventListener('click', function() {
    clearErrors();
    document.getElementById('successMessage').style.display = 'none';
});

function showError(errorId) {
    document.getElementById(errorId).style.display = 'block';
}

function clearErrors() {
    const errors = document.querySelectorAll('.error');
    errors.forEach(error => error.style.display = 'none');
}
