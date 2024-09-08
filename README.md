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

![alt text](https://github.com/KyrieCettyara/Intro-to-data-ETL/blob/main/image/design.png)


## ETL Design
Untuk memastikan bahwa pipeline dijalankan secara berkala maka dilakukan scheduling menggunakan crontab. 

Script yang akan dijalankan oleh crontab adalah sebagai berikut.

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
Pipeline berhasil dijalankan.

![alt text](https://github.com/KyrieCettyara/Intro-to-data-ETL/blob/main/image/summary.png)


Table Product

![alt text](https://github.com/KyrieCettyara/Intro-to-data-ETL/blob/main/image/table_product.png)

Table Sales

![alt text](https://github.com/KyrieCettyara/Intro-to-data-ETL/blob/main/image/table_sales.png)


### Scenario 2
Tarikan data sebelum insert data
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/before_testing1.png)


Tarikan data setelah insert data
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/after_testing1.png)
