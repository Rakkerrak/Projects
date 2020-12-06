
#returns list of groups. group is a list of strings, a string per person.
def getgroups():
    with open('Day6.txt', 'r') as file:
        groupList = []
        currgroup = []
        for line in file:
            if line not in ['\n', '\n\n']:
                currgroup.append(line.strip())
            else:
                groupList.append(currgroup)
                currgroup = []
        groupList.append(currgroup)
    return(groupList)

def option1():
    groupList = getgroups()
    norepeatsgroups = []
    for group in groupList:
        combined = []
        for person in group:
            for char in person:
                if char not in combined:
                    combined.append(char)
        norepeatsgroups.append(combined)
    answer = 0
    for group in norepeatsgroups:
        answer += len(group)
    print(answer, "unique 'yes'es ")


def option2():
    groupList = getgroups()
    count = 0
    allyesgroups = []
    for group in groupList:
        person1 = group[0]
        for person in group[1:]:
            for char in person1:                        #checks against the first person since first person must contain every letter(they all do but we have to pick one ok)
                if char not in person:
                    person1 = person1.replace(char,'')  #removes from first person if first person has a unique letter.
        if person1 != '':                               #removes empty lists. len([''])=1
            allyesgroups.append(person1)
            count += len(person1)
    print(count, " communal 'yes'es ")


def menu():
    #privae grievance: yes's is silly. That is all.
    print("\nOption 1: Number of Unique yes's(Part A) \nOption 2: Number of communal yes's(Part B)\nOption 3: Exit\n\nType a number\n\n")
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

if __name__ == "__main__":
    menu()
