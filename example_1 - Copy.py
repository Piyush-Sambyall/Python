age=int(input("age: "))
if age<18:
    print("teenager")
    if age<16:
        print("minor")
    else:
        print("KID")