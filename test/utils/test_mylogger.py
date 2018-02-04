import os
import sys
import inspect
import unittest
from pathlib import Path
from contextlib import contextmanager
from io import StringIO
from logging import getLogger, StreamHandler, INFO, Formatter


from frxpy.utils.mylogger import MyLogger

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


class TestMyLogger(unittest.TestCase):
    def setUp(self):
       self.l = MyLogger('Name', output=StringIO)
       
    def test_logger(self):
        print('errro')

    def test_get_logger_default_format(self):
        pass
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
            
