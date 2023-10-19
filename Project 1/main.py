# project is conter

def deposet():
    try:
        while True:
            amount = input("What amount the prodect is? $")
            if amount.isdigit:
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("The velue is grater then 0.")
            else:
                print("Plese enter a number.")
    except Exception as e:
        print(e)

def Main():
    while True:
        thing = input("What the thing is: ")
        things = []
        while True
