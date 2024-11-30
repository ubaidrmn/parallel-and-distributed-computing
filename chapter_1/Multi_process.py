
import time
import multiprocessing
import threading
import random

def do_something(count,out_list):
   for i in range(count):
       out_list.append(random.random())
if __name__ == "__main__":
    size = 20000
    process = 10
    jobs = []

    # Multiprocessing
    start_time = time.time()
    out_list = []
    for i in range(process):
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)
        process.start()

    for j in jobs:
        j.join()

    print("Multiprocessing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # Reset job list for threading
    jobs = []
    threads = 10
    out_list = []
    start_time = time.time()
    for i in range(threads):
        thread = threading.Thread(target=do_something, args=(size, out_list))  # Corrected to pass the function reference
        jobs.append(thread)
        thread.start()

    for j in jobs:
        j.join()

    print("Thread processing complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
