import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException

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

    def insert_data(self):
      try:
        # Go to the main page where data can be added
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=barang")
        print("Opened barang page")

        # Click on the Insert Data button to open the modal
        insert_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-target="#myModal"]')
        insert_button.click()
        print("Clicked Insert Data button")

        # Wait for the modal to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'myModal'))
        )
        print("Modal opened")

        # Fill in the form fields
        kategori_dropdown = self.driver.find_element(By.ID, 'kategori')
        dropdown_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@id='kategori']/option[text()='ATK']"))
        )
        dropdown_option.click()
        print("Selected category: ATK")

        nama_barang_input = self.driver.find_element(By.ID, 'nama')
        nama_barang_input.send_keys('Puplen ')
        print("Filled product name")

        merk_input = self.driver.find_element(By.ID, 'merk')
        merk_input.send_keys('Standard')
        print("Filled brand")

        harga_beli_input = self.driver.find_element(By.ID, 'beli')
        harga_beli_input.send_keys('2500')
        print("Filled purchase price")

        harga_jual_input = self.driver.find_element(By.ID, 'jual')
        harga_jual_input.send_keys('3000')
        print("Filled selling price")

        satuan_dropdown = self.driver.find_element(By.ID, 'satuan')
        dropdown_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@id='satuan']/option[text()='PCS']"))
        )
        dropdown_option.click()
        print("Selected unit: PCS")

        stok_input = self.driver.find_element(By.ID, 'stok')
        stok_input.send_keys('5')
        print("Filled stock")

        tanggal_input = self.driver.find_element(By.ID, 'tgl')
        tanggal_input.send_keys('2024-06-20')
        print("Filled date")

        # Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Insert Data')]")
        submit_button.click()
        print("Clicked Insert Data button in modal")

        # Wait for success message to appear
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'alert-success')]"))
        )
        print("Success message appeared")

        # Verify that the inserted data appears in the table
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//table[@id='example1']/tbody/tr/td[text()='Pensil']"))
        )
        print("Data appears in the table")

        # Click on the product to view its details
        view_button_xpath = "//table[@id='example1']/tbody/tr[td[text()='Pensil']]/td/a[contains(@href,'view')]"
        view_button = self.driver.find_element(By.XPATH, view_button_xpath)
        view_button.click()
        print("Clicked View button for the product 'Pensil'")

        # Wait for the detail page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h3[text()='Details Barang']"))
        )
        print("Product details page loaded")

        # Verify product details
        details_id = self.driver.find_element(By.XPATH, "//table[@class='table table-striped']/tr[td[text()='ID Barang']]/td[2]").text
        details_name = self.driver.find_element(By.XPATH, "//table[@class='table table-striped']/tr[td[text()='Nama Barang']]/td[2]").text
        self.assertEqual(details_name, 'Pensil', "Product name does not match")
        print(f"Verified product ID: {details_id} and name: {details_name}")

        time.sleep(3)  # Wait for 3 seconds before proceeding to edit

      except NoSuchElementException as e:
        print(f"Error finding element: {e}")
      except TimeoutException as e:
        print(f"Timeout waiting for element: {e}")

    def test_edit_and_delete_data(self):
      try:
        self.login()
        self.insert_data()  # Call insert_data method to add new data

        # Go to the main page where data can be edited
        self.driver.get("http://localhost/Aplikasi-Kasir-Berbasis-Web-main/kasir/index.php?page=barang")
        print("Opened barang page")

        # Click on the "Details" button for the specific product added
        details_button_xpath = "//table[@id='example1']/tbody/tr[td[text()='Pensil']]/td/a[contains(@href,'details')]"
        details_button = self.driver.find_element(By.XPATH, details_button_xpath)
        details_button.click()
        print("Clicked Details button for the product 'Pensil'")

        # Wait for the details page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h3[text()='Details Barang']"))
        )
        print("Product details page loaded")

        # Additional wait time to ensure the details page is fully loaded and visible
        time.sleep(5)  # Wait for 5 seconds

        # Click the "Back" button to return to the barang page
        back_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Balik')]")
        back_button.click()
        print("Clicked Back button to return to barang page")

        time.sleep(3)  # Wait for 3 seconds before proceeding to edit

        # Find the Edit button for the specific product added
        edit_button_xpath = "//table[@id='example1']/tbody/tr[td[text()='Pensil']]/td/a[contains(@href,'edit')]"
        edit_button = self.driver.find_element(By.XPATH, edit_button_xpath)
        edit_button.click()
        print("Clicked Edit button for the product 'Pensil'")

        # Wait for the edit page to load (assuming it is a separate page)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'nama'))
        )
        print("Edit page loaded")

        # Change category to 'ATK'
        kategori_dropdown = self.driver.find_element(By.NAME, 'kategori')
        kategori_dropdown.click()
        kategori_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='kategori']/option[text()='ATK']"))
        )
        kategori_option.click()
        print("Changed category to ATK")

        # Modify the form fields (for example, change the product name)
        nama_barang_edit = self.driver.find_element(By.NAME, 'nama')
        nama_barang_edit.clear()  # Clear existing text
        nama_barang_edit.send_keys('Pulpen ku')
        print("Changed product name to Pensil 2B")

        # Change brand to 'Staedtler'
        merk_edit = self.driver.find_element(By.NAME, 'merk')
        merk_edit.clear()
        merk_edit.send_keys('Staedtler')
        print("Changed brand to Staedtler")

        # Change purchase price to '2500'
        harga_beli_edit = self.driver.find_element(By.NAME, 'beli')
        harga_beli_edit.clear()
        harga_beli_edit.send_keys('2500')
        print("Changed purchase price to 2500")

        # Change selling price to '3500'
        harga_jual_edit = self.driver.find_element(By.NAME, 'jual')
        harga_jual_edit.clear()
        harga_jual_edit.send_keys('3500')
        print("Changed selling price to 3500")

        # Change stock to '15'
        stok_edit = self.driver.find_element(By.NAME, 'stok')
        stok_edit.clear()
        stok_edit.send_keys('15')
        print("Changed stock to 15")

        # Submit the edited form
        update_button = self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-primary') and contains(text(),'Update Data')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update_button)
        time.sleep(1)  # Optional: Add a small delay after scroll

        update_button.click()
        print("Clicked Update Data button in edit page")

        # Wait for success message to appear
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'alert-success')]"))
        )
        print("Success message appeared after edit")

        time.sleep(3)  # Wait for 3 seconds before verifying the edited data

        # Click the "Back" button to return to the barang page
        back_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Balik')]")
        back_button.click()
        print("Clicked Back button to return to barang page")

        time.sleep(3)  # Wait for 3 seconds before verifying the edited data

        # Verify the edited data in the table
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//table[@id='example1']/tbody/tr[td[text()='Pensil 2B']]"))
        )
        print("Verified edited data appears in the table")

        # Locate and click the delete button
        delete_button_xpath = "//table[@id='example1']/tbody/tr[td[text()='Pensil 2B']]/td/a[contains(@href,'hapus')]"
        delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
        delete_button.click()
        print("Clicked delete button for the product 'Pensil 2B'")

        try:
            # Handle confirmation dialog with delay
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            self.assertIn("Hapus Data barang ?", alert_text)  # Check for expected alert text
            alert.accept()

            # Wait for success message after deletion
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']/p"))
            )
            print("Success message appeared after delete")

            # Assert that success message contains expected text
            success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']/p").text
            self.assertIn("Hapus Data Berhasil !", success_message)

        except UnexpectedAlertPresentException as e:
            print(f"Unexpected alert present: {e}")
            alert = self.driver.switch_to.alert
            alert.dismiss()  # Dismiss the unexpected alert
            self.fail("Unexpected alert appeared during deletion")

      except NoSuchElementException as e:
        print(f"Error finding element: {e}")
      except TimeoutException as e:
        print(f"Timeout waiting for element: {e}")
      except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    unittest.main()
