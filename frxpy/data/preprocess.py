# -*- coding: utf-8 -*-

import pandas as pd
from pandas import DataFrame

import frxpy.data.csv
from frxpy.utils.mylogger import MyLogger


def whitening(data):
    logger = MyLogger('whitening')        

def _read_csv(infile: str) -> DataFrame:
    logger = MyLogger('_read_csv').get_logger()
    logger.info('open: ' + infile)
    names = ['daytime', 'open', 'high', 'low', 'close', 'output']
    options = dict(
        names=names,
        delimiter=';',
    )
    df = pd.read_csv(infile,  **options)
    return df

def csv2hdf5(files, output_path='./data.hdf5'):
    '''convert csv files to hdf5.
    When creating key in hdf5, this function use filename of inputs, and then
    sort the key. So, you don't change filename.
    '''
    logger = MyLogger('csv2hdf5').get_logger()
    logger.info(files)
    datalist = []
    for ifile in files:
        datalist.append(_read_csv(ifile))
    dfs = pd.concat(datalist)
    dfs.to_hdf(output_path, key='csv')

def csv2json(data):
    logger = MyLogger('csv2json')
    pass
