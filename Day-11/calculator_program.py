# exercise Day 11
# time 10 min
num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))
opr = input("What calculation you have to do?")

opr_list = [ 'a', 's', 'm', 'd']
#  input operation (a,s,m,d)

if opr in opr_list:
    if opr == 'a':
        print( num1 + num2)
    if opr == 's':
        print( num1 - num2)
    if opr == 'm':
        print( num1 * num2)
    if opr == 'd':
        print( num1 / num2)
else:
    print( "You have selected worng operation")

# if not in this operation
# print( invalid operation)

#else
# perform the operation and show the result


