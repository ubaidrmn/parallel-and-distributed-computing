from multiprocessing import Process
import time

def print_square(num):
    start_time = time.time()  # Start time for the square calculation
    print(f"Square: {num * num}")
    end_time = time.time()  # End time for the square calculation
    print(f"Execution time for square: {end_time - start_time} seconds")

def print_cube(num):
    start_time = time.time()  # Start time for the cube calculation
    print(f"Cube: {num * num * num}")
    end_time = time.time()  # End time for the cube calculation
    print(f"Execution time for cube: {end_time - start_time} seconds")

if __name__ == '__main__':
    p1 = Process(target=print_square, args=(10,))
    p2 = Process(target=print_cube, args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Processes finished executing")
