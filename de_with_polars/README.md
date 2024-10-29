# Data Engineering Package with Polars

A Python package demonstrating basic data engineering practices using `polars`. This project includes modules for data transformations, utility functions, and process scripts, organized in a modular, reusable structure.

## Project Structure

```plaintext
data_engineering_package/
├── __init__.py
├── base/
│   ├── __init__.py
│   └── base_transformation.py         # Base transformations, e.g., dropping nulls, adding columns
├── advance/
│   ├── __init__.py
│   └── advanced.py                    # Advanced transformations, e.g., filtering and aggregations
├── process/
│   ├── __init__.py
│   ├── process1.py                    # Process script using AdvancedTransformation
│   └── process2.py                    # Process script using BaseTransformation
└── utilities/
    ├── __init__.py
    └── common.py                      # Utilities for loading and saving data
```

## Features

- **Utilities** (`utilities/common.py`): Helper functions to load and save data.
- **Base Transformations** (`base/base_transformation.py`): Simple data transformations (e.g., drop nulls, add columns).
- **Advanced Transformations** (`advance/advanced.py`): Advanced operations such as filtering and aggregation.
- **Process Scripts** (`process/process1.py`, `process/process2.py`): Examples of workflows combining transformations and utilities.

## Getting Started

### Prerequisites

- **Python**: Ensure you have Python 3.7+ installed.
- **polars**: Install the `polars` library to handle data frames efficiently.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/data-engineering-package.git
   cd data-engineering-package
   ```
2. Install required dependencies:

   ```bash
   pip install polars
   ```

### Running the Code

The process scripts (`process1.py` and `process2.py`) illustrate basic data workflows. Update file paths for your local environment as needed.

#### Example Usage

1. Run `process1.py` to load data, apply transformations, and save results:

   ```bash
   python process/process1.py
   ```

   **Operations in `process1.py`:**

   - Load data from CSV
   - Drop null values
   - Add a new column
   - Filter rows based on a threshold
   - Aggregate data by group
2. Run `process2.py` to apply base transformations:

   ```bash
   python process/process2.py
   ```

   **Operations in `process2.py`:**

   - Load data from CSV
   - Drop null values
   - Add a column with static values

### Code Examples

#### Loading Data

```python
from utilities.common import load_data

df = load_data("select * from table", conn)
```

#### Applying Transformations

```python
from advance.advanced import AdvancedTransformation

transformation = AdvancedTransformation(df)
result = transformation.drop_nulls().filter_data("some_column", 10).aggregate_data("group_column", "some_column")
```

#### Saving Data

```python
from utilities.common import save_data

save_data(result, "table_name", conn)
```
