
number = int( input("Enter your number: ") )

if number // 10 == 0 :
    print( "1 digit ")
elif number // 100 == 0:
    print("2 digit")
else:
    print("more than 2 digit")
