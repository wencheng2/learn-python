# Importing the 'datetime' module
from datetime import datetime

# Creating a date using year, month, day as arguments
birthday = datetime(2022, 6, 5)

# Check
print("Year is:", birthday.year)
print("Month is:", birthday.month)
print("Day of week is:", (birthday.weekday()+1))

# Creating a date using datetime.now()
print(datetime.now())

# Parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print("The month is:", parsed_date.month)

# Rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print("Today's date is:", date_string)