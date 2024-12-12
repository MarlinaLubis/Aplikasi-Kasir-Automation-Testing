import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Implicit wait for all find_element calls

    def tearDown(self):
        # Menutup WebDriver setelah jeda 5 detik
        time.sleep(5)
        self.driver.quit()

    def login(self, user, password):
        try:
            # Membuka halaman login
            self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/login.php")
            print("Opened login page")

            # Mencari elemen input username dan password menggunakan XPath
            user_input = self.driver.find_element(By.XPATH, "//input[@id='user']")
            password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
            print("Found user and password input elements")

            # Memasukkan nama pengguna dan kata sandi
            user_input.send_keys(user)
            password_input.send_keys(password)
            print("Entered username and password")

            # Klik tombol Login
            button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            button.click()
            print("Clicked login button")

            # Tunggu hingga muncul alert dan terima alert tersebut
            WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Accepted alert")

            # Tunggu hingga halaman beranda dimuat
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='home']"))
            )
            print("Home page loaded")

        except NoSuchElementException as e:
            print(f"Error finding element: {e}")
        except TimeoutException as e:
            print(f"Timeout waiting for alert or element: {e}")

    def navigate_to_barang(self):
        # Navigasi ke halaman menu barang
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=barang")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Data Barang')]"))
        )

    def add_barang(self, kategori, nama, merk, beli, jual, satuan, stok):
        try:
            # Klik tombol untuk membuka modal tambah barang
            add_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-target="#myModal"]')
            time.sleep(2)  # Tambahkan waktu tunggu sebelum mengklik
            add_button.click()
            print("Clicked Insert Data button")

            # Tunggu modal terbuka
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'myModal'))
            )
            print("Modal opened")

            # Isi form tambah barang
            self.driver.find_element(By.ID, "kategori").send_keys(kategori)
            self.driver.find_element(By.ID, "nama").send_keys(nama)
            self.driver.find_element(By.ID, "merk").send_keys(merk)
            self.driver.find_element(By.ID, "beli").send_keys(beli)
            self.driver.find_element(By.ID, "jual").send_keys(jual)
            self.driver.find_element(By.ID, "satuan").send_keys(satuan)
            self.driver.find_element(By.ID, "stok").send_keys(stok)

            # Gunakan JavaScript untuk mengisi field tanggal yang readonly
            tanggal_input = self.driver.find_element(By.ID, 'tgl')
            date_script = 'arguments[0].value = "2024-06-20 10:00";'
            self.driver.execute_script(date_script, tanggal_input)
            print("Filled date using JavaScript")

            # Submit form
            submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Insert Data')]")
            submit_button.click()
            print("Clicked Insert Data button in modal")

            # Tunggu hingga modal tertutup dan halaman diperbarui
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'alert-success')]"))
            )
            print("Success message appeared")

        except NoSuchElementException as e:
            print(f"Error finding element: {e}")
        except TimeoutException as e:
            print(f"Timeout waiting for element: {e}")

    def edit_barang(self, id_barang, nama_kategori, nama_barang, merk, harga_beli, harga_jual, satuan, stok):
        try:
            # Navigasi ke halaman barang
            self.navigate_to_barang()

            # Klik tombol edit pada barang tertentu
            edit_button_xpath = f"//a[contains(@href,'index.php?page=barang/edit')][contains(@href,'barang={id_barang}')]"
            edit_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, edit_button_xpath))
            )
            edit_button.click()
            print("Clicked Edit button for a product")

            # Tunggu halaman edit terbuka
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'editModal'))  # Update to match actual modal ID
            )
            print("Edit modal opened")

            # Edit data barang
            self.driver.find_element(By.NAME, 'kategori').send_keys(nama_kategori)
            nama_barang_edit = self.driver.find_element(By.NAME, 'nama')
            nama_barang_edit.clear()
            nama_barang_edit.send_keys(nama_barang)
            print("Changed product name to", nama_barang)

            self.driver.find_element(By.NAME, 'merk').send_keys(merk)
            self.driver.find_element(By.NAME, 'beli').send_keys(harga_beli)
            self.driver.find_element(By.NAME, 'jual').send_keys(harga_jual)
            self.driver.find_element(By.NAME, 'satuan').send_keys(satuan)
            self.driver.find_element(By.NAME, 'stok').send_keys(stok)

            # Gunakan JavaScript untuk mengisi field tanggal yang readonly
            tanggal_edit = self.driver.find_element(By.NAME, 'tgl')
            date_script = 'arguments[0].value = "2024-07-01 10:00";'
            self.driver.execute_script(date_script, tanggal_edit)
            print("Changed date using JavaScript")

            # Submit form
            submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Update Data')]")
            submit_button.click()
            print("Clicked Update Data button in modal")

            # Tunggu hingga halaman kembali ke daftar barang
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Data Barang')]"))
            )
            print("Data Barang page reloaded")

        except NoSuchElementException as e:
            print(f"Error finding element: {e}")
        except TimeoutException as e:
            print(f"Timeout waiting for element: {e}")

    def delete_barang(self, id_barang):
        try:
            # Navigasi ke halaman barang
            self.navigate_to_barang()

            # Klik tombol hapus pada barang tertentu
            delete_button_xpath = f"//a[contains(@href,'index.php?page=barang/hapus')][contains(@href,'barang={id_barang}')]"
            delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
            delete_button.click()
            print("Clicked Delete button for a product")

            # Konfirmasi penghapusan
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Accepted alert")

            # Tunggu hingga halaman diperbarui
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
            )
            print("Success message appeared after deletion")

        except NoSuchElementException as e:
            print(f"Error finding element: {e}")
        except TimeoutException as e:
            print(f"Timeout waiting for element: {e}")

    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("admin", "123")

        # Tambah data barang
        self.add_barang("Sabun", "Sabun Mandi", "Lifebuoy", "5000", "10000", "PCS", "20")

        # Edit data barang
        self.edit_barang("BR038", "Perawatan", "Odol", "Pepsodent", "6000", "12000", "PCS", "30")

        # Hapus data barang
        self.delete_barang("BR038")

if __name__ == "__main__":
    unittest.main()
