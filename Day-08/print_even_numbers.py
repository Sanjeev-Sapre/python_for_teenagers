# Exercise - understanding for loop of list.
# create a list of 1 to 10 numbers
# use for loop to print only even numbers
# hint - need to use if command inside loop to check for odd and even.
# time - 10 min
lst = [1, 2, 3, 4,5,6,7,8,9,10]

for item in lst :
    # if (item /2) == int((item /2)):   # if you dont use remainder operator.
    if (item % 2) == 0:  # means it is even number !
        print(item)


