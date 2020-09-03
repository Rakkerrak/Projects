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





# # Layout                                                         # Creat GUI
#           [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='input')],
#           [sg.Txt(''  * 10)],
#           [sg.ReadFormButton('('), sg.ReadFormButton(')'), sg.ReadFormButton('c'), sg.ReadFormButton('«')],
#           [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('÷')],
#           [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('x')],
#           [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
#           [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
#           ]
#
# # Set PySimpleGUI
# form = sg.FlexForm('13411_CALCULATOR', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
# form.Layout(layout)
#
# # Set Process
# Equal = ''
# List_Op_Error =  ['+','-','*','/','(']
#
# # Loop
# while True:
#     button, value = form.Read()                            # call GUI
#
#     # Press Button
#     if button is 'c':
#         Equal = ''
#         form.FindElement('input').Update(Equal)
#     elif button is '«':
#         Equal = Equal[:-1]
#         form.FindElement('input').Update(Equal)
#     elif len(Equal) == 16 :
#         pass
#     elif str(button) in '1234567890+-().':
#         Equal += str(button)
#         form.FindElement('input').Update(Equal)
#     elif button is 'x':
#         Equal += '*'
#         form.FindElement('input').Update(Equal)
#     elif button is '÷':
#         Equal += '/'
#         form.FindElement('input').Update(Equal)
#
#    # Process Conditional
#     elif button is '=':
#         # Error Case
#         for i in List_Op_Error :
#             if '*' is Equal[0] or '/' is Equal[0] or ')' is Equal[0]  or i is Equal[-1]:   # Check Error Case
#                 Answer = "Error Operation"
#                 break
#             elif Equal == '6001012630187':
#                 Answer = 'Apisit.Khomcharoen'
#                 break
#             elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
#                 Answer = "Error Operation"
#                 break
#             elif '(' in Equal :
#                 if ')' not in Equal :
#                     Answer = "Error Operation"
#                     break
#             elif '(' not in Equal:
#                 if ')' in Equal:
#                     Answer = "Error Operation"
#                     break
#     # Calculate Case
#         else :
#             Answer = str("%0.2f" %(eval(Equal)))                         # eval(Equal)
#             if '.0' in Answer:
#                 Answer = str(int(float(Answer)))                         # convert float to int
#         form.FindElement('input').Update(Answer)                         # Update to GUI
#         Equal = Answer
#
#     elif button is 'Quit'  or button is None:                            # QUIT Program
#         break
