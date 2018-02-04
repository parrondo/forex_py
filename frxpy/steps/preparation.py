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
logger = MyLogger(Path(__file__).name).get_logger()


@ex.config
def config():
    workdir = ''
    data = '' # data is csv files
    
    d_type = 'hdf5'
    data_shape = ''
    input_files = []
    whitening = True

    ### check arguments ###
    assert data_convert_type in ['hdf5'], \
        "data_convert_type in ['hdf5', 'json', 'leveldb', 'protobuf']"
    assert workdir, 'workdir is required: ' \
        '"[prog] with workdir=/path/to/your/dir"'
    ### End check arguments ###

    def setup(workdir):
        workdir = Path(workdir)
        logdir = workdir / 'log'
        ex.observers.append(FileStorageObserver.create(logdir))
    setup(workdir)

    
@ex.automain
def run(d_type, data_shape, output_datapath, input_files):
    pass
