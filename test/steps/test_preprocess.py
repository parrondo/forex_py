#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from frxpy.steps.preprocess import get_inputs

class TestPreprocess(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_inputs(self):
        assert False, (get_inputs('test.csv'))

if __name__ == '__main__':
    unittest.run()
    
