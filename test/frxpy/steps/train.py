#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sacred import Experiment
from sacred.observers import FileStorageObserver

ex = Experiment('train')
ex.observers.append(FileStorageObserver.create('train'))


@ex.config
def config():
    pass

@ex.automain
def main():
    pass
