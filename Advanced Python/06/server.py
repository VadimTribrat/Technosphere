import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import socket
import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup



mutex = threading.Lock()
PROCESSED_URLS = 0


def server(workers, k):
    sock = socket.socket()
    sock.bind(('localhost', 12345))
    sock.listen(15)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        while True:
            client, addr = sock.accept()
            pool.submit(parser, client, k)


def parser(client, k):
    url = client.recv(4096)
    with urlopen(url.decode("utf-8")) as page:
        html = page.read()
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)
    words = Counter(text.split()).most_common(k)
    client.send(json.dumps(words, indent=4).encode())
    with mutex:
        global PROCESSED_URLS
        PROCESSED_URLS += 1
        print(PROCESSED_URLS)


if __name__ == "__main__":
    args = sys.argv
    works = int(args[args.index('-w') + 1])
    top = int(args[args.index('-k') + 1])
    p1 = multiprocessing.Process(target=server, args=[works, top])
    p1.start()
    p1.join()
