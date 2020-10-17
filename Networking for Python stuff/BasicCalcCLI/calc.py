#!usr/bin/env python
# for Linux
# but we're windows so just use python cli.py

import commands
import argparse #https://docs.python.org/3/library/argparse.html


def main():
    parser = argparse.ArgumentParser() #Creates a parser

    subparsers = parser.add_subparsers(dest = "command") #makes a group of commands that are subparsers

    #first command
    add = subparsers.add_parser(commands.ADD) #creates "add" for the commands subparsers
    add.add_argument("numbers", nargs = "+", type = int) #defines arguments of add under "numbers" which will be a list of 0+ objects with the type int

    #second command
    sub = subparsers.add_parser(commands.SUBTRACT)
    sub.add_argument("numbers", nargs = "+", type = int)

    #third command
    mult = subparsers.add_parser(commands.MULTIPLY)
    mult.add_argument("numbers", nargs = "+", type = int)

    #fourth command
    div = subparsers.add_parser(commands.DIVIDE)
    div.add_argument("numbers",nargs = "+", type = int)

    #make pretty. lists are ugly:
    def pretty(list):
        slist = ""
        for i in list:
            slist += (str(i) + " ")
        return slist

    #logic
    args = parser.parse_args() #creates a parser for args
    if args.command == commands.ADD:
        result = sum(args.numbers) #references the list created in line 16 and sums the ints
        nums = pretty(args.numbers)
        print(f"The sum of ( {nums}) is {result}.")

    elif args.command == commands.SUBTRACT:
        first, *rest = args.numbers #SUPER cool. [first] [rest]. this'll come in handy
        result = first - sum(rest)
        sfirst = str(first)
        srest = pretty(rest)

        print(f"The difference of ( {srest}) from ({sfirst}) is {result}.")

    elif args.command == commands.MULTIPLY:
        result = 1
        for i in args.numbers:
            result *= i
        nums = pretty(args.numbers)

        print(f"( {nums}) all multiplied together is {result}")

    elif args.command == commands.DIVIDE:
        first, *rest = args.numbers
        result = 0
        result += first
        for i in rest:
            result /= i
        nums = pretty(args.numbers)
        woof = round(result, 5) #stopping before the float gets all funky

        print(f"Dividing ( {nums}) all in order yeilds about {woof}")

    else:
        parser.print_help()





if __name__ == "__main__":
    main()
