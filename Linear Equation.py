def logo():
    print("LINEAR EQUATIONS \o/")
    print("by Andrew Hillman")
def Linear_Equations():
    print("This will solve two equations of the y=mx+b")
    print("Please enter the first equation")

    m1 = int(input ("Enter the m value: "))
    b1 = int(input ("Enter the b value: "))

    print("Please enter the second equation")

    m2 = int(input ("Enter the m value: "))
    b2 = int(input ("Enter the b value: "))

    if(b2==b1 and m2==m1):
        print("Equations are equal")
    elif ((m1- m2) == 0):
        print("invalid input, no intersection")
    else:
        equation = (b2 - b1) / (m1 - m2)
        print("The solution is y:",  equation)
logo()
Linear_Equations()
