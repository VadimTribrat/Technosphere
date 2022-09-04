import unittest
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
from server import server
from client import client


class TestClass(unittest.TestCase):
    def test_server(self):
        p1 = multiprocessing.Process(target=server, args=[5, 10])
        p1.start()
        time.sleep(3)
        p1.terminate()

    def test_interaction(self):
        p1 = multiprocessing.Process(target=server, args=[7, 3])
        p1.start()
        futures = []
        with ThreadPoolExecutor(max_workers=3) as pool:
            with open("urlst.txt", 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip('\n')
                    if line == '':
                        continue
                    future = pool.submit(client, line.lstrip('\n'))
                    futures.append(future)
        for val in futures:
            val.result()
        p1.terminate()


if __name__ == "__main__":
    unittest.main()
