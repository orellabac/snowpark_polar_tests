from snowflake.snowpark import Session, DataFrame
from data_engineering_package.sqlalchemy_snowpark import create_sqlalchemy_engine
from data_engineering_package.process import process1, process2
import polars as pl
import time, os
from rich import print
from snowflake.snowpark._internal.utils import is_in_stored_procedure
from data_engineering_package.utilities.common import execute_script_code

def read_snowflake_config(connection_name, config_path="~/.snowflake/config.toml"):
    import toml
    config = toml.load(os.path.expanduser(config_path))
    # Retrieve and print relevant details
    if connection_name in config.get("connections"):
        connection_info = config.get("connections").get(connection_name)
        user = connection_info.get("user")
        password = connection_info.get("password")
        account = connection_info.get("account")
        database = connection_info.get("database")
        schema = connection_info.get("schema")  # Optional, as schema may not be specified
        return f"{user}:{password}@{account}/{database}/{schema}"
    else:
        raise KeyError(f"Connection '{connection_name}' not found in config")

def main(session:Session = None):
    total_rows = 150000
    message = ""
    session = Session.builder.getOrCreate()
    execute_script_code("collect_sample_data.sql",session)
    conn = create_sqlalchemy_engine(session)
    start_time = time.time()
    process1.run_process1(f"select * from  SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.ORDERS limit {total_rows}", "orders1",conn)
    end_time = time.time()
    message1 = "Time taken to read data from snowflake with sqlalchemy: " + str(end_time - start_time) + " seconds" 
    print(message1)
    message = message + "\n" + message1

    if not is_in_stored_procedure():
        import adbc_driver_snowflake.dbapi
        start_time = time.time()
        with adbc_driver_snowflake.dbapi.connect(read_snowflake_config("migrations")) as conn:
            process1.run_process1(f"select * from  SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.ORDERS limit {total_rows}", "ORDERS2",conn)
        end_time = time.time()
        message2 = "Time taken to read data from snowflake with adbc:  " + str(end_time - start_time) + " seconds"
        print(message2)
        message = message + "\n" + message2
    return message

if __name__ == "__main__":
    main()
