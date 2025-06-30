import schedule
import time
from datetime import datetime

def run_pipeline():
    print(f"⏰ Pipeline triggered at {datetime.now()}")
    # Simulate a pipeline step like logging or saving a file
    with open("schedule_log.txt", "a") as f:
        f.write(f"Pipeline ran at {datetime.now()}\n")

# Schedule the job to run every 1 minute
schedule.every(10).minutes.do(run_pipeline)

print("🔁 Schedule-based trigger started. Waiting for pipeline runs...")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)
