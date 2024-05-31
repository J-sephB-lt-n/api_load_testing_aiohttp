import datetime
import gevent
from gevent import monkey
monkey.patch_all()
import time
import requests
from gevent.pool import Pool

# Function to make a request
def make_request(url):
    try:
        response = requests.get(url)
        print(f"{datetime.datetime.now()} URL: {url}, Status Code: {response.status_code}")
    except Exception as e:
        pass
        print(f"{datetime.datetime.now()} Error fetching {url}: {e}")

# Function to perform load testing
def load_test(url, num_requests, concurrency):
    pool = Pool(concurrency)
    jobs = [pool.spawn(make_request, url) for _ in range(num_requests)]
    gevent.joinall(jobs)

# Parameters
url = "https://test-api-pkksbrey3q-nw.a.run.app/get_task" 
num_requests = 500  # Total number of requests
concurrency = 100  # Number of concurrent requests

# Start load test
start_time = time.perf_counter()
load_test(url, num_requests, concurrency)
total_secs = time.perf_counter() - start_time
print(f"n requests per second = {num_requests/total_secs:,.2f}")
