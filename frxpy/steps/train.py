#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sacred import Experiment
from sacred.observers import FileStorageObserver

ex = Experiment('train')
ex.observers.append(FileStorageObserver.create('train'))

@ex.config
def config():
    data: str = '' 
    # required
    workdir: str = ''
    # required

    data_shape = ()
    
    batch_size = 128
    optimizer = 'torch.optim.SGD'
    optimizer_kargs = dict(
        lr = learning_rate,
        momentum = 0.09
        )
    
    ### check arguments ###
    assert datadir, f'datadir is required'
    assert workdir, f'workdir is required'
    ### END check arguments ###

    def setup(workdir):
        workdir = Path(workdir)
        logdir = workdir / 'log'
        ex.observers.append(FileStorageObserver.create(logdir))
    setup(workdir)


@ex.capure
def get_trainer():
    pass

@ex.capure
def get_iterator():
    pass

@ex.capure
def get_model():
    pass


@ex.automain
def main():
    trainer = get_trainer()
    iterator = get_iterator()
    
    pass
