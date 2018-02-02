#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from sacred import Experiment
from sacred.observers import FileStorageObserver

from frxpy.data.preparation import preparation
from frxpy.data.preparation import check_consistency
from frxpy.data.preparation import csv2hdf5
from frxpy.data.preparation import csv2json

ex = Experiment('preparation')
exp = Path('preparation').parent.parent
ex.observers.append(FileStorageObserver.create(exp))

@ex.config
def config():
    data_convert_type = 'hdf5'
    data_shape = ''
    output_datapath = ''
    input_files = []

    whitening = True
    assert data_convert_type in ['hdf5'], \
        "data_convert_type in ['hdf5', 'json', 'leveldb', 'protobuf']"
    
@ex.automain
def run(data_convert_type, data_shape, output_datapath, input_files):
    assert input_files
