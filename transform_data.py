import pandas as pd

def transform_product_data(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_drop = [
        "ean",
        "Unnamed: 26",
        "Unnamed: 27",
        "Unnamed: 28",
        "Unnamed: 29",
        "Unnamed: 30",
    ]

    df.drop(columns=columns_to_drop, inplace=True)

    df.fillna("Not Found", inplace=True)

    df.drop_duplicates(keep='first')



    return df

def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_drop = ["Unnamed: 0"]

    df.drop(columns=columns_to_drop, inplace=True)

    df.dropna(subset=["actual_price"], inplace=True)

    df.fillna(0, inplace=True)

    df.drop_duplicates(keep='first')

    return df