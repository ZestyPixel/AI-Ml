a = input("Enter User Id: ")
b = input("Enter Pin: ")

if(a == "123" and b == "456"):
    print("Login Successful")
elif(a == "456" and b == "123"):
    print("Login Details Reversed")
else:
    if(a != "123"):
        print("Wrong user id")
    else:
        print("Wrong pin")