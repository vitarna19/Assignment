import pandas as pd

def extract_data():
    # Read data from local CSV
    df = pd.read_csv(r'C:/python codes/Celebal Intership/week 6 assignment/task 1/local_data.csv')
    print("Data extracted from local CSV:")
    print(df)
    return df

if __name__ == "__main__":
    extract_data()
