from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET
from logging import getLogger, StreamHandler, INFO, Formatter

class MyLogger(object):
    """
    frxpy logger class.

    :param str name: set name but thiss clas don't show name.
    :param str space: set a charactor between messages.
    :param str level: set initial log level

    Examples:

    >>> m = MyLogger()
    >>> logger = m.get_logger()
    >>> logger.info('msg')

    >>> m.add('msg1')
    >>> m.add('msg2')
    >>>
    """
    def __init__(self, name, output='', space=' ', level='INFO'):
        self.name = __name__
        self.logger = getLogger(name)
        self.msgs = ['%(message)20s']        
        self.default_format = '[FILE: %(pathname)30s] [FUNC: %(funcName)15s] '
        self.default_format += '[LINE: %(lineno)4d]: '
        default_format = self._update_default_format()
        formatter = Formatter(default_format)
        self.handler = StreamHandler()
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)        
        self.set_level(level)
            
    def get_logger(self):
        """
        return logger.
        """
        return self.logger
    
    def push(self, msg):
        """
        Fisrt-In-Last-Out
        """
        self.clean()        
        self.msgs.insert(len(self.msgs)-1, msg)
        self.handler = StreamHandler()
        default_format = self._update_default_format()
        formatter = Formatter(default_format)
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def _update_default_format(self):
        """
        updates default format. This method is only called from internal method.
        """
        default_format = self.default_format[:]
        for imsg in self.msgs:
            default_format += imsg
        return default_format

    def pop(self):
        """
        Fisrt-In-Last-Out
        """
        self.clean()
        del self.msgs[0]
        print('>>>>>', self.msgs)
        formatter = Formatter(self._update_default_format())
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def clean(self):
        """
        create new name and set new logger in this class.
        """
        self.logger.removeHandler(self.handler)
        
    def set_level(self, level):
        """
        set log level []
        
        Args:


        :param str level: DEBUG
        :param str level: INFO
        :param str level: WARNING
        :param str level: ERROR
        :param str level: CRITICAL

        """
        
        if level == 'DEBUG':
            self.logger.setLevel(DEBUG)
        elif level == 'INFO':
            self.logger.setLevel(INFO)
        elif level == 'WARNING':
            self.logger.setLevel(WARNING)
        elif level == 'ERROR':
            self.logger.setLevel(ERROR)
        elif level == 'CRITICAL':
            self.logger.setLevel(CRITICAL)
        else:
            self.logger.setLevel(NOTSET)

