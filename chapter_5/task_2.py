
import time
import concurrent.futures
# Task function: Simulate a heavy computation 
def count (number):
    for _ in range(100_000_000):
        pass
    return number * 100_000_000
# Evaluation function
def evaluate(item):
    result = count(item)
    print (f"Item {item}, result {result}")
# List of numbers to process 
number_list = [1, 2, 3, 4, 5]
# Sequential Execution 
start_time = time.time() 
for item in number_list:
    evaluate(item)
print (f"Sequential Execution: {time.time() - start_time:.2f} seconds")
# Thread Pool Execution
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: 
    for item in number_list:
        executor.submit(evaluate, item)
print (f"Thread Pool Execution: {time.time() - start_time:.2f} seconds")
# Process Pool Execution
start_time = time.time()
with concurrent.futures. ProcessPoolExecutor (max_workers=5) as executor: 
    for item in number_list:
        executor.submit (evaluate, item)
print (f"Process Pool Execution: {time.time() - start_time:.2f} seconds")
