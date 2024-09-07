import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


def load_data(df: pd.DataFrame, table: str) -> pd.DataFrame:
    LOCAL_DB_NAME = 'store_data'
    LOCAL_DB_USER = 'postgres'
    LOCAL_DB_PASSWORD = 'mypassword'
    LOCAL_DB_HOST = 'localhost'
    LOCAL_DB_PORT = 5436

    conn = create_engine(
        f"postgresql://{LOCAL_DB_USER}:{LOCAL_DB_PASSWORD}@{LOCAL_DB_HOST}:{LOCAL_DB_PORT}/{LOCAL_DB_NAME}"
    )

    df["created_at"] = datetime.now()

    df.to_sql(name=table, con=conn, if_exists="replace", index=False)

    conn.dispose()

    return df
