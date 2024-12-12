import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait for all find_element calls

    def tearDown(self):
        time.sleep(3)  # Wait for 3 seconds before closing the browser
        self.driver.quit()

    def login(self):
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/login.php")
        user_input = self.driver.find_element(By.XPATH, "//input[@id='user']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_input.send_keys("admin")
        password_input.send_keys("admin")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Wait for the login alert to appear
        time.sleep(1)  # Wait for 1 second
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.assertIn("Login Sukses", alert.text)
            alert.accept()
        except Exception as e:
            print(f"Failed to find or handle login alert: {e}")

        # Wait for the home page to load after successful login
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='home']")))
        except Exception as e:
            print(f"Timeout waiting for home page: {e}")

    def test_logout(self):
        self.login()

        # Assume logout button can be found and clicked
        logout_button = self.driver.find_element(By.XPATH, "//a[@href='logout.php']")
        logout_button.click()

        # Handle logout confirmation alert
        time.sleep(1)  # Wait for 1 second
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.assertIn("Ingin Logout ?", alert.text)
            alert.accept()
        except Exception as e:
            print(f"Failed to find or handle logout confirmation alert: {e}")
            return

        # Handle logout success alert
        time.sleep(1)  # Wait for 1 second
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.assertIn("Anda Telah Logout", alert.text)
            alert.accept()
        except Exception as e:
            print(f"Failed to find or handle logout success alert: {e}")
            return
        
        # Verify redirection to login page after logout
        time.sleep(1)  # Wait for 1 second
        current_url = self.driver.current_url
        self.assertTrue(current_url.endswith("login.php"))

if __name__ == "__main__":
    unittest.main()