# PENGUJIAN SISTEM
![WhatsApp Image 2023-06-16 at 19 44 07](https://github.com/rplulbi/SQA/assets/15622730/fa9d0c3b-cbc3-48ab-81d1-b29cb1b6b328)
![WhatsApp Image 2023-06-16 at 19 53 09](https://github.com/rplulbi/SQA/assets/15622730/cb65425d-eca1-48bf-90da-44177a4246c1)
![WhatsApp Image 2023-06-16 at 20 16 53](https://github.com/rplulbi/SQA/assets/15622730/4385c756-c760-40cb-a1ba-ce4aa1f5c277)

Ada beberapa aplikasi yang populer digunakan untuk pengujian kualitas sistem. Berikut adalah beberapa contoh aplikasi yang umum digunakan dalam praktik pengujian perangkat lunak:
1. [Selenium](https://www.selenium.dev/): Selenium adalah alat pengujian otomatis yang digunakan untuk mengotomatisasi pengujian pada aplikasi web. Ini memungkinkan pengujian fungsional dan regresi melalui perekaman dan pemutaran aksi pengguna pada browser. 
![image](https://github.com/rplulbi/SQA/assets/15622730/5ef058dc-9dc2-41e9-a841-848803dc7ccb)

3. [JUnit](https://junit.org/junit5/): JUnit adalah kerangka kerja pengujian unit yang digunakan untuk pengujian unit perangkat lunak berbasis Java. Ini menyediakan metode untuk mengatur dan menjalankan pengujian unit secara otomatis.
![image](https://github.com/rplulbi/SQA/assets/15622730/9ee1f6e8-9d50-4243-9462-28d9155458a8)

5. [Appium](https://appium.io/docs/en/2.0/): Appium adalah alat pengujian otomatis yang digunakan untuk pengujian aplikasi seluler (Android dan iOS). Ini memungkinkan pengujian fungsional pada aplikasi seluler menggunakan skrip pengujian yang ditulis dalam bahasa pemrograman seperti Java, Python, atau Ruby.
![image](https://github.com/rplulbi/SQA/assets/15622730/2576eeee-febe-427b-a3f7-a397bdc08da8)

6. [LoadRunner](https://www.microfocus.com/en-us/products/loadrunner-professional/overview): LoadRunner adalah alat pengujian kinerja yang digunakan untuk menguji kinerja, ketahanan, dan skalabilitas sistem. Ini dapat mensimulasikan lalu lintas pengguna yang tinggi untuk melihat bagaimana aplikasi atau sistem berkinerja di bawah tekanan.
![image](https://github.com/rplulbi/SQA/assets/15622730/2a89a6e2-be0b-4c93-b051-3744c21deea6)

7. [Postman](https://www.postman.com/): Postman adalah alat pengujian API yang digunakan untuk menguji dan mengelola API. Ini memungkinkan pengujian fungsional dan validasi API dengan mengirim permintaan HTTP dan menganalisis tanggapan yang diterima.
![image](https://github.com/rplulbi/SQA/assets/15622730/9b4e7152-58c3-48a2-93f5-78455eaeb75d)

8. [JMeter](https://jmeter.apache.org/): Apache JMeter adalah alat pengujian kinerja yang digunakan untuk menguji kinerja aplikasi web, layanan web, dan protokol lainnya. Ini dapat mengukur kinerja sistem dengan memuat tes beban yang besar dan menganalisis responsnya.
![image](https://github.com/rplulbi/SQA/assets/15622730/130b2c58-48ac-4838-8be5-ebc724773a52)

9. [SonarQube](https://docs.sonarqube.org/latest/): SonarQube adalah alat pengujian statis dan analisis kode yang digunakan untuk mengidentifikasi masalah kualitas kode seperti bug, kelemahan keamanan, dan pelanggaran standar kode. Ini membantu dalam meningkatkan kualitas kode dan memastikan kepatuhan terhadap praktik pengembangan yang baik.
![image](https://github.com/rplulbi/SQA/assets/15622730/ec09e1ce-d0b9-4752-98f6-01f734b79e87)

10. [TestComplete](https://smartbear.com/product/testcomplete/): TestComplete adalah alat pengujian otomatis yang mendukung pengujian fungsional dan regresi pada berbagai platform, termasuk aplikasi desktop, web, dan seluler. Ini memiliki antarmuka pengguna grafis yang mudah digunakan dan mendukung berbagai bahasa pemrograman.
![image](https://github.com/rplulbi/SQA/assets/15622730/7a626bb3-fa89-427a-97ed-f6dda8fa0b1b)

Perlu diingat bahwa pilihan alat pengujian kualitas sistem dapat bervariasi tergantung pada kebutuhan dan preferensi spesifik proyek atau organisasi.

# Selenium Python
## Instal Python
Silahkan download terlebih dahulu [PYTHON WINDOWS](https://www.python.org/)
Lakukan prosess instalasinya sampai selesai
lakukan pengecekan instalasi python 
![image](https://github.com/rplulbi/SQA/assets/15622730/7ec2bf99-31d4-4170-bd06-7be2b0e01b91)

## Instal Kode Editor
Download [VSCODE](https://code.visualstudio.com/) 
tambahkan ekstensi python nya
![image](https://github.com/rplulbi/SQA/assets/15622730/8a8a1a3d-fab9-492c-8684-387e0286bb7a)

## Instal Selenium
**Ketikan perintah berikut pada terminal
**
``` py
pip install selenium
```
![image](https://github.com/rplulbi/SQA/assets/15622730/7eb29346-c5a1-4029-871a-6bb32e18f78c)

**Cek instalasi selenium
**
``` py
pip list
```
![image](https://github.com/rplulbi/SQA/assets/15622730/7d4e5bf2-782c-4447-b05d-06a9f3ed43d4)

Instal Chrome Driver
[Chrome Driver](https://chromedriver.chromium.org/downloads)
pilih sesuai chrome nya
![image](https://github.com/rplulbi/SQA/assets/15622730/6f9848f7-29c6-4143-8128-5eec859f80de)
Cek Instalasi
![image](https://github.com/rplulbi/SQA/assets/15622730/1f03af10-cd18-412e-bb3b-e96cabfa00ec)
Masukan Path Chrome Drivernya pada Environment WINDOWS

Hasilnya begini
![image](https://github.com/rplulbi/SQA/assets/15622730/d24fb396-324f-464e-b9ea-7fe4f36fc085)
![image](https://github.com/rplulbi/SQA/assets/15622730/e9f4e523-6a18-4f7a-a99e-30de7d8e6669)

# Menambahkan Locating Element
![image](https://github.com/rplulbi/SQA/assets/15622730/0b5e0d93-13f5-4938-b99c-d4a5ac6105f0)
Tambahkan Kodingan berikut pada file yang akan di tambahkan
disini yang akan digunakan adalah findelemen.py

![image](https://github.com/rplulbi/SQA/assets/15622730/6bf9cac0-d930-4944-b71e-fa8cf93f5773)





