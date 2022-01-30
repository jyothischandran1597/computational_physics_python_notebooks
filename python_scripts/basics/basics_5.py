## Calender

import calendar

# ask of month and year
year = int(input("Please Enter the year Number: "))
month = int(input("Please Enter the month Number: "))

print(calendar.month(year, month))

### Remarks
#* "import \<package name\>" imports the python library\package named after "import" and enables us to use the functions from that specific package.
#* "calender" is a python library and calender.month() is a function that gives the calender of the year and month given as an input for the function.
#* There are multiple ways to import a full package, a specific subset of a package or only specific functions from a package.