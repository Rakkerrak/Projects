def menu():
    print("Option 1: Part 1 and 2 \nOption 2: There is no Option 2\nOption 3: Exit\n\nType a number\n\n")
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

def upperhalf(range, char):
    range[0] = (range[0] + range[1])//2 + 1
    return range

def lowerhalf(range, char):
    range[1] = (range[0] + range[1])//2
    return range


def option1():
    with open('Day5.txt',  'r') as file:
        do = { 'B': upperhalf, 'F': lowerhalf, 'R': upperhalf, 'L': lowerhalf}
        final = []
        IDs = []
        for line in file:
            rowcolID = [0,0,0]      
            rowrange = [0, 127]
            colrange = [0, 7]
            for char in line[:6]:
                rowrange = do[char](rowrange, char)
            if line[6] == 'F':
                rowcolID[0] = rowrange[0]
            elif line[6] == 'B':
                rowcolID[0] = rowrange[1]
            for char in line[7:-2]:
                colrange = do[char](colrange, char)
            if line[-2] == 'R':
                rowcolID[1] = colrange[1]
            elif  line[-2] == 'L':
                rowcolID[1] = colrange[0]
            rowcolID[2] = rowcolID[0] * 8 + rowcolID[1]
            final.append(rowcolID)
            IDs.append(rowcolID[2])
        print(max(IDs), " is the highest ")
        IDs.sort()
        missing = [x for x in range(IDs[0], IDs[-1] + 1) if x not in IDs]
        print(missing, " is your seat ID")

def option2():
    print("Told you so\n\n")
    menu()

if __name__ == "__main__":
    menu()
