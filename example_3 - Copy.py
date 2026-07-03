name=input("enter the shape:")
if(name.lower()=="cylinder"):
    g=input("enter what you want in cylinder:")
    if(g.lower()=="csa"):
        print("2*3.14*h")
    elif(g.lower()=="tsa"):
        print("(2*pi*r)(r+h)")
    elif(g.lower()=="volume"):
        print("pi*r*r*h")