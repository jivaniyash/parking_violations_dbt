# Data Flow - Parking Violations -  using dbt

This repository is modified on top of [LinkedIn Course](https://github.com/LinkedInLearning/data-engineering-with-data-build-tool-dbt-4458303)

![](https://github.com/jivaniyash/parking_violations_dbt/blob/main/images/dbt-outline.png)
![](https://github.com/jivaniyash/parking_violations_dbt/blob/main/images/models.png)

## Steps to Start the App

### 1. Clone the Repository
```sh
git clone https://github.com/jivaniyash/parking_violations_dbt
cd parking_violations_dbt
```

### 2. Set up a Virtual Environment
```sh
virtualenv .venv
source venv/bin/activate
```

### 3. Install Python Requirements
```sh
pip install -r requirements.txt
```

### 4. Download datasets
Download data from Repo -
```sh
wget https://raw.githubusercontent.com/LinkedInLearning/data-engineering-with-data-build-tool-dbt-4458303/main/data/dof_parking_violation_codes.csv -P ./data/

wget https://raw.githubusercontent.com/LinkedInLearning/data-engineering-with-data-build-tool-dbt-4458303/main/data/parking_violations_issued_fiscal_year_2023_sample.csv -P ./data/
```

### 5. Run Code to import csv data into DuckDB Tables & check the output
```sh
python ./app/main.py
```

### 6. Initalize dbt project
```sh
dbt init
```
- This command will ask for name of project - `<nyc_parking_violations>`
- It will ask `Enter a number` - `<1>`
- It will create a directory `<project_name>`

Always go to dbt directory and then run following in CLI - 
`dbt debug` to check errors , `dbt compile` to check errors faster & `dbt run` to execute sql models (which creates tables)  

Add sql querries in `../models` directory
```sh
dbt docs generate
dbt docs serve # it will open a UI to explore models
```

---

### Project Information

Medallion Architecture with Materialization of each models- 
#### 1. Bronze

Raw data with just 2 csv files converted into 2 sql tables (minor )
- bronze_parking_violation_codes `view`
- bronze_parking_violations `view`

#### 2. Silver

Tranformed & Cleaned Data
- silver_violation_tickets `ephermal`
- silver_violation_vehicles `ephermal`
- silver_parking_violation_codes `view`
- silver_parking_violations `view`

#### 3. Gold

Data used to create Dashboards
- gold_ticket_metrics `table`
- gold_vehicles_metrics `table`


Make changes in `dbt-project.yml` file to add `materlizations` in each model

#### Descriptions 
You can add description of each model & its attributes. 
- `docs_blocks.md` & `schema.yml` files using jinja approach (dry-`don't repeat yourself`) in `./<project_name>/docs`

#### Run Tests

You can run tests using 2 approach
- add sql files in `./<project_name>/tests/` (Custom Singular Test)
- add `tests` attribute in `docs/schema.yml` under columns (generic-out of box test = null/not_null)
- add sql file using [jinja](https://docs.getdbt.com/guides/best-practices/writing-custom-generic-tests#generic-tests-with-default-config-values) inside `./<project_name>/tests/` & add the name of test model in `docs/schema.yml`

Add the code to show the error.
```yaml
tests:
  +store_failures: true
```

#### Production
- Run `app/main.py` to add tables to new production database
- Add `prod` in profiles.yml file 
```sh
dbt debug
dbt compile --target prod
dbt run --target prod
```