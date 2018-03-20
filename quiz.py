import random
import json

def write(to_write):
    file = open('user_info.json' , 'w')
    json_dump = json.dumps(to_write)
    file.write(json_dump)
    file.close

def load_users():
    try:
        file = open('user_info.json' , 'r')
        users = json.load(file)
        file.close()
        return users
        #print('Load Success!') #DEBUG
    except:
        #print('Load Failed!') #DEBUG
        users = {'top':{'History': ['NONE', 0], 'Music': ['NONE', 0], 'Computer Science': ['NONE', 0]}}
        write(users)

def user_exist(username):
    #print('User check') #DEBUG
    try:
        users = load_users()
        users[username]
        return True
    except:
        return False
        

def menu():
    print('\n  1) Log In\n  2) Create New Account\n  3) Generate Reports')
    valid = False
    while valid == False:
        try:
            usr_in = int(input('>>> '))
            if usr_in > 0 and usr_in < 4:
                valid = True
            else:
                print('\nThat is not a valid option. Please try again.')
        except:
            print('\nThat is not a valid option. Please try again.')
    if usr_in == 1:
        log_in()
    elif usr_in == 2:
        new_user()
    else:
        gen_reps()

def new_user():
    users = load_users()
    run = True
    while run:
        print('\nPlease enter your full name.')
        name = input('>>> ')
        space_absent = True
        int_present = False
        for i in range(len(name)):
            try:
                int(name[i])
                int_present = True
            except:
                pass
            if name[i] == ' ':
                space_absent = False
        if int_present or space_absent:
            print('\nThat is not a valid option.')
        else:
            run = False
    run = True
    while run:
        try:
            print('\nPlease enter your age.')
            age = int(input('>>> '))
            run = False
        except:
            print('\nThat is not a valid option.')
    print('\nPlease enter your year group.')
    year = input('>>> ')
    username = name[:3].lower() + str(age)
    if user_exist(username):
        print('\nThat user already exists; please use the log in section to access your account, or enter different user information.')
        menu()
    print('\nPlease enter in your desired password.')
    password =  input('>>> ')
    print('\nPlease confirm in your desired password.')
    password =  input('>>> ')
    users[username] = {"user" : username, "pass" : password, "name" : name, "age" : age, "year" : year, "quizzes" : []}
    print('\nYour username is: ' + username)
    print('\nYour password is: ' + password)
    write(users)
    topic_menu(users)

menu()
