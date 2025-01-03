from concurrent.futures import ThreadPoolExecutor
def cube (number):
    return number ** 3
numbers = [2, 4, 6, 8]
# Create a thread pool executor
executor = ThreadPoolExecutor (max_workers=2)
# Submit a single task
future = executor.submit(cube, 3)
print("Single Task Result:", future.result()) # Output: 27
# Use map to process multiple tasks
results = executor.map(cube, numbers)
print("Mapped Results:", list(results)) # Output: [8, 64, 216, 512]
# Shutdown the executor
executor.shutdown()
print("Executor Shut Down.")
