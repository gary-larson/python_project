''' Module to deal with user's data '''

class User:
    ''' A class that defines what user data is '''
    def __init__(self, **kwargs):
        ''' A method that initializes an object of this class '''
        self._id = kwargs['db_id'] if 'db_id' in kwargs.keys() else 0
        self.name = kwargs['name'] if 'name' in kwargs.keys() else ''
        self.last_visited = kwargs['last_visited'] if 'last_visited' in kwargs.keys() else ''
        self.state_offset = kwargs['state_offset'] if 'state_offset' in kwargs.keys() else 0
        self.percent_offset = kwargs['percent_offset'] if 'percent_offset' in kwargs.keys() else 0
    def __str__(self):
        ''' Method to give string representation '''
        return (self.name + ', ' + self.last_visited + ', ' +
        str(self.state_offset) + ', ' + str(self.percent_offset))
    def __repr__(self):
        ''' Method to give a printable representation '''
        return self.__str__()
    def to_dict(self):
        ''' Returns a dictionary representation of the object '''
        return self.__dict__
    def set_id(self, _id):
        ''' Method to set the id '''
        self._id = _id
    def set_last_visited(self, last_visited):
        ''' Method to set the last visited date and time '''
        self.last_visited = last_visited
