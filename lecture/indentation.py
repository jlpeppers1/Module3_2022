


#Sequential
age = 16
rating = 'pg13'
#conditional with two relational/logical operators
if ((rating == 'r') and (age < 17)):
    print("You are too young to see the movie.")
    #nested conditional with one relational/logical operator
    if (age > 13):
        print("There are other movies availible")
    else:
        print("Please bring your parent with you")
else:
    print('Your age is fine to see the movie')
#Sequential
print('Done with program')
