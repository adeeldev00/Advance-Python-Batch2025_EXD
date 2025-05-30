from datetime import datetime, timedelta

def get_next_birthday(birth_date):
    today = datetime.now()
    current_year = today.year
    
    next_birthday = birth_date.replace(year=current_year)
    #print(year=current_year)
    #print(next_birthday)
    if next_birthday < today:
        next_birthday = birth_date.replace(year=current_year + 1)
        #print(year=current_year + 1)
        #print(next_birthday)
    
    return next_birthday

def main():
    print(f'╭──────────────────────────.★..─╮\n  Birthday Countdown Calculator\n╰─..★.──────────────────────────╯')
    print("-----------------------------")
    
    while True:
        try:
            birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
            birth_date = datetime.strptime(birthday_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.") 
    
    next_birthday = get_next_birthday(birth_date)
    today = datetime.now()
    
    time_left = next_birthday - today
    
    #current_year = today.year
    #year = current_year - next_birthday.year
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print("\nTime until your next birthday:")
    print(f"➺ {days} days\n➺ {hours} hours\n➺ {minutes} minutes\n➺ {seconds} seconds")


main()