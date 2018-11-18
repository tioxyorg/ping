import app
import unittest2 as unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_message(self):
        response = self.app.get('/')
        message = hello_world.wrap_html('Hello DockerCon 2018!')
        self.assertEqual(response.data, message)

if __name__ == '__main__':
    unittest.main()

import unittest2 as unittest
import requests


HOST = "http://localhost:5000"


class Sample(unittest.TestCase):
    def test_health_page(self):
        DESIRED_PATH = f"{HOST}/health"
        EXPECTED = 200

        result = requests.get(DESIRED_PATH)
        self.assertEqual(EXPECTED, result.status_code)

    def test_root_page(self):
        DESIRED_PATH = f"{HOST}/"
        EXPECTED = "pong"

        result = requests.get(DESIRED_PATH)
        self.assertEqual(EXPECTED, result.text)

    def test_user_page(self):
        USERNAME = "Genji"
        DESIRED_PATH = f"{HOST}/hello/{USERNAME}"
        EXPECTED = f"Hello {USERNAME}!"

        result = requests.get(DESIRED_PATH)
        self.assertEqual(EXPECTED, result.text)

if __name__ == "__main__":
    unittest.main()
