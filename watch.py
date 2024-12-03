import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class SolutionHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        self.run_solution()

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.file_path:
            self.run_solution()

    def run_solution(self):
        print("\n" + "="*50)
        print(f"Running solution at {time.strftime('%H:%M:%S')}")
        print("="*50)
        try:
            subprocess.run([sys.executable, self.file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running solution: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python watch.py solutions/day_X.py")
        sys.exit(1)

    path = os.path.abspath(sys.argv[1])
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)

    print(f"Watching {path}")
    event_handler = SolutionHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
