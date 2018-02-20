#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from sacred import Experiment
from sacred.observers import FileStorageObserver

from frxpy.utils.mylogger import MyLogger
from frxpy.data.preprocess import csv2hdf5
from frxpy.data.preprocess import csv2json

ex = Experiment('preprocess')
ex.logger =  MyLogger('preprocess').get_logger()

@ex.config
def config():
    workdir = ''
    datadir = '' # datadir contains csv files.
    
    output_data_type = 'hdf5'
    data_shape = ''

    whitening = True

    ### check arguments ###
    assert output_data_type in ['hdf5'], \
        "data_convert_type in ['hdf5', 'json', 'leveldb', 'protobuf']"
    assert workdir, 'workdir is required: ' \
        '"[prog] with workdir=/path/to/your/dir"'
    assert datadir, 'datadir is required: '
    
    ### End check arguments ###
    
    ### preprocess ###
    workdir = str(Path(workdir).resolve())
    ### End preprocess ###

    def setup(workdir):
        workdir = Path(workdir)
        logdir = workdir / 'log'
        ex.observers.append(FileStorageObserver.create(logdir))
    setup(workdir)

@ex.capture    
def get_csvs(_log, datadir:str):
    parent_path = Path(datadir)
    inputs_keyward = '*.csv'
    _log.info(parent_path)    
    _log.info(inputs_keyward)
    _inputs = [str(i) for i in list(Path(parent_path).glob(inputs_keyward))]
    return _inputs

@ex.automain
def run(_log, workdir, output_data_type, data_shape):
    workdir = str(Path(workdir).resolve())
    inputs = get_csvs()
    _log.info(f'output data type is [ {output_data_type} ].')
    _log.info(f'workdir is [ {workdir} ].')
    _log.info(f'inputs are {inputs}.')    
    csv2hdf5(inputs)
