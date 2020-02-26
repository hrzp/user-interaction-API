from app.server import app
import unittest
import json


flask_app = app.app


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_app(self):
        """
        Test the app structure
        """
        # by default the Swagger UI is enabled
        swagger_ui = self.app.get('/api/ui/')  # type: flask.Response
        assert swagger_ui.status_code == 200
        assert b"Swagger UI" in swagger_ui.data

    def set_user_data(self):
        pass

    def get_all(self):
        response = self.app.get('/api/getUserData/user1')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['has_error'], False)


if __name__ == '__main__':
    unittest.main()
