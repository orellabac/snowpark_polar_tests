# advance/advanced.py
from data_engineering_package.base.base_transformations import BaseTransformation
import polars as pl

class AdvancedTransformation(BaseTransformation):
    def filter_data(self, column: str, threshold: float) ->  pl.DataFrame:
        """Filters rows based on a threshold for a specific column."""
        self.data = self.data.filter(pl.col(column) > threshold)
        return self.data

    def aggregate_data(self, group_by_column: str, agg_column: str) -> pl.DataFrame:
        """Aggregates data by computing the mean of a column grouped by another column."""
        self.data = self.data.group_by(group_by_column).agg(pl.col(agg_column).mean().alias(f"{agg_column}_mean"))
        return self.data
