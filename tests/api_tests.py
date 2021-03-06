from app.server import app
import unittest
import random
import string
import json
import os

flask_app = app.app
user = ''.join(random.choices(
    string.ascii_uppercase + string.ascii_lowercase, k=6))  # create a random user for tests


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True
        self.test_user = user

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

    def test_set_global_data(self):
        # insert normal data
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        input_data = {
            "name": f"globalKey_{random_string}",
            "value": f"globalValue_{random_string}"
        }
        response = self.app.post(
            '/api/setGlobalData', json=input_data)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['has_error'], False)
        self.assertEqual(data['message'], "Data submitted")

        # insert the existed data
        response = self.app.post(
            '/api/setGlobalData', json=input_data)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['has_error'], False)
        self.assertEqual(data['message'], "Data updated")

        # insert wrong data
        input_data = {
            "wrongname": "globalKey",
            "wrongvalue": "globalValue"
        }
        response = self.app.post(
            '/api/setGlobalData', json=input_data)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['has_error'], True)

    def test_upload_file(self):
        # insert normal data
        data = {
            "file": open("tests/files/sample.jpg", 'rb')
        }
        response = self.app.post(
            f'/api/upload/{self.test_user}', data=data, content_type='multipart/form-data')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['has_error'], False)
        self.assertEqual(data['message'], "File successfully uploaded")

        # insert unacceptable file type
        data = {
            "file": open("tests/files/sample.svg", 'rb')
        }
        response = self.app.post(
            f'/api/upload/{self.test_user}', data=data, content_type='multipart/form-data')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['has_error'], True)
        self.assertIn("Allowed file types are", data['message'])

    def test_download_file(self):
        # before testing download we upload a file then download it
        # insert normal data
        data = {
            "file": open("tests/files/sample.jpg", 'rb')
        }
        response = self.app.post(
            f'/api/upload/{self.test_user}', data=data, content_type='multipart/form-data')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)

        # download uploaded file
        response = self.app.get(
            f'/api/download/{self.test_user}/tests_files_sample.jpg')
        self.assertEqual(response.status_code, 200)
        response.close()  # close it cause of ResourceWarning

        # wrong file to download
        response = self.app.get(
            f'/api/download/{self.test_user}/wrong_file.jpg')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['has_error'], True)
        self.assertIn("File Not found", data['message'])

    def test_get_all(self):
        response = self.app.get(f'/api/getUserData/{self.test_user}')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['has_error'], False)


if __name__ == '__main__':
    unittest.main()
