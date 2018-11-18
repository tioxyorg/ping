import ping
import unittest2 as unittest


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = ping.app.test_client()
        self.app.testing = True

    def test_health_page(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_hello_message_tracer(self):
        response = self.app.get('/hello/Tracer')
        self.assertEqual(
            response.json,
            {'message': 'Hello Tracer'},
        )

    def test_hello_message_tdc(self):
        response = self.app.get('/hello/TDC')
        self.assertEqual(
            response.json,
            {'message': 'Hello TDC'},
        )


if __name__ == '__main__':
    unittest.main()
