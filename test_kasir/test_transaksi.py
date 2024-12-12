import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='home']")))
        except TimeoutException as e:
            print(f"Timeout waiting for home page: {e}")

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Optional: Wait for 1 second after scrolling

    def test_transaksi(self):
        self.login()
        driver = self.driver

        # Navigate to the transaksi page
        driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=jual")

        # Search for a product
        search_box = driver.find_element(By.ID, "cari")
        product_code = "BR019"  # Replace with the actual product code or name
        
        for char in product_code:
            search_box.send_keys(char)
            time.sleep(0.2)  # Wait for 200 milliseconds between each keystroke

        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "hasil_cari"))
            )
            print("Search results are visible")
        except TimeoutException as e:
            print(f"Timeout waiting for search results: {e}")
            self.fail("Search results did not load in time")

        # Click the "keranjang" button for the first search result
        try:
            keranjang_button = driver.find_element(By.XPATH, "//div[@id='hasil_cari']//tr[2]//a[contains(@href, 'jual=jual')]")
            keranjang_button.click()
            print("Keranjang button clicked")
        except NoSuchElementException as e:
            print(f"Keranjang button not found: {e}")
            self.fail("Keranjang button not found")

        # Wait for the item to be added to the cashier form
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//table[@id='example1']//tr[2]"))
            )
            print("Item added to cashier form")
        except TimeoutException as e:
            print(f"Timeout waiting for item to be added to cashier form: {e}")
            self.fail("Item was not added to the cashier form in time")

        bayar_input = driver.find_element(By.NAME, "bayar")
        driver.execute_script("arguments[0].scrollIntoView(true);", bayar_input)
        time.sleep(1)  # Tunggu sebentar setelah scroll

        bayar_input.clear()
        desired_payment = 100000  # Input jumlah pembayaran yang diinginkan
        bayar_input.send_keys(desired_payment)
        print(f"Entered payment amount: {desired_payment}")

        bayar_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-success') and contains(., 'Bayar')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", bayar_button)
        bayar_button.click()
        print("Payment form submitted")

        # Wait for the alert and handle it
        try:
            WebDriverWait(driver, 20).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            self.assertIn("Belanjaan Berhasil Di Bayar", alert.text)
            alert.accept()
            print("Alert accepted")
        except TimeoutException as e:
            print(f"Timeout waiting for payment alert: {e}")
            self.fail("Payment alert did not appear in time")

        # Wait for the form to be updated and verify that the kembali (change) field is auto-filled
        time.sleep(2)  # Wait to ensure that the form has time to update

        try:
            kembali_input = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='kembali']"))
            )
            kembali_amount = kembali_input.get_attribute("value")
            self.assertNotEqual(kembali_amount, "", "Kembali amount should not be empty after payment")
            print(f"Kembali amount: {kembali_amount}")
        except TimeoutException as e:
            print(f"Timeout waiting for kembali amount: {e}")
            self.fail("Kembali amount did not appear in time")

        # Click the "Print Bukti Pembayaran" button
        try:
            print_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Print Untuk Bukti Pembayaran')]"))
            )
            print_button.click()
            print("Print Bukti Pembayaran button clicked")
        except TimeoutException as e:
            print(f"Timeout waiting for print button: {e}")
            self.fail("Print Bukti Pembayaran button did not appear in time")

        # Optional: Additional verification that print dialog or PDF opened (depends on your application and environment)

if __name__ == "__main__":
    unittest.main()
