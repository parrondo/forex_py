#!/usr/bin/env python
# -*- coding: utf-8 -*-

import frxpy.data.csv
from frxpy.utils.mylogger import MyLogger


def whitening(data):
    logger = MyLogger('whitening')        

def check_consistency(data):
    logger = MyLogger('check_consistency')    
    pass

def csv2hdf5(files):
    '''convert csv files to hdf5.
    When creating key in hdf5, this function use filename of inputs, and then
    sort the key. So, you don't change filename.
    '''
    logger = MyLogger('csv2hdf5')

def csv2json(data):
    logger = MyLogger('csv2json')
    
    pass
