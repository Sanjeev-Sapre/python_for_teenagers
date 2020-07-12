    # Exercise - print tables from 11 to 20
# every table should be on new line
# like this
# 11,22,33,44,...
# 12,24,36,.....
# hint - remember to use end commmad in print function. Also use range

for item in range(1,101) :
    # if (item /2) == int int((item /2)):   # if you dont use remainder operator.
    #if (item % 2) == 0:  # means it is even number !
    print(item * user_number, end=' ' )   # line feed \n - google search
