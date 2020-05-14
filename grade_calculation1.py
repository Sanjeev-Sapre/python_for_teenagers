percent = int( input("enter your perent :"))


if percent > 75 :
    print("Distinction")
else :
    if percent > 60:
        print('First Class')
    else :
        if percent > 40:
            print("Second Class")
        else :
            if percent < 40 :
                print( "Failed")



