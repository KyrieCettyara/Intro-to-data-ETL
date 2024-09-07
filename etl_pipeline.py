import os
import luigi
import pandas as pd
from extract_data import extract_db
from validate_data import validate_data
from transform_data import transform_product_data, transform_sales_data
from load_data import load_data

class ForceableTask(luigi.Task):
    force = luigi.BoolParameter(significant=False, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.force is True:
            outputs = luigi.task.flatten(self.output())
            for out in outputs:
                if out.exists():
                    os.remove(out.path)


class ExtractDataFromCSV(luigi.Task):
    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        return luigi.LocalTarget("data/raw/ElectronicsProductsPricingData.csv")


class ExtractDataFromDB(ForceableTask):
    def requires(self):
        pass

    def run(self):
        df = extract_db()

        df.to_csv(self.output().path, index=False)

    def output(self):
        return luigi.LocalTarget("data/raw/amazon_sales_data.csv")


class ValidateData(luigi.Task):
    def requires(self):
        return [
            ExtractDataFromCSV(),
            ExtractDataFromDB(),
        ]

    def run(self):
        tables = ["amazon_sales_data", "ElectronicsProductsPricingData"]

        for index, table in enumerate(tables):
            df = pd.read_csv('data/raw/' + table + '.csv')

            validate_data(df, table)

    def output(self):
        pass


class TransformProducts(luigi.Task):
    def requires(self):
        return ExtractDataFromCSV()

    def run(self):
        df = pd.read_csv(self.input().path)

        transformed_df = transform_product_data(df)

        transformed_df.to_csv(self.output().path, index=False)

    def output(self):
        return luigi.LocalTarget("data/transform/transform_ElectronicsProductsPricingData.csv")


class TransformSalesData(ForceableTask):
    def requires(self):
        return ExtractDataFromDB()

    def run(self):
        df = pd.read_csv(self.input().path)

        transformed_df = transform_sales_data(df)

        transformed_df.to_csv(self.output().path, index=False)

    def output(self):
        return luigi.LocalTarget("data/transform/transform_sales_data.csv")


class LoadData(ForceableTask):

    def requires(self):
        return [TransformProducts(), TransformSalesData()]

    def run(self):
        products_df = pd.read_csv(self.input()[0].path)
        sales_df = pd.read_csv(self.input()[1].path)

        loaded_products_df = load_data(products_df, "product")
        loaded_sales_df = load_data(sales_df, "sales")

        loaded_products_df.to_csv(self.output()[0].path, index=False)
        loaded_sales_df.to_csv(self.output()[1].path, index=False)

    def output(self):
        return [
            luigi.LocalTarget("data/load/load_products_data.csv"),
            luigi.LocalTarget("data/load/load_sales_data.csv"),
        ]


if __name__ == "__main__":
    luigi.build(
        [
            ExtractDataFromCSV(),
            ExtractDataFromDB(force=True),
            ValidateData(),
            TransformProducts(),
            TransformSalesData(force=True),
            LoadData(force=True),
        ]
    )
