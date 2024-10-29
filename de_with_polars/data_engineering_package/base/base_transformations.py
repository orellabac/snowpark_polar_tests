import polars as pl

class BaseTransformation:
    def __init__(self, data: pl.DataFrame):
        self.data = data

    def drop_nulls(self) -> pl.DataFrame:
        """Removes rows with null values."""
        self.data = self.data.drop_nulls()
        return self.data

    def add_column(self, column_name: str, values) -> pl.DataFrame:
        """Adds a new column with specified values."""
        self.data = self.data.with_columns(pl.Series(name=column_name, values=values))
        return self.data
