from fastapi import BackgroundTasks
import time

def send_email(task_id:int):
    print(f"Starting email for task{task_id}")
    time.sleep(5)
    print(f"Email sent for task{task_id}")

    