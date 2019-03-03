print('\033c') 
# print('\x1bc')


def age_program():
    user_age = input("Enter your age: ")
    age_second = int(user_age) * 365 * 24 * 60 * 60
    print("your age in seconds is {}".format(age_seconds))

age_program()