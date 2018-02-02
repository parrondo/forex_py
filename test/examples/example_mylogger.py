#!/usr/bin/env python
import os
import sys

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

from frxpy.utils.mylogger import MyLogger

m = MyLogger('loggingggg')
logger = m.get_logger()
logger.info('hello')
m.push('--->')
logger.info('hello222')
m.clean()
m.push('--->')
logger.info('hello333')
m.pop()
logger.info('hello444')


