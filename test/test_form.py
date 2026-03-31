"""
Selenium Test Suite for Student Feedback Form
"""
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestStudentFeedbackForm(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up Chrome driver"""
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # Disabled for visible browser
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--start-maximized')
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        
        # Get the absolute path to index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, '..', 'index.html')
        cls.form_url = f'file:///{os.path.abspath(html_path)}'
    
    def setUp(self):
        """Navigate to form before each test"""
        self.driver.get(self.form_url)
        time.sleep(0.5)
    
    def test_valid_submission(self):
        """Test valid form submission"""
        driver = self.driver
        
        # Fill in valid data
        driver.find_element(By.ID, 'name').send_keys('John Doe')
        driver.find_element(By.ID, 'email').send_keys('john.doe@example.com')
        driver.find_element(By.ID, 'mobile').send_keys('9876543210')
        
        # Select department
        department = Select(driver.find_element(By.ID, 'department'))
        department.select_by_visible_text('Computer Science')
        
        # Select gender
        driver.find_element(By.CSS_SELECTOR, 'input[value="Male"]').click()
        
        # Fill feedback
        feedback_text = 'This is an excellent course with great content and wonderful instructors who are very helpful'
        driver.find_element(By.ID, 'feedback').send_keys(feedback_text)
        
        # Submit form
        driver.find_element(By.CSS_SELECTOR, '.btn-submit').click()
        time.sleep(1)
        
        # Check for success message
        success_msg = driver.find_element(By.ID, 'successMessage')
        self.assertTrue(success_msg.is_displayed(), 'Success message should be displayed')
    
    def test_empty_fields(self):
        """Test form submission with empty fields"""
        driver = self.driver
        
        # Submit without filling any fields
        driver.find_element(By.CSS_SELECTOR, '.btn-submit').click()
        time.sleep(0.5)
        
        # Check that error messages are displayed
        name_error = driver.find_element(By.ID, 'nameError')
        email_error = driver.find_element(By.ID, 'emailError')
        mobile_error = driver.find_element(By.ID, 'mobileError')
        department_error = driver.find_element(By.ID, 'departmentError')
        gender_error = driver.find_element(By.ID, 'genderError')
        feedback_error = driver.find_element(By.ID, 'feedbackError')
        
        self.assertTrue(name_error.is_displayed(), 'Name error should be displayed')
        self.assertTrue(email_error.is_displayed(), 'Email error should be displayed')
        self.assertTrue(mobile_error.is_displayed(), 'Mobile error should be displayed')
        self.assertTrue(department_error.is_displayed(), 'Department error should be displayed')
        self.assertTrue(gender_error.is_displayed(), 'Gender error should be displayed')
        self.assertTrue(feedback_error.is_displayed(), 'Feedback error should be displayed')
    
    def test_invalid_email(self):
        """Test form submission with invalid email"""
        driver = self.driver
        
        # Fill form with invalid email
        driver.find_element(By.ID, 'name').send_keys('John Doe')
        driver.find_element(By.ID, 'email').send_keys('invalid-email')
        driver.find_element(By.ID, 'mobile').send_keys('9876543210')
        
        department = Select(driver.find_element(By.ID, 'department'))
        department.select_by_visible_text('Computer Science')
        
        driver.find_element(By.CSS_SELECTOR, 'input[value="Male"]').click()
        driver.find_element(By.ID, 'feedback').send_keys('This is an excellent course with great content and wonderful instructors')
        
        # Submit form
        driver.find_element(By.CSS_SELECTOR, '.btn-submit').click()
        time.sleep(0.5)
        
        # Check that email error is displayed
        email_error = driver.find_element(By.ID, 'emailError')
        self.assertTrue(email_error.is_displayed(), 'Email error should be displayed for invalid email')
    
    def test_invalid_mobile(self):
        """Test form submission with invalid mobile number"""
        driver = self.driver
        
        # Test with less than 10 digits
        driver.find_element(By.ID, 'name').send_keys('John Doe')
        driver.find_element(By.ID, 'email').send_keys('john.doe@example.com')
        driver.find_element(By.ID, 'mobile').send_keys('12345')
        
        department = Select(driver.find_element(By.ID, 'department'))
        department.select_by_visible_text('Computer Science')
        
        driver.find_element(By.CSS_SELECTOR, 'input[value="Male"]').click()
        driver.find_element(By.ID, 'feedback').send_keys('This is an excellent course with great content and wonderful instructors')
        
        # Submit form
        driver.find_element(By.CSS_SELECTOR, '.btn-submit').click()
        time.sleep(0.5)
        
        # Check that mobile error is displayed
        mobile_error = driver.find_element(By.ID, 'mobileError')
        self.assertTrue(mobile_error.is_displayed(), 'Mobile error should be displayed for invalid mobile')
    
    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests"""
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
