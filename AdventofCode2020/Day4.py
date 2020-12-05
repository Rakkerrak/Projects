
def menu():
    print("Option 1: Valid by Number (Part A) \nOption 2: Valid but Picky(Part B)\nOption 3: Exit\n\nType a number\n\n")
    try:
        option = int(input(">> "))
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            exit()
        else:
            print("Error: Incorrect Input\n\n")
            menu()
    except ValueError:
        print("Error: Incorrect Input. Enter a number\n\n")
        menu()

def validbynum(): #returns a list of passport records(records are a list of strings)
    with open('test.txt', 'r') as file:
        lines = file.readlines()
        #seoerating the different records by looking at the newlines.
        records1 = []
        currec = []
        for item in lines:
            if item != '\n':
                currec.append(item[:-1])
            else:
                records1.append(currec)
                currec = []
        records1.append(currec)
        #getting all fields into the same list, each field to a value in the list, lists in the list of records.
        records2 = []
        currec2 = []
        for elem in records1:
            for str in elem:
                fields = str.split(' ')
                currec2.extend(fields)
            records2.append(currec2)
            currec2 = []
        valid = 0
        good = []
        for passport in records2:
            if len(passport) == 8:
                valid += 1
                good.append(passport)
            elif len(passport) == 7:
                ok = True
                for field in passport:
                    if 'cid' in field:
                        ok = False
                        break
                if ok:
                    valid += 1
                    good.append(passport)
        return good

def option1():
        print(len(validbynum()))


def option2():
    print("in progress")
    menu()



if __name__ == "__main__":
    menu()
