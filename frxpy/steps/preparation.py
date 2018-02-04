#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from sacred import Experiment
from sacred.observers import FileStorageObserver

from frxpy.utils.mylogger import MyLogger
from frxpy.data.preparation import check_consistency
from frxpy.data.preparation import csv2hdf5
from frxpy.data.preparation import csv2json

ex = Experiment('preparation')


@ex.config
def config():
    workdir = ''
    inputs = ''
    data = '' # data is csv files
    
    output_data_type = 'hdf5'
    data_shape = ''
    inputs = []
    whitening = True

    ### check arguments ###
    assert output_data_type in ['hdf5'], \
        "data_convert_type in ['hdf5', 'json', 'leveldb', 'protobuf']"
    assert workdir, 'workdir is required: ' \
        '"[prog] with workdir=/path/to/your/dir"'
    assert inputs, 'inputs are required: ' \
        'inputs files'
    ### End check arguments ###

    ### preparation ###
    inputs = []
    ### End preparation ###

    def setup(workdir):
        workdir = Path(workdir)
        logdir = workdir / 'log'
        ex.observers.append(FileStorageObserver.create(logdir))
    setup(workdir)

@ex.capture    
def get_inputs(inputs):
    inputs_path = Path(inputs).parent.resolve()
    inputs_keyward = Path(inputs).name
    _inputs = [ str(i) for i in list(Path(inputs_path).glob(inputs_keyward)) ]
    del inputs_path
    del inputs_keyward
    return _inputs

@ex.automain
def run(_log, workdir, inputs, output_data_type, data_shape):
    workdir = str(Path(workdir).resolve())
    inputs = get_inputs()
    _log.info(f'output data type is [ {output_data_type} ].')
    _log.info(f'workdir is [ {workdir} ].')
    _log.info(f'inputs are {inputs}.')    

    csv2hdf5(inputs)
