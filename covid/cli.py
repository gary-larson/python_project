''' Module to run the command line interface '''
from data.setup import setup_mongo
from data.covid_dao import MongoDao
from data.mongo_utility import get_connection
from user.model import User

conn = get_connection()
db = conn.get_database('pycovid')
states_col = db.get_collection("states")
users_col = db.get_collection("users")
counters_col = db.get_collection("counters")
# Get DAO
dao = MongoDao()
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
    name = ''
    while is_invalid_name:
        print("Enter a name (letters and numbers only)")
        print("Press 'q' or 'Q' for previous menu")
        user_input = input("Enter Choice: ")
        if user_input.isalnum():
            is_invalid_name = False
        else:
            print("Invalid entry please try again!")
    return user_input
def get_user():
    ''' Method to get the user from the database '''
    name_exists = False
    not_quit = True
    name = ''
    user = User()
    while not name_exists and not_quit:
        name = input_name()
        if name == 'q' or name == 'Q':
            not_quit = False
        else:
            dict_user = dao.get_user_by_name(users_col, name)
            if dict_user == None:
                print(name + " does not exist! Please choose another.")
            else:
                name_exists = True
                user.set_id(dict_user['_id'])
                user.name = dict_user['name']
                user.last_visited = dict_user['last_visited']
                user.state_offset = dict_user['state_offset']
                user.percent_offset = dict_user['percent_offset']
    return user
def create_user():
    ''' Method to create a user in the database '''
    name_exists = True
    not_quit = True
    name = ''
    user = User()
    while name_exists and not_quit:
        name = input_name()
        if name == 'q' or name == 'Q':
            not_quit = False
        else:
            dict_user = dao.get_user_by_name(users_col, name)
            if dict_user == None:
                name_exists = False
                user.name = name
                user.state_offset = 0
                user.percent_offset = 0
                dao.add_user(users_col, counters_col, user)
                dict_user = dao.get_user_by_name(users_col, name)
                user.set_id(dict_user['_id'])
                user.name = dict_user['name']
                user.last_visited = dict_user['last_visited']
                user.state_offset = dict_user['state_offset']
                user.percent_offset = dict_user['percent_offset']
            else:
                print(name + " Exists Please choose another name!")
    return user 
def delete_user():
    ''' Method to delete the user from the database '''
    name_exists = False
    not_quit = True
    name = ''
    user = User()
    while not name_exists and not_quit:
        name = input_name()
        if name == 'q' or name == 'Q':
            not_quit = False
        else:
            dict_user = dao.get_user_by_name(users_col, name)
            if dict_user == None:
                print(name + " exists! Please choose another.")
            else:
                name_exists = True
                confirm_delete = False
                while not confirm_delete:
                    print("are you sure you want to delete user: " + name)
                    user_input = input("Press 'y', 'Y', 'n', or 'N': ")
                    if user_input in ['y', 'Y']:
                        dao.remove_user_by_id(users_col, dict_user['_id'])
                        confirm_delete = True
                        name_exists = True
                    elif user_input in ['n', 'N']:
                        confirm_delete = True
                        name_exists = True
                    else:
                        print("Invalid Entry Please try again")
    return None            
def get_user_name():
    ''' Method to get the user name '''
    keep_looping = True
    while keep_looping:
        print_user_menu()
        user_input = input('Enter choice: ')
        if user_input[0] == '1':
            user = get_user()
            if not user.name == '':
                keep_looping = False
        elif user_input[0] == '2':
            user = create_user()
            if not user.name == '':
                keep_looping = False
        elif user_input[0] == '3':
            delete_user()
        elif user_input[0] == 'q' or user_input[0] == 'Q':
            keep_looping = False
        else:
            print('Invalid entry please try again.')
    return user


if __name__ == '__main__':
    setup_mongo()
    user = get_user_name()
    print_main_menu(user.name)