#!/usr/bin/env python3
import os
import sys

cafepypath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(cafepypath)

import frxpy.fileio.csvfile as csvfile
c = csvfile.CSV('../test/data/test_USDJPY_M1_2000.csv')

c.load()

print(c[0])
print(len(c))
print(c)
c.dump_tinydb('test.json')


