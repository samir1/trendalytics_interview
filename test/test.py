import unittest
import requests
import json


class TestApi(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://0.0.0.0')
        self.assertEqual(response.status_code, 200)

    def test_predict_cat(self):
        url = 'http://0.0.0.0/predict'
        files = {'image': open('test/cat.jpg', 'rb')}
        response = requests.post(url, files=files)
        self.assertEqual(response.json(),
                         {"label": "Cat", "probability": 0.0, "success": True})

    def test_predict_dog(self):
        url = 'http://0.0.0.0/predict'
        files = {'image': open('test/dog.jpg', 'rb')}
        response = requests.post(url, files=files)
        self.assertEqual(response.json(),
                         {"label": "Dog", "probability": 0.9999780654907227, "success": True})


if __name__ == "__main__":
    unittest.main()

