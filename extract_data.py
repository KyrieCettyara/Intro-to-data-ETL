import pandas as pd
import psycopg2




def extract_db() -> pd.DataFrame:
    DB_NAME = 'etl_db'
    DB_USER = 'postgres'
    DB_PASSWORD = 'password123'
    DB_HOST = 'localhost'
    DB_PORT ='5433'

    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

    query = "SELECT * FROM amazon_sales_data"

    df = pd.read_sql(query, conn)

    conn.close()
    
    df.to_csv('data/raw/amazon_sales_data.csv', index=False)
    return df
