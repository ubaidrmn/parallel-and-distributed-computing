from multiprocessing import Process, Pipe

def child_process(child_conn):
    # Receive data from the parent
    received_data = child_conn.recv()
    print(f"Child received: {received_data}")

    # Process the data (for example, make it uppercase)
    processed_data = received_data.upper()

    # Send the processed data back to the parent
    child_conn.send(processed_data)
    child_conn.close()

if __name__ == '__main__':
    # Create a Pipe
    parent_conn, child_conn = Pipe()

    # Create a child process, passing the child end of the pipe
    p = Process(target=child_process, args=(child_conn,))

    # Start the child process
    p.start()

    # Parent process sends data
    data_to_send = "hello from parent"
    print(f"Parent sending: {data_to_send}")
    parent_conn.send(data_to_send)

    # Parent process receives the response from the child
    response = parent_conn.recv()
    print(f"Parent received: {response}")

    # Wait for the child process to finish
    p.join()
    print("Parent and child processes finished")
