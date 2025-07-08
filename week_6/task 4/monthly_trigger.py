# import datetime
# import calendar

# def is_last_saturday_of_month(date=None):
#     if date is None:
#         date = datetime.date.today()

#     # Get last day of the current month
#     last_day = calendar.monthrange(date.year, date.month)[1]
#     last_date = datetime.date(date.year, date.month, last_day)

#     # Go backward to find the last Saturday
#     while last_date.weekday() != calendar.SATURDAY:
#         last_date -= datetime.timedelta(days=1)

#     return date == last_date

# def run_pipeline():
#     print("Running pipeline... (e.g., data processing, loading, etc.)")

# def main():
#     today = datetime.date(2025, 7, 26)

#     print(f"Today: {today.strftime('%A, %d %B %Y')}")

#     if is_last_saturday_of_month(today):
#         print("Today is the LAST Saturday of the month!")
#         run_pipeline()
#     else:
#         print("Not the last Saturday. Pipeline will not run.")

# if __name__ == "__main__":
#     main()


import datetime
import calendar
import subprocess
import os

def is_last_saturday_of_month(date=None):
    if date is None:
        date = datetime.date.today()

    last_day = calendar.monthrange(date.year, date.month)[1]
    last_date = datetime.date(date.year, date.month, last_day)

    while last_date.weekday() != calendar.SATURDAY:
        last_date -= datetime.timedelta(days=1)

    return date == last_date

def run_pipeline():
    print("Running actual pipeline (incremental_loader.py)...")
    
    # Full path OR relative path to the script
    pipeline_path = os.path.abspath("task 3/incremental_loader.py")

    # Use subprocess to run it
    result = subprocess.run(["python", pipeline_path], capture_output=True, text=True)

    print("Pipeline Output:")
    print(result.stdout)

    if result.returncode != 0:
        print("Pipeline failed!")
        print(result.stderr)
    else:
        print("Pipeline ran successfully!")

def main():
    today = datetime.date(2025, 7, 26)  # <- Simulate or use datetime.date.today()
    print(f"Today: {today.strftime('%A, %d %B %Y')}")

    if is_last_saturday_of_month(today):
        print("Today is the LAST Saturday of the month!")
        run_pipeline()
    else:
        print("Not the last Saturday. Pipeline will not run.")

if __name__ == "__main__":
    main()
