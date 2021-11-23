import unittest

import tensorflow as tf

import models

class TestRinna(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = models.Rinna()
        cls.model.load()
    
    @classmethod
    def tearDownClass(cls):
        del cls.model

    def test_generate(self):
        sample_text = "私はりんなです。"
        input_tensor = self.model.tokenize(sample_text)
        output_tensor = self.model.generate(input_tensor, output_size=20)
        self.assertEqual(output_tensor.numpy().shape[1], 20)

    def test_tokenize(self):
        sample_text = "私はりんなです。"
        expected_array = [9, 6057, 7670, 57, 2767, 8, 2]

        tensor = self.model.tokenize(sample_text)
        self.assertTrue(all(tensor.numpy()[0] == expected_array))

    def test_decode(self):
        sample_tensor = tf.constant([[9, 6057, 7670, 57, 2767, 8]])
        expected_text = "私はりんなです。"
        
        text = self.model.decode(sample_tensor)
        self.assertEqual(text, expected_text)