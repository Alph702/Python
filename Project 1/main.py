# project is conter
from time import sleep
def deposet():
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
    return amount

def Main():
    while True:
        thing = input("What the thing is (q for quit): ")
        if thing != 'q':
            things = []
            things.append(thing)

            price = deposet()
            prices = []
            prices.append(price)

            print(f"The price of {thing} is {price}")
        else:
            for Thing in things:
                print(f"things is {Thing}")
            sleep(60)
            break

Main()
