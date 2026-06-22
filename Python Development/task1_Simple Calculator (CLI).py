X=input("Enter the value of x:")
Y=input("enter the value of y:")

if X.isdigit() and Y.isdigit():
    X = int(X)
    Y = int(Y)
    def Calculation(X,Y):
        opertation = input("Enter the symbole for calculation:")
        if opertation == "+":
            return X+Y
        elif opertation == "-":
            return X-Y
        elif opertation == "*":
            return X*Y
        elif opertation == "/":
            if Y == 0:
                return "Cannot divide by zero"
            return X / Y


    Result = Calculation(X,Y)
    print(f"The vlaue is :{Result}")
else:
    print("Invlaid please enter only numbers")

