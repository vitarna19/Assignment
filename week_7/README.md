# Azure Data Lake File Processing Simulation

## Overview
This project simulates a data ingestion pipeline that processes files from a data lake container into respective tables with custom transformations.

### File Handling Logic:
1. **CUST_MSTR** files: Extract date from filename, add `Date` column, load to `CUST_MSTR` table.
2. **master_child_export** files: Extract date and datekey from filename, add `Date` and `DateKey` columns, load to `master_child` table.
3. **H_ECOM_ORDER** file: Loaded as-is to `H_ECOM_Orders` table.

### Structure:
- `data/`: Input CSV files.
- `output/`: Processed CSV files.
- `sql/`: SQL files (table creation and truncate load).
- `main_pipeline.py`: Main script to process files.

### How to Run
```bash
pip install pandas
python main_pipeline.py
```
## Future Scope
- This project can be extended to use Azure Data Factory (ADF) pipelines with Linked Services to automate ingestion into a cloud database like Azure SQL or Synapse.
- Instead of CSV, it can be extended to handle JSON and Parquet formats.

## Limitations
- This project uses local file system simulation due to lack of Azure access.
- The truncate load logic is simulated through SQL files without execution.

## Sample Command
