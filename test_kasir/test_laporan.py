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
        time.sleep(3)  # Tunggu 3 detik sebelum menutup browser
        self.driver.quit()

    def login(self):
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/login.php")
        user_input = self.driver.find_element(By.XPATH, "//input[@id='user']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_input.send_keys("admin")
        password_input.send_keys("admin")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Tunggu hingga alert login muncul
        time.sleep(1)  # Tunggu 1 detik
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.assertIn("Login Sukses", alert.text)
            alert.accept()
        except Exception as e:
            print(f"Gagal menemukan atau menangani alert login: {e}")

        # Tunggu hingga halaman utama dimuat setelah login berhasil
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='home']")))
        except Exception as e:
            print(f"Timeout menunggu halaman utama: {e}")

    def test_laporan_penjualan(self):
        self.login()

        # Navigasi ke halaman laporan
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=laporan")

        # Tunggu hingga form untuk cari laporan per bulan dimuat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@action='index.php?page=laporan&cari=ok']")))

        # Pilih bulan dan tahun
        bulan_dropdown = self.driver.find_element(By.NAME, "bln")
        bulan_dropdown.send_keys("Juni")  # Sesuaikan dengan kasus pengujian Anda
        
        tahun_dropdown = self.driver.find_element(By.NAME, "thn")
        tahun_dropdown.send_keys("2024")  # Sesuaikan dengan kasus pengujian Anda

        # Klik tombol Cari
        cari_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
        cari_button.click()

        # Tunggu hingga tabel dengan laporan dimuat
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "example1")))

        # Klik link unduh Excel berdasarkan bulan
        excel_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'excel.php') and contains(@class,'btn-info')]")))
        excel_button.click()

        # Tunggu hingga halaman berikutnya dimuat
        time.sleep(3)

          # Tunggu hingga form untuk cari laporan per hari dimuat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@action='index.php?page=laporan&hari=cek']")))

        # Pilih bulan dan tahun
        tanggal_input = self.driver.find_element(By.NAME, "hari")
        tanggal_input.send_keys("22/06/2024")  # Sesuaikan dengan kasus pengujian Anda

        # Klik tombol Cari
        cari_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        cari_button.click()

        # Tunggu hingga tabel dengan laporan dimuat
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "example1")))

        # Klik link unduh Excel berdasarkan hari yang dipilih
        excel_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'excel.php') and contains(@class,'btn-info')]")))
        excel_button.click()

if __name__ == "__main__":
    unittest.main()
