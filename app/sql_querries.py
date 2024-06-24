import os
cwd = os.getcwd()

show_all_tables = "SHOW TABLES;"

dof_parking_violation_codes_path = os.path.join(cwd, 'data', 'dof_parking_violation_codes.csv')
import_violation_code_csv = f'''
CREATE OR REPLACE TABLE parking_violation_codes AS
SELECT * 
FROM read_csv_auto(
    '{dof_parking_violation_codes_path}',
    normalize_names=True
    )
'''

parking_violations_issued_fiscal_year_2023_sample_path = os.path.join(cwd, 'data', 'parking_violations_issued_fiscal_year_2023_sample.csv')
import_parking_violations_2023_csv = f'''
CREATE OR REPLACE TABLE parking_violations_2023 AS
SELECT *
FROM read_csv_auto(
    '{parking_violations_issued_fiscal_year_2023_sample_path}',
    normalize_names=True
    )
'''