import time
import random
import os
from functools import partial

LOG_FILE = "retry_log.txt"

def fragile_task(task_name):
    """Simulates a flaky task that may randomly fail."""
    if random.random() < 0.5:
        raise Exception(f"Simulated failure in task '{task_name}'")
    print(f"{task_name} succeeded!")

def log_attempt(message):
    """Appends log to a file with timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def run_with_retry(task_func, max_retries=3, delay=5):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt} of {max_retries}...")
            log_attempt(f"Attempt {attempt} started")
            task_func()
            print("Task completed successfully.")
            log_attempt(f"Attempt {attempt} succeeded")
            break
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            log_attempt(f"Attempt {attempt} failed: {e}")

            if attempt < max_retries:
                wait_time = delay * attempt  # exponential backoff
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("All attempts failed. Exiting.")
                log_attempt("All retry attempts failed.")

if __name__ == "__main__":
    # You can change the task name here
    task_name = "Mock FTP File Download"
    
    # Use partial to pass arguments
    retryable_task = partial(fragile_task, task_name)

    # Run the task with retry logic
    run_with_retry(retryable_task, max_retries=3, delay=5)
