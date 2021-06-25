'''Log setup file'''
import logging
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.conf')
logging.config.fileConfig(log_file_path)
#logging.info('this is the root logger') # We could import this object to log directly to the
# system's logger what we'd rather do, is create a logger that knows what file it is logging from
def get_logger(nom):
    '''returns a logger for the module that called the function'''
    return logging.getLogger(nom)
