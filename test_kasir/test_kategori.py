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

    def test_kategori(self):
        self.login()

        # Navigate to the category page
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=kategori")

        # Wait until the form is loaded
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='kategori']")))
        except Exception as e:
            print(f"Failed to load category page: {e}")
            return

        # Fill the form with new data
        input_nama_kategori = self.driver.find_element(By.XPATH, "//input[@name='kategori']")
        input_nama_kategori.clear()
        input_nama_kategori.send_keys("Snack")

        # Submit the form
        tombol_simpan = self.driver.find_element(By.XPATH, "//button[@id='tombol-simpan']")
        tombol_simpan.click()

        # Wait for success message
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert alert-success')]//p")))
            success_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert alert-success')]//p")
            self.assertIn("Tambah Data Berhasil !", success_message.text)
        except Exception as e:
            print(f"Failed to find success message: {e}")

        # Add delay before editing the category
        time.sleep(5)  # Wait for 5 seconds before editing

        # Editing the category data
        # Assuming the UID of the newly added category is available or can be retrieved
        # Here we will just simulate clicking the edit button for the first item in the list

        # Wait for the table to be present
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@id='example1']//tbody//tr[1]//a[contains(@href, 'uid=')]")))
            edit_button = self.driver.find_element(By.XPATH, "//table[@id='example1']//tbody//tr[1]//a[contains(@href, 'uid=')]//button[@class='btn btn-warning']")
            edit_button.click()
        except Exception as e:
            print(f"Failed to find edit button: {e}")
            return

        # Wait until the edit form is loaded
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='kategori']")))
        except Exception as e:
            print(f"Failed to load edit form: {e}")
            return

        # Edit the form with new data
        input_nama_kategori = self.driver.find_element(By.XPATH, "//input[@name='kategori']")
        input_nama_kategori.clear()
        input_nama_kategori.send_keys("ATK")

        # Submit the form
        tombol_ubah = self.driver.find_element(By.XPATH, "//button[@id='tombol-simpan']")
        tombol_ubah.click()

        # Wait for success message after editing
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert alert-success')]//p")))
            success_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert alert-success')]//p")
            self.assertIn("Update Data Berhasil !", success_message.text)
        except Exception as e:
            print(f"Failed to find success message after editing: {e}")

        # Add a delay before clicking the delete button
        time.sleep(5)  # Wait for 5 seconds before deleting

        # Now proceed to delete the edited category
        # Assuming we want to delete the first category in the list
        delete_button_xpath = "//table[@id='example1']//tbody//tr[1]//a[contains(@href, 'fungsi/hapus/hapus.php')]/button[@class='btn btn-danger']"

        # Click on the delete button of the first category
        try:
            delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
            delete_button.click()
        except Exception as e:
            print(f"Failed to find or click delete button: {e}")
            return

        # Handle confirmation dialog with delay
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            self.assertIn("Hapus Data Kategori ?", alert_text)
            time.sleep(2)  # Wait for 2 seconds before accepting alert
            alert.accept()

            # Wait for success message after deletion
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert alert-success')]//p")))
            success_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert alert-success')]//p")
            self.assertIn("Hapus Data Berhasil !", success_message.text)
        except Exception as e:
            print(f"Failed to handle delete confirmation alert: {e}")
            return

if __name__ == "__main__":
    unittest.main()
