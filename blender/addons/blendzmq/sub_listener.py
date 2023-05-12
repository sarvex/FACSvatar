# CC0
# Stef van der Struijk

import sys
import zmq


def main(ip="127.0.0.1"):
    # ZMQ connection
    url = f"tcp://{ip}:5550"
    ctx = zmq.Context()
    socket = ctx.socket(zmq.SUB)
    socket.connect(url)  # subscriber creates ZeroMQ socket
    socket.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))  # any topic
    print(f"Sub bound to: {url}\nWaiting for data...")

    while True:
        # wait for publisher data
        topic, msg = socket.recv_multipart()
        print(f"On topic {topic}, received data: {msg}")


if __name__ == "__main__":
    # pass ip argument
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
