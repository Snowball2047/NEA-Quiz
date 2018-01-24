import random

def menu():
    print('  1) Log In\n  2) Create New Account\n  3) Generate Reports')
    valid = False
    while valid == False:
        try:
            usr_in = int(input('>>> '))
            if usr_in > 0 and usr_in < 4:
                valid = True
            else:
                print('That is not a valid option. Please try again.')
        except:
            print('That is not a valid option. Please try again.')
    if usr_in == 1:
        log_in()
    elif usr_in == 2:
        new_acct()
    else:
        gen_reps()
        
menu()
