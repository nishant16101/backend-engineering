import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:8000/tasks/3/increment-priority-locked"

def send_request():
    response = requests.post(URL)
    print(
        response.status_code,
        response.json()
    )
    return response

def main():
    number_of_requests = 10
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request) for _ in range(number_of_requests)]
        for future in futures:
            future.result()

if __name__ =="__main__":
    main()

