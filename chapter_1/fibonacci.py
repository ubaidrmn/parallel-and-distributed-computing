import threading
import time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)


def timed_fibonacci(n, thread_num):
    start_time = time.time()
    result = calc_fibonacci(n)
    end_time = time.time()
    print(f"Thread {thread_num} finished calculating Fibonacci({n}) = {result} in {end_time - start_time:.4f} seconds.")

threads = []
n = 10  


overall_start_time = time.time()

for i in range(9):  
    t = threading.Thread(target=timed_fibonacci, args=(n, i + 1))
    threads.append(t)
    
    print(f"Starting thread {i + 1}")
    t.start()

for t in threads:
    t.join()


overall_end_time = time.time()
print(f"All threads have finished. Total execution time: {overall_end_time - overall_start_time:.4f} seconds.")
