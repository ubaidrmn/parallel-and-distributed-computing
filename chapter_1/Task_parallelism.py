from concurrent.futures import ThreadPoolExecutor
import time

def task_1():
    print("Task 1 executed")

def task_2():
    print("Task 2 executed")

# Measure the start time
start_time = time.time()

# Using ThreadPoolExecutor to run tasks concurrently
with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)
    future2 = executor.submit(task_2)

# Measure the end time
end_time = time.time()

# Print the execution time
print(f"Execution time: {end_time - start_time:.5f} seconds")
