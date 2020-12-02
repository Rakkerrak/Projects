def menu():
    print("Option 1: (Part A) \nOption 2: (Part B)\nOption 3: Exit\n\nType a number\n\n")
    option = int(input(">> "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        exit()
    else:
        print("Error Incorrect Input")
        menu()
