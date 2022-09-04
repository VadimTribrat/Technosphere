import unittest
import asyncio
import time
from main import crawl


class TestClass(unittest.TestCase):
    def test_server(self):
        start = time.time()
        asyncio.get_event_loop().run_until_complete(crawl("urlst.txt", 3000))
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    unittest.main()
