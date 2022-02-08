import datetime
users_date_of_birth: str = input('what is your date of birth? ')
current_year: int = datetime.date.today().year
# User input validation

if not users_date_of_birth.isdigit():
    print('Enter digits only, please')
else:
    users_date_of_birth: int = int(users_date_of_birth)
    user_age: int = int(current_year - users_date_of_birth)

    if user_age == 21:
        print('You', 'should', 'visit', 'Holland', sep=' ')
    elif user_age > 21:
        print('You', 'should', 'visit', 'Vietnam.', sep=' ')
    else:
        print('Travell everywhere')
