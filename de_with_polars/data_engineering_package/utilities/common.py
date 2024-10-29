# utilities/common.py
import polars as pl

def load_data(query: str,conn) -> pl.DataFrame:
    """Loads data from a CSV file using polars."""
    return pl.read_database(query, conn)

def save_data(df: pl.DataFrame, table_name: str, conn) -> None:
    """Saves data to a CSV file using polars."""
    df.write_database(table_name, if_table_exists='replace', connection=conn)
