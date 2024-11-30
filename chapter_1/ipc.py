from multiprocessing import Process, Queue
import time

def producer(queue):
    start_time = time.time()  # Start time for the producer
    for i in range(5):
        queue.put(i)
        print(f"Produced {i}")
    end_time = time.time()  # End time for the producer
    print(f"Execution time for producer: {end_time - start_time} seconds")

def consumer(queue):
    start_time = time.time()  # Start time for the consumer
    while not queue.empty():
        item = queue.get()
        print(f"Consumed {item}")
    end_time = time.time()  # End time for the consumer
    print(f"Execution time for consumer: {end_time - start_time} seconds")

if __name__ == '__main__':
    queue = Queue()
    
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Producer and consumer processes finished")
