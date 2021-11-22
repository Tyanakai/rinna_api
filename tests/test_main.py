import unittest

from fastapi.testclient import TestClient

import main
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):
    def test_upload_input_NR001(self):
        response = client.post("/upload", json={"text" : "test upload input NR001"})
        self.assertTrue(response.json()["filename"][-4:]==".txt")

    def test_prediction_NR001(self):
        response = client.post("/upload", json={"text" : "test predict NR001"})
        filename = response.json()["filename"]
        self.assertEqual(main.prediction(filename, output_size=20), {"output was saved"})

if __name__=="__main__":
    unittest.main()


