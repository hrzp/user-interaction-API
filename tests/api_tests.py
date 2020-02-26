from app.server import app
import unittest
import random
import string
import json


flask_app = app.app


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True
        self.test_user = ''.join(random.choices(
            string.ascii_uppercase + string.ascii_lowercase, k=6))  # create a random user for tests

    def test_app(self):
        """
        Test the app structure
        """
        # by default the Swagger UI is enabled
        swagger_ui = self.app.get('/api/ui/')  # type: flask.Response
        assert swagger_ui.status_code == 200
        assert b"Swagger UI" in swagger_ui.data

    def test_set_user_data(self):
        # insert normal data
        input_data = {
            "name": "keyOfUser",
            "value": "valueOfUser"
        }
        response = self.app.post(
            f'/api/setUserData/{self.test_user}', json=input_data)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['has_error'], False)
        self.assertEqual(data['message'], "Data submitted")

        # insert the existed data
        response = self.app.post(
            f'/api/setUserData/{self.test_user}', json=input_data)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['has_error'], False)
        self.assertEqual(data['message'], "Data updated")

        # insert wrong data
        input_data = {
            "wrongname": "keyOfUser",
            "wrongvalue": "valueOfUser"
        }
        response = self.app.post(
            f'/api/setUserData/{self.test_user}', json=input_data)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['has_error'], True)

    def test_get_all(self):
        response = self.app.get(f'/api/getUserData/{self.test_user}')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['has_error'], False)


if __name__ == '__main__':
    unittest.main()
