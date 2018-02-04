#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sacred import Experiment
from sacred.observers import FileStorageObserver

ex = Experiment('evaluation')

@ex.config
def config():
    workdir: str = ''
    # required

    def setup(workdir):
        workdir = Path(workdir)
        logdir = workdir / 'log'
        ex.observers.append(FileStorageObserver.create(logdir))
    setup(workdir)

    pass

@ex.automain
def main():
    pass
