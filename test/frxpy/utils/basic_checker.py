"""

"""
import re
import importlib

def load_class(class_path : str) -> 'class' :
    """load class from a string.
    
    Examples:
    
        >>>> from your.module import YourClass  
        >>>> # instend of the above sentence.
        >>>> YourClass = load_class("your.module.YourClass")

    :param str class_path: path to class. 
        
    :returns: Class 

    """
    module_path, class_name = _check_class_path(class_path)
    mod = importlib.import_module(module_path)
    model = getattr(mod, class_name)
    return model

def _check_class_path(class_path : str) -> (str, str) :
    """check class path. 
    
    If model path is directory path like 'path/module/model', 
    this method changes 'path/module/model' to 'path.module' and 'model'
    
    :params str class_path:
    
    :returns: (module_path, class_name)
        
    """
    class_path_list = re.split('[./]', class_path)
    module_path = ".".join(class_path_list[:-1])
    class_name  = class_path_list[-1]
    return (module_path, class_name)


def check_file(filename):
    """
    """
    return True

def check_db(dbname):
    """
    """
    return True

