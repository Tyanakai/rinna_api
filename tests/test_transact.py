import datetime
import os
import unittest

import schemas
import transact

STORAGE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "storage")
INPUT = os.path.join(STORAGE, "input")
OUTPUT = os.path.join(STORAGE, "output")

class TestTransact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # set sample
        cls.sample_text = "transact.pyのテスト"
        cls.sample_input = schemas.Input(text=cls.sample_text)
        cls.filename = "text" + datetime.datetime.now().strftime("%m%d%H%M") + ".txt"

    @classmethod
    def tearDownClass(cls):
        del cls.sample_text, cls.sample_input, cls.filename
        
    def test_save_input_NR001(self):
        self.assertEqual(transact.save_input(self.sample_input), self.filename)

    def test_save_input_NR002(self):
        path = os.path.join(INPUT, self.filename)
        transact.save_input(self.sample_input)
        self.assertTrue(os.path.exists(path))

    def test_load_input_NR001(self):
        transact.save_input(self.sample_input)
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

        



