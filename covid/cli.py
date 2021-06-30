''' Module to run the command line interface '''
from user.model import User

from data.setup import setup_mongo
from data.mongo_utility import get_connection
from data.covid_dao import get_user_by_name
from data.covid_dao import add_user
from data.covid_dao import remove_user_by_id
from data.covid_dao import get_states
from data.covid_dao import get_percents
from data.covid_dao import update_user_by_id

# pylint: disable=invalid-name
conn = get_connection()
db = conn.get_database('pycovid')
states_col = db.get_collection("states")
users_col = db.get_collection("users")
counters_col = db.get_collection("counters")
LIMIT = 10
STATE_COUNT = states_col.count_documents({})
def print_main_menu(name):
    ''' Method to print the main menu '''
    print("\nWelcome " + name)
    print(" *** MAIN MENU ***")
    print("Press '1' to print next screen of basic state data")
    print("Press '2' to print next screen of percent state data")
    print("Press 'q' or 'Q' to quit")
def print_user_menu():
    ''' Method to print the user menu'''
    print("\n   *** USER MENU ***")
    print("Press '1' for an existing user.")
    print("Press '2' to create a new user.")
    print("Press '3' to delete a user.")
    print("Press 'q' or 'Q' to quit program.")
def input_name():
    ''' Method to get the user name from the user '''
    is_invalid_name = True
    while is_invalid_name:
        print("\n\nEnter a name (letters and numbers only)")
        print("Press 'q' or 'Q' for previous menu")
        my_input = input("Enter Choice: ")
        if my_input.isalnum():
            is_invalid_name = False
        else:
            print("Invalid entry please try again!")
    return my_input
def get_user():
    ''' Method to get the user from the database '''
    name_exists = False
    not_quit = True
    name = ''
    my_user = User()
    while not name_exists and not_quit:
        name = input_name()
        if name in ('q', 'Q'):
            not_quit = False
        else:
            dict_user = get_user_by_name(users_col, name)
            if dict_user is None:
                print(name + " does not exist! Please choose another.")
            else:
                name_exists = True
                my_user.db_id = dict_user['_id']
                my_user.name = dict_user['name']
                my_user.last_visited = dict_user['last_visited']
                my_user.state_offset = dict_user['state_offset']
                my_user.percent_offset = dict_user['percent_offset']
    return my_user
def create_user():
    ''' Method to create a user in the database '''
    name_exists = True
    not_quit = True
    name = ''
    my_user = User()
    while name_exists and not_quit:
        name = input_name()
        if name in ('q', 'Q'):
            not_quit = False
        else:
            dict_user = get_user_by_name(users_col, name)
            if dict_user is None:
                name_exists = False
                my_user.name = name
                my_user.state_offset = 0
                my_user.percent_offset = 0
                add_user(users_col, counters_col, user)
                dict_user = get_user_by_name(users_col, name)
                my_user.db_id = dict_user['_id']
                my_user.name = dict_user['name']
                my_user.last_visited = dict_user['last_visited']
                my_user.state_offset = dict_user['state_offset']
                my_user.percent_offset = dict_user['percent_offset']
            else:
                print(name + " Exists Please choose another name!")
    return my_user
def delete_user():
    ''' Method to delete the user from the database '''
    name_exists = False
    not_quit = True
    name = ''
    while not name_exists and not_quit:
        name = input_name()
        if name in ('q', 'Q'):
            not_quit = False
        else:
            dict_user = get_user_by_name(users_col, name)
            if dict_user is None:
                print(name + " exists! Please choose another.")
            else:
                name_exists = True
                confirm_delete = False
                while not confirm_delete:
                    print("are you sure you want to delete user: " + name)
                    my_user_input = input("Press 'y', 'Y', 'n', or 'N': ")
                    if my_user_input in ['y', 'Y']:
                        remove_user_by_id(users_col, dict_user['_id'])
                        confirm_delete = True
                        name_exists = True
                    elif my_user_input in ['n', 'N']:
                        confirm_delete = True
                        name_exists = True
                    else:
                        print("Invalid Entry Please try again")
def get_user_name():
    ''' Method to get the user name '''
    keep_looping = True
    while keep_looping:
        print_user_menu()
        my_user_input = input('Enter choice: ')
        if my_user_input[0] == '1':
            my_user = get_user()
            if my_user.name != '':
                keep_looping = False
        elif my_user_input[0] == '2':
            my_user = create_user()
            if my_user.name != '':
                keep_looping = False
        elif my_user_input[0] == '3':
            delete_user()
        elif my_user_input[0] == 'q' or user_input[0] == 'Q':
            keep_looping = False
            my_user.name = my_user_input[0]
        else:
            print('Invalid entry please try again.')
    return my_user


if __name__ == '__main__':
    setup_mongo()
    user = get_user_name()
    continue_looping = True
    if user.name == 'q' or user.name == 'Q':
        continue_looping = False
    while continue_looping:
        print_main_menu(user.name)
        user_input = input('Enter choice: ')
        if user_input[0] == '1':
            # Print screen with basic information and update user
            state_offset = user.state_offset
            states = get_states(states_col, state_offset, LIMIT)
            if states is None:
                print("No results")
            else:
                # Print header
                print("               State  Population Population-Rank Total-Cases New-Cases" +
                    " Total-Deaths New-Deaths Total-Active-Cases")
                for state in states:
                    print(format("%20s %11s %15s %11s %9s %12s %10s %18s" % (state['state'],
                    "{:,}".format(state['population']), "{:,}".format(state['populationUSARank']),
                    "{:,}".format(state['totalCases']), "{:,}".format(state['newCases']),
                    "{:,}".format(state['totalDeaths']), "{:,}".format(state['newDeaths']),
                    "{:,}".format(state['totalActiveCases']))))
                # update user state offset
                state_offset += LIMIT
                if state_offset > STATE_COUNT:
                    state_offset = 0
                update_user_by_id(users_col, user.db_id, state_offset, user.percent_offset)
        elif user_input[0] == '2':
            # print screen with percent information and update user
            percent_offset = user.percent_offset
            states = get_percents(states_col, percent_offset, LIMIT)
            if states is None:
                print("No results")
            else:
                # Print header
                print("               State Percent-Population Mortality-Rate Percent-Cases " +
                    "Percent-Deaths Percent-Recovered Percent-Active-Cases")
                for state in states:
                    print("%20s %18s %14s %13s %14s %17s %20s" % (state['state'],
                    "{:,.2f}".format(state['pcOfUSAPopulation']),
                    "{:,.2f}".format(state['mortalityRate']),
                    "{:,.2f}".format(state['pcOfUSATotalCases']),
                    "{:,.2f}".format(state['pcOfUSADeaths']),
                    "{:,.2f}".format(state['pcOfUSARecovered']),
                    "{:,.2f}".format(state['pcOfUSAActiveCases'])))
                # update user state offset
                percent_offset += LIMIT
                if percent_offset > STATE_COUNT:
                    percent_offset = 0
                update_user_by_id(users_col, user.db_id, user.state_offset, percent_offset)
        elif user_input[0] == 'q' or user_input[0] == 'Q':
            # Quit the program
            continue_looping = False
        else:
            print('Invalid Entry Please try again!')
