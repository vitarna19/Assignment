import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

folder_to_watch = "watched_folder"
if not os.path.exists(folder_to_watch):
    os.makedirs(folder_to_watch)

# Define the actual pipeline logic
def run_pipeline(file_path):
    print(f"🚀 Running pipeline for: {file_path}")
    with open("event_log.txt", "a") as log:
        log.write(f"Pipeline triggered for {file_path} at {datetime.now()}\n")
    
    # Simulate saving file in multiple formats
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(f"{base_name}_output.csv", "w") as f:
        f.write("sample,data,from,pipeline\n1,2,3,4")

    print(f"✅ Pipeline completed for: {file_path}")

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            run_pipeline(event.src_path)

observer = Observer()
observer.schedule(FileHandler(), folder_to_watch, recursive=False)
observer.start()

print(f"👀 Watching folder: {folder_to_watch} for new files...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
