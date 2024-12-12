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

    def test_edit_profile_and_change_password(self):
        self.login()

        # Navigate to user profile page
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=user")

        # Wait for profile form to load
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "nama")))
        except Exception as e:
            print(f"Failed to load profile form: {e}")
            return

        # Edit profile information
        new_nama = "Pedro Pede"
        new_email = "pede@gmail.com"
        new_tlp = "081234567892"
        new_nik = "123456789"
        new_alamat = "Jl. Kebon Jeruk No. 12"

        try:
            nama_input = self.driver.find_element(By.NAME, "nama")
            nama_input.clear()
            nama_input.send_keys(new_nama)

            email_input = self.driver.find_element(By.NAME, "email")
            email_input.clear()
            email_input.send_keys(new_email)

            tlp_input = self.driver.find_element(By.NAME, "tlp")
            tlp_input.clear()
            tlp_input.send_keys(new_tlp)

            nik_input = self.driver.find_element(By.NAME, "nik")
            nik_input.clear()
            nik_input.send_keys(new_nik)

            alamat_input = self.driver.find_element(By.NAME, "alamat")
            alamat_input.clear()
            alamat_input.send_keys(new_alamat)
        except Exception as e:
            print(f"Failed to fill profile form: {e}")
            return

        # Click the "Ubah Profil" button
        try:
            ubah_profil_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary') and contains(text(), 'Ubah Profil')]"))
            )
            ubah_profil_button.click()
        except Exception as e:
            print(f"Failed to click the 'Ubah Profil' button: {e}")
            return

        # Wait for success message
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']/p[contains(text(), 'Edit Data Berhasil')]")))
            success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success']/p[contains(text(), 'Edit Data Berhasil')]")
            self.assertTrue(success_message.is_displayed(), "Success message not displayed after profile edit")
        except Exception as e:
            print(f"Failed to find success message: {e}")
            return

        # Ensure profile update is complete before proceeding to password change
        time.sleep(2)  # Add a short delay to ensure page updates

        # Wait for change password form to load
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "pass")))
        except Exception as e:
            print(f"Failed to load change password form: {e}")
            return

        # Fill in the change password form
        try:
            username_input = self.driver.find_element(By.NAME, "user")
            pass_baru_input = self.driver.find_element(By.NAME, "pass")
            username_input.clear()
            username_input.send_keys("admin")
            pass_baru_input.clear()
            pass_baru_input.send_keys("admin")
        except Exception as e:
            print(f"Failed to fill password form: {e}")
            return

        # Click the "Ubah Password" button
        try:
            ubah_password_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary') and contains(text(), 'Ubah Password')]"))
            )
            ubah_password_button.click()
        except Exception as e:
            print(f"Failed to click the 'Ubah Password' button: {e}")
            return

        # Wait for success message
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']/p[contains(text(), 'Password Berhasil Diubah')]")))
            success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success']/p[contains(text(), 'Password Berhasil Diubah')]")
            self.assertTrue(success_message.is_displayed(), "Success message not displayed after password change")
        except Exception as e:
            print(f"Failed to find success message: {e}")
            return

if __name__ == "__main__":
    unittest.main()
