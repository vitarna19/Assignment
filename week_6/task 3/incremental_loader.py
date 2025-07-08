import pandas as pd

DATA_FILE = r"C:/python codes/Celebal Intership/week 6 assignment/task 3/data_source.csv"
WATERMARK_FILE = r"C:/python codes/Celebal Intership/week 6 assignment/task 3/last_run.txt"
TARGET_FILE = r"C:/python codes/Celebal Intership/week 6 assignment/task 3/target_data.csv"

def load_incremental_data():
    df = pd.read_csv(DATA_FILE)

    # Get last processed ID from watermark file
    with open(WATERMARK_FILE, "r") as f:
        last_id = int(f.read().strip())

    print(f"Last processed ID: {last_id}")

    # Filter rows with ID > last processed ID
    new_data = df[df['id'] > last_id]

    if new_data.empty:
        print("No new records to process.")
        return

    print("New records to load:")
    print(new_data)

    # Append to target file
    new_data.to_csv(TARGET_FILE, mode="a", index=False, header=not bool(last_id))

    # Update watermark with new max ID
    new_max_id = new_data['id'].max()
    with open(WATERMARK_FILE, "w") as f:
        f.write(str(new_max_id))

    print(f"Loaded new data. Watermark updated to ID {new_max_id}")

if __name__ == "__main__":
    load_incremental_data()
