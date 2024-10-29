# utilities/common.py
import polars as pl

def load_data(query: str,conn) -> pl.DataFrame:
    """Loads data from a CSV file using polars."""
    return pl.read_database(query, conn)

def save_data(df: pl.DataFrame, table_name: str, conn) -> None:
    """Saves data to a CSV file using polars."""
    df.write_database(table_name, if_table_exists='replace', connection=conn)

import os, io
from snowflake.connector.util_text import split_statements
import data_engineering_package
def execute_script_code(filename, session):
    # Construct the path to the script file within the package
    package_dir = os.path.dirname(__file__)  # Gets the current package directory
    script_path = os.path.join(package_dir,"..","scripts", filename)

    # Check if the file exists
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"{filename} not found in the script folder.")

    # Read and return the file contents
    with open(script_path, "r") as file:
        code = file.read()
        # Split the code into individual statements
        statements = split_statements(io.StringIO(code))
        for s in statements:
            sql = s[0].strip()
            if sql.endswith(";"):
                sql = sql[:-1]
            session.sql(sql).show()
    
    return code