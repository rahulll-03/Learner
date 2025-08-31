a = int(input("Enter your age : "))

if(a >= 18):
    print("you are above the age of consent !")
    print("good for you")
elif(a==0):
    print("age is invalid beouse you enter 0 !")
elif(a<=0):
    print("you are enter invalid age  !")
else:
    print("you are below the age of consent")

print("done  !")