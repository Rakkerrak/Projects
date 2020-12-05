import fileinput



def menu():
    print("Option 1: A normal slope(Part A) \nOption 2: All the slopes(Part B)\nOption 3: Exit\n\nType a number\n\n")
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


#Answer is 244
def option1():
    with fileinput.input(files=('Day3b.txt')) as file:
        overflow = 0
        trees = 0
        index = 3
        for line in file:
            linenum = fileinput.lineno()    #line number
            leng = len(line) - 2           #length of line adjusted for index
            if index <= leng and linenum != 1: #checking if line is indexable and skipping first line
                if line[index] == "#":
                    print("*", linenum, index, line[:index + 1])
                    trees += 1
                    index += 3
                else:
                    print(linenum, index, line[:index + 1]) #print lines that aren't counted to see why they aren't counted.
                    index += 3
            elif index > leng:              #handling the overflow
                overflow += 1
                index = index - leng -1
                if line[index] == "#":
                    print("*", linenum, index, line[:index + 1], "of")
                    trees += 1
                    index += 3
                else:
                    print( linenum, index, line[:index + 1], "of")
                    index += 3
            else:
                continue
        print(trees, overflow, 3 * linenum, leng)

def option2():
    def slope(x, y): #x=right y=down
        with fileinput.input(files=('Day3b.txt')) as file:
            trees = 0
            index = x
            for line in file:
                linenum = fileinput.lineno()
                leng = len(line) - 2
                if linenum % y == 0:                #used to skip lines altogether
                    if index <= leng and linenum != 1:  #makes sure first line is skipped
                        if line[index] == "#":
                            trees += 1
                        index += x
                    elif index > leng:
                        index = index - leng - 1
                        if line[index] == "#":
                            trees += 1
                        index += x
                    else:
                        continue
                else:
                    continue
        return trees
    print(slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2))



if __name__ == "__main__":
    menu()
