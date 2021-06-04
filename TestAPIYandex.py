#import pytest
import unittest
from main import YaUploader

token_ya = 'yandex_token'
ya = YaUploader(token_ya)


class TestAPIYandex(unittest.TestCase):

    def SetUp(self):
        print('method setUp')

    #200, OK, все верно
    def test_api_yandex_OK(self):
        self.assertEqual(ya.new_folder(), 200)

    #401, Unauthorized, неправильный токен
    def test_api_yandex_Unauthorized(self):
        self.assertEqual(ya.new_folder(), 401)

    #404, Not Found, ошибка в - new_folder_url
    def test_api_yandex_Not_Found(self):
        self.assertEqual(ya.new_folder(), 404)

    def tearDown(self):
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()

