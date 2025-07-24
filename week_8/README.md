# NYC Taxi Dataset Assignment

## Setup Instructions

1. Create a virtual environment (optional):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the notebook:
```bash
jupyter notebook nyc_taxi_analysis.ipynb
```

### Dataset Download
The file `yellow_tripdata_2018-01.parquet` was too large for GitHub (>100MB).

Please download it manually from:
[NYC TLC Trip Data (January 2018 CSV)](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-01.csv)

To use it with this project:
1. Download the file
2. Convert it to `.parquet` (or load as CSV)
3. Place it inside: `week_8/data/`

Make sure the dataset exists in the `data/` folder as `yellow_tripdata_2018-01.parquet`.
