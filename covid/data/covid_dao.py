''' Data Access Module for Covid-19 data '''
import datetime
import pymongo
from data.mongo_utility import get_connection

class MongoDao:
    ''' Data Access Object for states '''

    def __init__(self):
        ''' Initializes the class'''
    def _get_user_id(self, counters_col):
        ''' Retrieves the next user id in the database and increment it '''
        return counters_col.find_one_and_update(
        {'_id': 'UNIQUE_USER_COUNT'},
        {'$inc': {'count': 1}},
        return_document=pymongo.ReturnDocument.AFTER)['count']
    def add_user(self, users_col, counters_col, my_user):
        ''' Method to insert one user into the database '''
        my_user.set_id(self._get_user_id(counters_col))
        my_user.set_last_visited(datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
        dict_user = my_user.to_dict()
        users_col.insert_one(dict_user)
    def get_user_by_name(self, users_col, name):
        ''' Method to get user by name '''
        query = users_col.find({'name': name})
        users = list(query)
        if len(users) == 0:
            return None
        return users[0]
    def get_states(self, states_col, state_offset, limit):
        ''' Method to get the states basic data for the limit after the offset '''
        return states_col.find({}, {"state": 1, "population": 1, "populationUSARank": 1,
        "totalCases": 1, "newCases": 1, "totalDeaths": 1, "newDeaths": 1,
        "totalActiveCases": 1}).sort({'state': 1}).skip(state_offset).limit(limit)
    def get_percents(self, states_col, percent_offset, limit):
        ''' Method to get the states percent data for the limit after the offset'''
        return states_col.find({}, {"state": 1, "pcOfUSAPopulation": 1, "mortalityRate": 1,
        "pcOfUSADeaths": 1, "pcOfUSAActiveCases": 1, "pcOfUSARecovered": 1,
        "pcOfUSATotalCases": 1}).sort({'state': 1}).skip(percent_offset).limit(limit)
    def update_user_by_id(self, users_col, db_id, state_offset, percent_offset):
        ''' Method to update the users data '''
        users_col.update({'_id': db_id}, {"$set": {"stateOffset": state_offset,
        "percentOffset": percent_offset, 
        "lastVisited": datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S")}})
    def remove_user_by_id(self, users_col, db_id):
        ''' Method to remove the user '''
        users_col.delete_one({'_id': db_id})
