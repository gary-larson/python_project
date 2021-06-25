''' State representation for Covid-19 Data '''
class State:
    ''' A class that defines what state data is '''

    # pylint: disable=too-many-instance-attributes
    # Fifteen is reasonable in this case.

    def __init__(self, **kwargs):
        ''' A method that initializes an object of this class '''
        self._id = kwargs['db_id'] if 'db_id' in kwargs.keys() else 0
        self.state = kwargs['state'] if 'state' in kwargs.keys() else ''
        self.population = kwargs['population'] if 'population' in kwargs.keys() else 0
        self.population_usa_rank = kwargs['populationUSARank'] if \
        'populationUSARank' in kwargs.keys() else 0
        self.pc_of_usa_population = kwargs['pcOfUSAPopulation'] if \
        'pcOfUSAPopulation' in kwargs.keys() else 0.0
        self.mortality_rate = kwargs['mortalityRate'] if 'mortalityRate' in \
        kwargs.keys() else 0.0
        self.pc_of_usa_deaths = kwargs['pcOfUSADeaths'] if 'pcOfUSADeaths' in \
        kwargs.keys() else 0.0
        self.pc_of_usa_active_cases = kwargs['pcOfUSAActiveCases'] if \
        'pcOfUSAActiveCases' in kwargs.keys() else 0.0
        self.pc_of_usa_recovered = kwargs['pcOfUSARecovered'] if \
        'pcOfUSARecovered' in kwargs.keys() else 0.0
        self.pc_of_usa_total_cases = kwargs['pcOfUSATotalCases'] if \
        'pcOfUSATotalCases' in kwargs.keys() else 0.0
        self.total_cases = kwargs['totalCases'] if 'totalCases' in kwargs.keys() else 0
        self.new_cases = kwargs['newCases'] if 'newCases' in kwargs.keys() else 0
        self.total_deaths = kwargs['totalDeaths'] if 'totalDeaths' in kwargs.keys() else 0
        self.new_deaths = kwargs['newDeaths'] if 'newDeaths' in kwargs.keys() else 0
        self.total_active_cases = kwargs['totalActiveCases'] if 'totalActiveCases' in \
        kwargs.keys() else 0
    def __str__(self):
        return (self.state + ', ' + self.population + ', ' +
        self.population_usa_rank + ', ' + self.pc_of_usa_population +
        ', ' + self.mortality_rate + ', ' + self.pc_of_usa_deaths +
        ', ' + self.pc_of_usa_active_cases + ', ' + self.pc_of_usa_recovered +
        ', ' + self.pc_of_usa_total_cases + ', ' + self.total_cases + ', ' +
        self.new_cases + ', ' + self.total_deaths + ', ' + self.new_deaths +
        ', ' + self.total_active_cases)
    def __repr__(self):
        return self.__str__()
    def to_dict(self):
        ''' Returns a dictionary representation of the object '''
        return self.__dict__
