# Exercise - get number from user (use input)
# create table for that number
# example - if user enters 12
# program will print ->  12,24,36,28.... .120
# hint - use range, for loop
# time - 10 min
user_number = int( input( "Enter number :"))

for item in range(1,101) :
    # if (item /2) == int((item /2)):   # if you dont use remainder operator.
    #if (item % 2) == 0:  # means it is even number !
    print(item * user_number, end=' ' )   # line feed \n - google search
