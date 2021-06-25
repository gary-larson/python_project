''' Factory to do initial setup of MongoDB database '''
import os
import json
from data.mongo_utility import get_connection



def setup_mongo():
    ''' Method to check and setup MongoDB '''
    # Get connection to MongoDB
    _connection = get_connection()
    # Get database
    _db = _connection["pycovid"]
    # Get counters collection
    _counters_collection = _db['counters']

    # Check if there are documents in counters collection if not create it
    if _counters_collection.count_documents({}) == 0:
        _counters_collection.insert_one({'_id': 'UNIQUE_STATE_COUNT', 'count': 0})
        _counters_collection.insert_one({'_id': 'UNIQUE_USER_COUNT', 'count': 0})

    _states_collection = _db['states']
    # Check if there are any documents in states collection if not create and populate it
    if _states_collection.count_documents({}) == 0:
        directory = os.path.dirname(__file__)
        try:
            with open(directory + '\\states.json') as json_file:
                state_json = json.load(json_file)
                _states_collection.insert_many(state_json)
        except:
            print('Could not add states list')
            raise
