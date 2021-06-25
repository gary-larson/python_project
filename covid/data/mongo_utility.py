''' Factory to creat a connection to mongo database '''
import os
import pymongo

from log.logger import get_logger

_log = get_logger(__name__)



def get_connection():
    ''' Method to get MongoDB connection through MongoClient '''
    try:
        # Get the connection to the database
        client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
        _log.info("made connection to database")
        return client
    except:
        # Deal with an exception
        _log.exception('Could not connect to Mongo')
        raise
