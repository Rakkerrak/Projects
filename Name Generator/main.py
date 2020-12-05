import PySimpleGUI as sg
import random

import names
import experimental as exp

layout = [[sg.Txt("Random Name Generator")],
            [sg.Checkbox("Female", enable_events = True, key = "FE"), sg.Checkbox("Male", enable_events = True, key = "MA")],
            [sg.Txt("Name:")], [sg.Text(size=(25,1), key = "GEN-NAME")],
            [sg.Button("Generate")],
            [sg.Txt("Experimental:")],
            [sg.Txt("Name:"), sg.Txt(size = (25,1), key = "EXP_NAME")],
            [sg.Button("Try it")]
            ]
window = sg.Window("Random Name Generator", layout)

def nameExp():
    syllables = random.randint(1, 4)
    name = ""
    vowelStart = random.randint(0, 1)
    if vowelStart == 1:
        name = name + random.choice(exp.vowels)
    for _ in range(0, syllables):
        name = name + random.choice(exp.cons) + random.choice(exp.vowels)
    return name.title()

def main():
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        namelist = []
        if values["FE"] == True:
                namelist.extend(names.feFirst)
        if values["MA"] == True:
                namelist.extend(names.maFirst)
        if values["MA"] == False and values["FE"] == False:
            namelist = names.maFirst + names.feFirst
        if event == 'Generate':
            name = random.choice(namelist) + " " + random.choice(names.last)
            window["GEN-NAME"].update(name)
        if event == "Try it":
            window["EXP_NAME"].update(nameExp() + " " + nameExp())

main()



window.close()
