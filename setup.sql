
CREATE WAREHOUSE IF NOT EXISTS TEST_WH
WAREHOUSE_SIZE = 'XSMALL'
WAREHOUSE_TYPE = 'SNOWPARK-OPTIMIZED'
RESOURCE_CONSTRAINT = 'MEMORY_1X_x86';

-- You need to use absolute paths here, so adjust this to your path
put file:///Users/mrojas/snowpark_polar_tests/packages/polars-1.12.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl 
@mystage overwrite=true auto_compress=false;
put file:///Users/mrojas/snowpark_polar_tests/packages/SQLAlchemy-2.0.36-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
@mystage overwrite=true auto_compress=false;
put file:///Users/mrojas/snowpark_polar_tests/de_with_polars/dist/de_with_polars-0.0.1-py3-none-any.whl @mystage overwrite=true auto_compress=false;
put file:///Users/mrojas/snowpark_polar_tests/code_using_my_code/program.py @mystage overwrite=true auto_compress=false;

use warehouse TEST_WH;
CREATE OR REPLACE PROCEDURE RUN_POLARS()
RETURNS STRING
LANGUAGE PYTHON
RUNTIME_VERSION = '3.9'
HANDLER = 'main'
PACKAGES = ('snowflake-snowpark-python','snowflake-sqlalchemy','rich')
IMPORTS = (
-- You can get this helper from: https://github.com/Snowflake-Labs/snowpark-extensions-py/blob/main/extras/wheel_loader/wheel_loader.py
'@mystage/wheel_loader.py', 
'@mystage/program.py',
'@mystage/de_with_polars-0.0.1-py3-none-any.whl',
'@mystage/polars-1.12.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl',
'@mystage/SQLAlchemy-2.0.36-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl'    
)
AS
$$
import wheel_loader
wheel_loader.add_wheels()
def main(session):
    import program
    return program.main(session)
$$;

call RUN_POLARS();
alter warehouse TEST_WH suspend;