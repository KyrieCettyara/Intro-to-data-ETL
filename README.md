# Introduction to Data 
# Background
Pada proyek ini diharapkan membuat pipeline yang akan melakukan simpel Extract, Transfor, dan Load dari CSV dan database. 

## Requirement Gathering dan Solution
- Data yang telah dimiliki perlu untuk diolah lebih lanjut karena kedua data tersebut berada di dua tempat yang berbeda sehingga sulit untuk dilakukan analisa.

Solusi:
1. Membuat pipeline. Pipeline yang dibuat akan mengekstrak data dari kedua sumber data, kemudian melakukan transform pada data tersebut dan me-load data ke satu database sehingga lebih dapat digunakan untuk analisa.

2. Melakukan scheduling sehingga proses dilakukan secara berkala dan otomatis.


## ETL Design
Pipeline akan mengikuti alur seperti pada gambar, yaitu:
- Extract
- Transform
- Load

![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/flow.png)


## ETL Design
Untuk memastikan bahwa pipeline dijalankan secara berkala maka dilakukan scheduling menggunakan crontab. 

Script yang akan dijalankan oleh crontab adalah




# User Flowchart
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/flow.png)

Berdasarkan flow diatas. Pertama kali user akan melihat halaman login. User yang belum memiliki akun diharuskan untuk melakukan registrasi terlebih dahulu. Jika user sudah memiliki akun, user dapat memasukkan username dan password. Jika username dan password yang diberikan benar maka akan ditampilkan halaman home. Jika username dan password yang dimasukkan salah maka user akan diminta untuk memasukkan kombinasi username dan password yang benar. User yang sudah berhasil mengakses halaman home dapat membuat tweet dengan mengupload gambar ataupun tidak. Melalui halaman home user juga dapat melihat tweet yang dimasukkan oleh user lainnya dan mengakses leaderboard untuk melihat jumlah banyak tweet yang diinput oleh semua user. 


# Requirements and Technology Used
### backend
- Python
- Flask
- Flask-JWT-Extended
- Flask-Cors
- Flask-SQLAlchemy
- psycopg2

### frontend
- vue
- vue-router
- axios
- datatables.net
- tailwindcss
- vue-sweetalert2
- pinia


~~~
#!/bin/bash

echo "========== Start dbt with Luigi Orchestration Process =========="

# Set Python script
PYTHON_SCRIPT="./elt.py"

# Get Current Date
current_datetime=$(date '+%d-%m-%Y_%H-%M')

# Append Current Date in the Log File
LOG_FILE="./logs/elt/elt_$current_datetime.log"

# Run Python Script and Insert Log
python "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1

echo "========== End of dbt with Luigi Orchestration Process =========="
~~~


# Testing Scenario
### Scenario 1

![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/login.png)

Pipeline berhasil dijalankan.

![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/login.png)

Table Product

![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/login.png)

Table Sales


### Scenario 2
Tarikan data sebelum insert data
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/home.png)


Tarikan data setelah insert data
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/upload.png)
