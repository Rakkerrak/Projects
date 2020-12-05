
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
    with open('Day4.txt', 'r') as file:
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
#function to check value is in a range since it comes up a lot
def rangecheck(field, value, min, max):
    try:
        int(value)
        if min <= int(value) <= max:
            print(field,value,"True")
            return True
        else:
            print(field,value,"False")
            return False
    except ValueError:
        return False

#commanddict functions
def byrcheck(field, value):
    return rangecheck(field, value, 1920, 2020)

def iyrcheck(field, value):
    return rangecheck(field, value, 2010, 2020)

def eyrcheck(field, value):
    return rangecheck(field, value, 2020, 2030)

def hgtcheck(field, value):
    measure = value[-2:]
    if measure in ['cm','in']:
        print(measure)
        try:
            year = int(value[:-2])
            if measure == 'cm':
                return rangecheck(field, year, 150, 193)
            elif measure == 'in':
                return rangecheck(field, year, 59, 76)
            else:
                print("Error")
        except ValueError:
            print(field, value, "Val error")
            return False

def hclcheck(field, value):
    if value[0] == '#':
        for char in value[1:]:
            try:
                int(char)
            except ValueError:
                if char > 'f':
                    print(field, value, "False letter too big")
                    return False
        print(field, value, "True")
        return True
    else:
        print(field, value, "False")
        return False

def eclcheck(field, value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(field, value, "True")
        return True
    else:
        print(field, value, "False")
        return False

def pidcheck(field, value):
    if len(value) == 9 and value.isdigit():
        print(field, value, "True")
        return True
    else:
        print(field, value, "False")
        return False


def option2():
    records = validbynum()
    #creating a dictionary
    recdicts = []
    currec = {}
    for passport in records:
        for field in passport:
            fieldpair = field.split(':')
            currec.update({fieldpair[0]:fieldpair[1]})
        recdicts.append(currec)
        currec = {}
    #checking values in the dictionary. could be merged but...eh
    commanddict = {'byr': byrcheck, 'iyr': iyrcheck, 'eyr': eyrcheck, 'hgt': hgtcheck, 'hcl': hclcheck, 'ecl': eclcheck, 'pid': pidcheck}
    good = []
    for passport in recdicts:
        print(passport)
        ok = True
        while ok == True:
            for field in passport:
                if field in commanddict:
                    # print(field, passport[field])
                    if not commanddict[field](field, passport[field]):
                        ok = False
                        break
                elif field not in commanddict:
                    print(field, "not in dict")
            if ok == True:
                good.append(passport)
                print("passport added")
                break
    print(len(good))







if __name__ == "__main__":
    menu()
