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

    def tearDown(self):
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
            WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.assertIn("Login Sukses", alert.text)
            alert.accept()
        except Exception as e:
            print(f"Failed to find or handle login alert: {e}")

        # Wait for the home page to load after successful login
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='home']")))
        except Exception as e:
            print(f"Timeout waiting for home page: {e}")

    def test_transaksi(self):
        driver = self.driver
        self.login()  # Call login method to ensure the user is logged in

        driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=jual")

        try:
            # Wait for the page to load
            WebDriverWait(driver, 20).until(
                EC.title_contains("Kasir")  # Adjust this to the actual title or use an element on the page
            )
        except Exception as e:
            self.fail(f"Timeout waiting for home page to load: {e}")

        driver.find_element(By.ID, "cari_barang").send_keys("BR019")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Cari')]").click()

        try:
            # Wait for search results to appear
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//table[@id='example1']//tr[2]//td[contains(text(), 'BR019')]"))
            )
        except Exception as e:
            self.fail(f"Timeout waiting for search results: {e}")

        # Add scroll action to ensure the element is visible
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        driver.find_element(By.XPATH, "//button[contains(text(), 'Keranjang')]").click()

        try:
            # Wait for the item to appear in the cashier form
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//table[@id='example1']//tr[2]//td[contains(text(), 'BR019')]"))
            )
        except Exception as e:
            self.fail(f"Timeout waiting for item to be added to cashier form: {e}")

        kasir_item = driver.find_element(By.XPATH, "//table[@id='example1']//tr[2]//td[contains(text(), 'BR019')]")
        self.assertIsNotNone(kasir_item, "Item was not found in the cashier form")

        # Fill out the payment form
        try:
            payment_input = driver.find_element(By.ID, "bayar")  # Replace with the actual ID or locator of the payment input
            payment_input.send_keys("100000")  # Enter the payment amount
        except Exception as e:
            self.fail(f"Failed to find payment input field: {e}")

        try:
            submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")  # Replace with the actual locator of the submit button
            submit_button.click()
            print("Payment form submitted")
        except Exception as e:
            self.fail(f"Failed to find or click submit button: {e}")

        try:
            # Wait for the payment confirmation alert and handle it
            WebDriverWait(driver, 20).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"Alert text: {alert_text}")

            # Check if the alert text matches the expected value
            self.assertIn("Belanjaan Berhasil Di Bayar", alert_text)  # Update the expected text to match the actual alert message
        except Exception as e:
            self.fail(f"Timeout waiting for payment confirmation: {e}")

if __name__ == "__main__":
    unittest.main()
