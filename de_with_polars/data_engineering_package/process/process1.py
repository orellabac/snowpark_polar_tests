# process/process1.py
from data_engineering_package.utilities.common import load_data, save_data
from data_engineering_package.advanced.advanced import AdvancedTransformation
import polars as pl

def run_process1(input_query: str, output_table: str, conn) -> None:
    # Load data
    df = load_data(input_query, conn)

    # Apply transformations
    transformation = AdvancedTransformation(df)
    transformation.drop_nulls()
    transformation.add_column("COUNTS", [1] * df.height)
    transformation.filter_data("O_TOTALPRICE", threshold=140000)
    result = transformation.aggregate_data("O_ORDERSTATUS", "O_TOTALPRICE")
    print(f"Number of rows: {result.height}")
    # Save result
    save_data(result, output_table, conn)

if __name__ == "__main__":
    run_process1("select * from  SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.ORDERS limit 150000", "CUSTOMER_SAMPLE1")
