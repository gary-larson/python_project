import datetime
import pytest
from user.model import User

@pytest.fixture
def my_user():
    ''' returns empty user'''
    return User()

@pytest.fixture
def constructed_user():
    ''' returns a constructed user '''
    return User(db_id = 23, name = 'Serena', last_visited = '2021-06-28 16:32:23', 
    state_offset = 30, percent_offset = 50)

def test_populate_user_name(my_user):
    my_user.name = "Gary"
    assert my_user.name == "Gary"

def test_populate_user_id(my_user):
    my_user.db_id = 5
    assert my_user.db_id == 5

def test_populate_user_state_offset(my_user):
    my_user.state_offset = 10
    assert my_user.state_offset == 10

def test_populate_user_percent_offset(my_user):
    my_user.percent_offset = 20
    assert my_user.percent_offset == 20

def test_populate_user_last_visited(my_user):
    my_date_time_string = datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S")
    my_user.last_visited = my_date_time_string
    assert my_user.last_visited == my_date_time_string

def test_constructed_user_db_id(constructed_user):
    assert constructed_user.db_id == 23

def test_constructed_user_name(constructed_user):
    assert constructed_user.name == 'Serena'

def test_constructed_user_last_visited(constructed_user):
    assert constructed_user.last_visited == '2021-06-28 16:32:23'

def test_constructed_user_state_offset(constructed_user):
    assert constructed_user.state_offset == 30

def test_constructed_user_percent_offset(constructed_user):
    assert constructed_user.percent_offset == 50