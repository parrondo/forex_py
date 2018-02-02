import os
import unittest
from contextlib import contextmanager
from frxpy.dnn.predictor import Predictor

import frxpy.utils.basic_checker as b

class TestPredictor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test__check_class_path(self):
        class_path = 'frxpy/dnn/th/models/nn.NNH500'
        module_path, class_name = b._check_class_path(class_path)
        self.assertEqual('frxpy.dnn.th.models.nn', module_path)
        self.assertEqual('NNH500', class_name)        

    def test__check_class_path2(self):
        class_path = 'frxpy/dnn/th.models.nn.NNH500'
        module_path, class_name = b._check_class_path(class_path)
        self.assertEqual('frxpy.dnn.th.models.nn', module_path)
        self.assertEqual('NNH500', class_name)        

