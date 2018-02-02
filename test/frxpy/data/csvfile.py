"""
csvfile.py
---------------

This module contains some classes which can treat csv files.


.. autoclass:: fileio.csvfile.CSV

"""

import csv
import glob
import time
import codecs
import calendar
from pytz import timezone
from datetime import datetime

import numpy as np

from frxpy.utils.basic_checker import check_file

class CSV(object):
    r"""
    CSV is a class which contains data from reading a csv file. 
    You can access csv data like a list object and also save or dump
    csv data to other database format.
    
    :param str filename: open a file name.
    :param str fmt: You specify row strcture of csv. default value is 
         [date, open, close, high, low]
    :param str bitask_fmt: choses Your CSV has bit-value and ask-value.
    :param str unit: chose ['minute', 'hour', 'day', 'week'] or int(seconds)
    :param str delimiter: specify separator of csv
    
    Usage::

        >>> import CSV
        >>> c = CSV('test.csv')
        >>> c.size()
    
        >>> s.info()
       
        >>> s.to_db('test.db')
    
    .. note::
    
        If your csv file contains no utf-8 charactor in header, remove header 
        from your file.
    
    """
    def __init__(self, filename, forex_format='ohlc', bitask_fmt='bitask',
                 daytime_format='%Y%m%d %H%M%S', delimiter=';', skip_header=False,
                 unit='minute'):
        
        self.filename = filename
        self.data = []
        self.delimiter = delimiter
        self.daytime_format = daytime_format
        self.forex_format = forex_format
        self.skip_header = skip_header
        self.unit = unit
        self.datetime = datetime(1970, 1, 1) 
        ### private menber
        self.n_row = 0
        self.n_col = 0
        self.iter_idx = 0
        
    
    def load(self):
        """
        This method can only read a csv-file which does't have header line.
        Csv data structure. ex)
        day-time, Open(BID), High(BID), Low(BID), Close(BID), \
        Open(ASK), High(ASK), Low(ASK), Close(ASK)
        """
        
        ## TODO: use self.fmt.
        ## TODO: use self.timefmt.
        ## TODO: use self.timefmt.
        if not self.data:
            ## TODO: if self.data has data, return it and give logs.
            pass
        
        with codecs.open(self.filename, 'r', 'utf-8') as f:
            reader = csv.reader(f, delimiter=self.delimiter)

            if self.skip_header:
                reader.next()
            
            for i in reader:
                s = self.convert_daytime_to_seconds(i[0])
                d = [float(j) for j in i[1:]]
                self.data.append([s, *d])

        self.n_row = len(self.data)
        self.n_col = len(self.data[0])

    def dump_npy(self, path_to_npy):
        np_data = np.asarray(self.data)
        np.save(path_to_npy, np_data)

    def dump_tinydb(self, path_to_db):
        from tinydb import TinyDB, Query
        db = TinyDB(path_to_db)
        for i in self:
            db.insert({'daytime': i[0], 'open': i[1], 'high': i[2]
                       , 'low': i[3], 'close':i[4], 'output':i[5]})
                
    def size(self):
        return (self.n_row, self.n_col)
    
    def info(self):
        """
        show storing information.
        """
        print(self.__str__())

    def reload(self):
        self.iter_idx = 0

    def convert_daytime_to_seconds(self, daytime) -> int:
        s = self.datetime.strptime(daytime, self.daytime_format)
        return  calendar.timegm(s.utctimetuple())
    
    def convert_seconds_to_daytime(self, seconds):
        return self.datetime.utcfromtimestamp(seconds).strftime(self.daytime_format)

    def __str__(self):
        x, y = self.size()
        load_flag = not( not self.data )
        out = '\
        file: {}\n\
        load: {}\n\
        size: ({:6d},{:2d})\n\
        '.format(self.filename, load_flag, x, y)
        return out
    
    def __add__(self):
        pass

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            return self.data[key]
        else:
            raise TypeError("Invalid argument type.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_idx >= len(self):
            raise StopIteration
        else:
            self.iter_idx += 1
            return self[self.iter_idx - 1]

    def __len__(self):
        return len(self.data)
        
