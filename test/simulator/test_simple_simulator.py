# -*- coding: utf-8 -*-
import os
import unittest
from contextlib import contextmanager

from frxpy.simulator.simple_simulator import Simulator


class TestSimulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_path = os.path.join(os.path.dirname(__file__), '../data/')
        cls.s = Simulator()
    
    def test_load_data_csv(self):
        from frxpy.data.csv import CSV
        c = CSV(self.data_path + 'test_USDJPY_M1_2000.csv')
        self.assertEqual('CSV', self.s.load_data(c))

        
        
        
        
