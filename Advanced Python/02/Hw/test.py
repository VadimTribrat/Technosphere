import unittest
from unittest.mock import patch
from myparser import parser_html


class TestClass(unittest.TestCase):
    @patch("myparser.parser_html.open_tag_callback", return_value=None)
    @patch("myparser.parser_html.data_callback", return_value=None)
    @patch("myparser.parser_html.close_tag_callback", return_value=None)
    def test_1(self, f1, f2, f3):
        test_html = r'''
        <!DOCTYPE html>

        <html lang="ru">
        <head>

        <meta charset="UTF-8">

        <title> Пример простой страницы html</title>
        </head>

        <body>

        Пример простой страницы - для того, чтобы посмотреть код, нажмите ctrl + U
        </body>

        </html>
        '''
        parser_html(test_html, f1, f2, f3)
        print(f1.call_count)       
        self.assertEqual(f1.call_count, 6)
        self.assertEqual(f2.call_count, 2)
        self.assertEqual(f3.call_count, 4)

    def test_2(self):
        test_html = r'''
        <!DOCTYPE html>

        <html lang="ru">
        <head>

        <meta charset="UTF-8">

        <title> Пример простой страницы html</title>
        </head>

        <body>

        Пример простой страницы - для того, чтобы посмотреть код, нажмите ctrl + U
        </body>

        </html>
        '''
        f1 = lambda x: print("Open tag:", x)
        f2 = lambda x: print("Data:", x)
        f3 = lambda x: print("Close tag:", x)
        parser_html(test_html, f1, f2, f3)

if __name__ == "__main__":
    unittest.main()
    #print(dir(parser_html))
