#!/usr/bin/env python
# -*- cofing:utf-8 -*-

import resource

class MemManager:
    """
    MemManager provides a setting for the limit of memory.
    """
    def __init__(self, maxsize=2):
        self._setLimitMemory(maxsize)

    def _setLimitMemory(self):
        """
        argments
        :maxsize: 2GB (default)
        """
        self.maxsize = 1024 * 1024 * 1024 * maxsize
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS, (self.maxsize, hard))
        print('Set Memoy Limit\t:\t{}Gb;'.format(maxsize))
        
