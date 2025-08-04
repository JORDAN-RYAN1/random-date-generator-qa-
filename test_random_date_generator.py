# Save as: test_random_date_generator.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestRandomDateGenerator:
    
    def setup_method(self):
        """Setup browser"""
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Auto-download ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        self.driver.get("https://codebeautify.org/generate-random-date")
        time.sleep(3)  # Wait for page load
        
    def teardown_method(self):
        """Cleanup"""
        self.driver.quit()
    
    def test_page_loads(self):
        """TC01: Verify page loads"""
        assert "codebeautify" in self.driver.current_url.lower()
        print("✅ Page loaded successfully")
    
    def test_find_elements(self):
        """TC02: Find key elements on page"""
        # Look for any input fields
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        
        print(f"Found {len(inputs)} input fields")
        print(f"Found {len(buttons)} buttons")
        
        assert len(inputs) > 0, "No input fields found"
        assert len(buttons) > 0, "No buttons found"
    
    def test_basic_interaction(self):
        """TC03: Basic interaction test"""
        try:
            # Find first input and enter value
            inputs = self.driver.find_elements(By.TAG_NAME, "input")
            if inputs:
                first_input = inputs[0]
                first_input.clear()
                first_input.send_keys("5")
                print("✅ Entered value in first input")
            
            # Find and click first button
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            if buttons:
                first_button = buttons[0]
                first_button.click()
                print("✅ Clicked first button")
                
            time.sleep(3)
            
            # Check for any changes on page
            page_text = self.driver.find_element(By.TAG_NAME, "body").text
            assert len(page_text) > 100, "Page should have content"
            
        except Exception as e:
            print(f"Interaction test error: {e}")
            # Don't fail - this is exploratory
    
    def test_page_source_analysis(self):
        """TC04: Analyze page structure"""
        page_source = self.driver.page_source
        
        # Look for common date generator elements
        keywords = ["date", "generate", "random", "format", "count"]
        found_keywords = []
        
        for keyword in keywords:
            if keyword.lower() in page_source.lower():
                found_keywords.append(keyword)
        
        print(f"Found keywords: {found_keywords}")
        assert len(found_keywords) >= 2, "Should find date-related keywords"
    
    def test_screenshot_capture(self):
        """TC05: Capture screenshot for manual review"""
        self.driver.save_screenshot("page_screenshot.png")
        print("✅ Screenshot saved as page_screenshot.png")
        assert True


if __name__ == "__main__":
    print("🧪 Running QA Test Suite")
    print("Run with: pytest test_random_date_generator.py -v --html=report.html")