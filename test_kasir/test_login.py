import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def login(self, user, password):
        # Membuka halaman login
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/login.php")

        # Mencari elemen input user dan password menggunakan XPath
        user_input = self.driver.find_element(By.XPATH, "//input[@id='user']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")

        # Memasukkan nama pengguna dan kata sandi
        user_input.send_keys(user)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Tunggu hingga muncul alert
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.assertIn("login sukses", alert_text.lower())
        alert.accept()

        # Tambahkan penundaan sebelum pindah ke halaman dashboard
        time.sleep(5)

    def home(self):
        # Membuka halaman dashboard
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php")

    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("admin", "admin")

        # Jalankan pengujian halaman utama
        self.home()

if __name__ == "__main__": 
    unittest.main()