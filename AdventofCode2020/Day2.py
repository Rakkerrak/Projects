#menu to access both options
def menu():
    print("Option 1: valid by number(Part A) \nOption 2: valid by position(Part B)\nOption 3: Exit\n\nType a number\n\n")
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

#protecting my iterable
def count(strng, goal):
    itern = 0
    for char in strng:
        if char in goal:
            itern += 1
        else:
            pass
    return itern

# I could make this shorter but it'd make it less readable so why?
def option1():
    with open('Day2b.txt','r') as file:
        valid = 0
        for line in file:
            sections = line.split(' ')
            section1 = sections[0].split('-')
            minn = int(section1[0])
            maxx = int(section1[1])
            goal = sections[1][0]
            itern = count(sections[2],goal)
            if minn <= itern <= maxx:
                valid += 1
        print(valid)




def option2():
    with open('Day2b.txt','r') as file:
        valid = 0
        for line in file:
            sections = line.split(' ')
            section1 = sections[0].split('-')
            pos1 = int(section1[0]) - 1
            pos2 = int(section1[1]) - 1
            goal = sections[1][0]
            if (goal in sections[2][pos1] and goal not in sections[2][pos2]) or (goal not in sections[2][pos1] and goal in sections[2][pos2]):
                    valid += 1
        print(valid)

if __name__ == "__main__":
    menu()
