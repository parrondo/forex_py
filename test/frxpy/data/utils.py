# -*- coding: utf-8 -*-

from zipfile import ZipFile

from frxpy.utils.mylogger import MyLogger

log = MyLogger('data/utils').get_logger()

def load_zip(zipfile):
    log.info('load zip')
    ZipFile(zipfile)
    
    
