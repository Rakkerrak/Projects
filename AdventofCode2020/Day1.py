#importing a list of numbers for the challenge
import Day1b

#Creating a menu to access both options
def main():
    print("Option 1: two numbers(Part A) \nOption 2: three numbers(Part B)\nOption 3: Exit\n\nType a number\n\n")
    option = int(input(">> "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        exit()
    else:
        print("Error Incorrect Input")
        main()



def option1():
    for curr1 in range(len(Day1b.nums)):
        for curr2 in range(len(Day1b.nums)):
            if Day1b.nums[curr1] + Day1b.nums[curr2] == 2020:
                print(Day1b.nums[curr1] * Day1b.nums[curr2])
                print("Done")
                main()

def option2():
    for curr1 in range(len(Day1b.nums)):
        for curr2 in range(len(Day1b.nums)):
            for curr3 in range(len(Day1b.nums)):
                if Day1b.nums[curr1] + Day1b.nums[curr2] + Day1b.nums[curr3] == 2020:
                    print(Day1b.nums[curr1] * Day1b.nums[curr2] * Day1b.nums[curr3])
                    print("Done")
                    main()


#I did the python thing r u proud?
if __name__ == "__main__":
        main()
