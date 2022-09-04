from concurrent.futures import ThreadPoolExecutor
import socket
import json
import sys
from textwrap import indent


def client(url):
    sock = socket.socket()
    sock.connect(('localhost', 12345))
    sock.sendall(url.encode())
    data = sock.recv(1024)
    data = json.loads(data.decode())
    sock.close()
    print(url)
    print(data)


if __name__ == "__main__":
    argv = sys.argv
    file = argv[-1] if '.txt' in argv[-1] else argv[-2]
    workers = int(argv[-1]) if argv[-1].isdigit() else int(argv[-2])
    futures = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n')
                if line == '':
                    continue
                future = pool.submit(client, line.lstrip('\n'))
                futures.append(future)
        for val in futures:
            val.result()
