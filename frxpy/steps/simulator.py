#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sacred import Experiment
from sacred.observers import FileStorageObserver

ex = Experiment('simulate')
exp_path = str((EXP_ROOT_PATH / 'simulate').resolve())
ex.observers.append(FileStorageObserver.create(exp_path))


@ex.config
def config():
    pass

@ex.automain
def main():
    pass

