import os
import sys
import unittest
from io import StringIO
from contextlib import contextmanager

from frxpy.fileio.csvfile import CSV

@contextmanager
def captured_output():
    """
    https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
    """
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestCSV(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_path = os.path.join(os.path.dirname(__file__), '../data/')
        cls.c = CSV(cls.data_path + 'test_USDJPY_M1_2000.csv')
        cls.c.load()

    def test___len__(self):
        self.assertEqual(100, len(self.c))        
        
    def test___getitem__(self):
        self.assertEqual([959709480, 106.6, 106.6, 106.6, 106.6, 0.0], self.c[0])

    @unittest.expectedFailure
    def test___getitem__indexerror(self):
        self.c[101]

        
    def test_info(self):
        ans_txt = '\
        file: {}\n\
        load: {}\n\
        size: ({:6d},{:2d})\n\
        '.format(self.data_path + 'test_USDJPY_M1_2000.csv', True, 100, 6)
        with captured_output() as (out, err):
            self.c.info()
            out.getvalue()
            self.assertEqual(out.getvalue().strip(), ans_txt.strip())

    def test_dump_npz(self):
        import numpy as np
        self.c.dump_npy(self.data_path + 'test.npy')
        test = np.load(self.data_path + 'test.npy')
        ans_array = np.array([9.59709480e+08, 1.06600000e+02, 1.06600000e+02,
                              1.06600000e+02, 1.06600000e+02, 0.00000000e+00])
        np.testing.assert_array_equal(test[0], ans_array)
        os.remove(self.data_path + 'test.npy')            
    
    def test_convert_daytime_to_seconds(self):
        self.assertEqual(1183766401,
                         self.c.convert_daytime_to_seconds('20070707 000001'))
        ## TODO: add limit test
        
    def test_convert_seconds_to_daytime(self):
        self.assertEqual(self.c.convert_seconds_to_daytime(1183766401)
                         ,'20070707 000001')
        ## TODO: add limit test
        
    def test_size(self):
        self.assertEqual(self.c.size(), (100, 6))

    def test_iter(self):
        self.c.reload()
        self.assertEqual(next(self.c), [959709480, 106.6, 106.6, 106.6, 106.6, 0.0])

    def test_dump_tinydb(self):
        self.c.dump_tinydb(self.data_path + 'test.json')
        import json
        with open(self.data_path + 'test.json') as fp:
            j = json.load(fp)
            b = []
            for i in j['_default']['1']:
                b.append(j['_default']['1'][i])
            self.assertEqual(self.c[0], b)
        os.remove(self.data_path + 'test.json')            
        
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
            
