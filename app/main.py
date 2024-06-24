# tar -czf myfolder.tar.gz dbt-project/*

import requests
import duckdb
# import pandas as pd
from sql_querries import show_all_tables, import_violation_code_csv, import_parking_violations_2023_csv;
import os

parent_dir = os.getcwd()
db_path = os.path.join(parent_dir, "data/nyc_parking_violations.db")


with duckdb.connect(db_path) as connection:
    connection.sql(show_all_tables).show()

# with duckdb.connect(db_path) as connection:
#     connection.sql(import_violation_code_csv)
#     connection.sql("SELECT * FROM parking_violation_codes LIMIT 5;").show()

# with duckdb.connect(db_path) as connection:
#     connection.sql(import_parking_violations_2023_csv)
#     connection.sql("SELECT * FROM parking_violations_2023 LIMIT 5;").show()

# with duckdb.connect(db_path) as connection:
#     connection.sql("SELECT * FROM ref_model").show()

with duckdb.connect(db_path) as connection:

    # connection.sql("SELECT * FROM bronze_parking_violation_codes LIMIT 5").show()
    # connection.sql("SELECT * FROM silver_parking_violation_codes LIMIT 5").show()
    # connection.sql("SELECT * FROM gold_ticket_metrics LIMIT 5").show()
    # connection.sql("SELECT * FROM gold_vehicle_metrics LIMIT 5").show()
    connection.sql('select * from "nyc_parking_violations"."main_dbt_test__audit"."violation_codes_revenue"').show()


# make production database for deployment
prod_db_path = os.path.join(parent_dir, "data/prod_nyc_parking_violations.db")

with duckdb.connect(prod_db_path) as connection:
    connection.sql(import_parking_violations_2023_csv)
    connection.sql(import_violation_code_csv)
    connection.sql(show_all_tables).show()