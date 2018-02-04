import os
import sys
import unittest
from io import StringIO
from contextlib import contextmanager

from frxpy.data.csv import CSV

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
        pass

    def test___len__(self):
        pass
        
    def test___getitem__(self):
        pass

    @unittest.expectedFailure
    def test___getitem__indexerror(self):
        pass

        
    def test_info(self):
        pass

    def test_dump_npz(self):
        pass
    
    def test_convert_daytime_to_seconds(self):
        pass
        ## TODO: add limit test
        
    def test_convert_seconds_to_daytime(self):
        pass
        ## TODO: add limit test
        
    def test_size(self):
        pass

    def test_iter(self):
        pass

    def test_dump_tinydb(self):
        pass
        
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
            
