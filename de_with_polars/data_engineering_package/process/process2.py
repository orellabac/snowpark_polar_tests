from data_engineering_package.utilities.common import load_data, save_data
from data_engineering_package.base.base_transformations import BaseTransformation

def run_process2(input_file: str, output_file: str) -> None:
    # Load data
    df = load_data(input_file)

    # Apply simple base transformations
    transformation = BaseTransformation(df)
    transformation.drop_nulls()
    transformation.add_column("another_column", [5] * df.height)
    result = transformation.data

    # Save result
    save_data(result, output_file)

if __name__ == "__main__":
    run_process2("select * from  SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.ORDERS limit 150000", "CUSTOMER_SAMPLE1")
