import threading
import time


sem = threading.Semaphore(2) 

def access_resource(thread_name):
    start_time = time.time()  
    sem.acquire()  
    print(f"{thread_name} accessing the resource")
    time.sleep(2)  
    print(f"{thread_name} done")
    sem.release()  
    end_time = time.time() 
    print(f"Execution time for {thread_name}: {end_time - start_time} seconds")


threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads finished executing")
