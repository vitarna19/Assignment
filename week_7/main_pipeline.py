import pandas as pd
import os
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

data_dir = './data/'
output_dir = './output/'
os.makedirs(output_dir, exist_ok=True)

def extract_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        date_key = match.group(1)
        date_formatted = f"{date_key[:4]}-{date_key[4:6]}-{date_key[6:]}"
        return date_formatted, date_key
    return None, None

def process_files():
    logging.info("Starting file processing...")
    for root, _, files in os.walk(data_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            logging.info(f"Processing file: {filename}")

            if filename.startswith("CUST_MSTR"):
                date, _ = extract_date(filename)
                df = pd.read_csv(filepath)
                df['Date'] = date
                output_file = os.path.join(output_dir, f'CUST_MSTR_processed_{date}.csv')
                df.to_csv(output_file, index=False)

            elif filename.startswith("master_child_export"):
                date, date_key = extract_date(filename)
                df = pd.read_csv(filepath)
                df['Date'] = date
                df['DateKey'] = date_key
                output_file = os.path.join(output_dir, f'master_child_processed_{date}.csv')
                df.to_csv(output_file, index=False)

            elif filename.startswith("H_ECOM_ORDER"):
                df = pd.read_csv(filepath)
                output_file = os.path.join(output_dir, 'H_ECOM_ORDER_processed.csv')
                df.to_csv(output_file, index=False)

            logging.info(f"Processed and saved to: {output_file}")
    logging.info("All files processed successfully.")

if __name__ == "__main__":
    process_files()
