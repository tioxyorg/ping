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
