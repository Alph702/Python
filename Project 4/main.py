def Main():
    Id = input("Enter the email id:\n> ")
    password = input("Enter the password:\n> ")
    with open(r"pass.txt",'a') as f:
        f.write(f"Email: {Id}\nPassword: {password}\n \n")
Main()