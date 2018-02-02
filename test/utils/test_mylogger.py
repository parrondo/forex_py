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
        logger = self.l.get_logger()
        p = Path('.')
        pathname = str(p.cwd()) + '/test/utils/test_mylogger.py'
        with captured_output() as (out, err):
            handler = StreamHandler(sys.stdout)
            formatter = Formatter(self.l._update_default_format())
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.info('test')
            ans_output = '[FILE: {:30s}] [FUNC: {:15s}] [LINE: {:4d}]: {:>20s}\n'\
                .format(pathname,
                        'test_get_logger_default_format',
                        inspect.currentframe().f_lineno-4, 'test')
            
            output = out.getvalue()
            self.assertEqual(output, ans_output)

    def test_push(self):
        self.l.push('{:10s}'.format('hello'))
        logger = self.l.get_logger()
        p = Path('.')
        pathname = str(p.cwd()) + '/test/utils/test_mylogger.py'
        with captured_output() as (out, err):
            handler = StreamHandler(sys.stdout)
            formatter = Formatter(self.l._update_default_format())
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.info('test')
            ans_output = '[FILE: {:30s}] [FUNC: {:>15s}] [LINE: {:4d}]: {:10s}{:>20s}\n'\
                .format(pathname,
                        'test_push',
                        inspect.currentframe().f_lineno-4, 'hello', 'test')
            
            output = out.getvalue()
            self.assertEqual(output, ans_output)

    def test_pop(self):
        self.l.push('{:10s}'.format('hello'))
        self.l.push('{:10s}'.format('hello'))        
        self.l.pop()
        logger = self.l.get_logger()
        p = Path('.')
        pathname = str(p.cwd()) + '/test/utils/test_mylogger.py'
        with captured_output() as (out, err):
            handler = StreamHandler(sys.stdout)
            formatter = Formatter(self.l._update_default_format())
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.info('test')
            ans_output = '[FILE: {:30s}] [FUNC: {:>15s}] [LINE: {:4d}]: {:10s}{:>20s}\n'\
                .format(pathname,
                        'test_pop',
                        inspect.currentframe().f_lineno-4, 'hello', 'test')
            
            output = out.getvalue()
            self.assertEqual(output, ans_output)

        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
            
