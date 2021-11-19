import datetime
import shutil
import os
import unittest

import transact

STORAGE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "storage")
INPUT = os.path.join(STORAGE, "input")
OUTPUT = os.path.join(STORAGE, "output")

class TestTransact(unittest.TestCase):
    def setUp(self):
        # set file
        self.sample_text = "This is sample from test_transact.py"
        self.filename = "text" + datetime.datetime.now().strftime("%m%d%H%M") + ".txt"

    def tearDown(self):
        # delete file
        for path in [os.path.join(INPUT, self.filename), os.path.join(OUTPUT, self.filename)]:
            if os.path.exists(path):
                os.remove(path)
        
    def test_save_input_NR001(self):
        self.assertEqual(transact.save_input(self.sample_text), self.filename)

    def test_save_input_NR002(self):
        path = os.path.join(INPUT, self.filename)
        transact.save_input(self.sample_text)
        self.assertTrue(os.path.exists(path))

    def test_load_input_NR001(self):
        transact.save_input(self.sample_text)
        self.assertEqual(transact.load_input(self.filename), self.sample_text)
        
    def test_load_input_ABNR001(self):
        with self.assertRaises(ValueError):
            transact.load_input("randompath755486")

    def test_save_output_NP001(self):
        path = os.path.join(OUTPUT, self.filename)
        transact.save_output(self.sample_text, self.filename)
        self.assertTrue(os.path.exists(path))

    def test_load_output_NR001(self):
        transact.save_output(self.sample_text, self.filename)
        self.assertEqual(transact.load_output(self.filename), self.sample_text)
    
    def test_load_output_ABNR001(self):
        with self.assertRaises(ValueError):
            transact.load_output("randompath235489")
        
    def test_check_output_NR001(self):
        transact.save_output(self.sample_text, self.filename)
        self.assertTrue(transact.check_output(self.filename))


if __name__ == "__main__":
    unittest.main()
    

        



