from ctypes import resize
import tkinter as tk
from tkinter import *
from turtle import clear
from PIL import Image,ImageTk


inputs = []
number = []
letters = []
img_names = []


root = tk.Tk()
root.geometry("450x300")
root.title("Input Translator")
canvas = tk.Canvas(root,width=450,height=300)
inputEntry = tk.Entry(canvas)
inputLabel = tk.Label(canvas,text="Inputs: ")
comboLabel = tk.Label(canvas, text="Full Combo: ")
show_input = tk.Label(canvas,text="Input Arrows: ")


def numbTrans(numb):
    global inputName
    if numb == 1:
        inputName = "Down Left"
    elif numb ==  2:
        inputName = "Down"
    elif numb == 3:
        inputName = "Down Right"
    elif numb == 4:
        inputName = "Left"
    elif numb == 5:
        inputName = "Neutral/Center"
    elif numb == 6:
        inputName = "Right"
    elif numb == 7:
        inputName = "Up Right"
    elif numb == 8:
        inputName = "Up"
    elif numb == 9:
        inputName = "Up Left"
    return inputName

def letterTrans(letter):
    global attackType
    if letter.lower() == "h":
        attackType = "Heavy"
    elif letter.lower() == "s":
        attackType = "Slashing"
    elif letter.lower() == "k":
        attackType = "Kick"
    elif letter.lower == "p":
        attackType = "Punch"
    return attackType

def clearInputs():
    global inputs
    inputs.clear()
    global letters
    letters.clear()
    global number
    number.clear()
    global comboLabel
    comboLabel.config(text="Full Combo: ")
    global img_names
    img_names.clear()

def assignImage(inputName):
    global img_names
    if inputName == "Down Left":
        img_names.append("Down_Left")
    elif inputName == "Down Right":
        img_names.append("Down_Right")
    elif inputName == "Up Right":
        img_names.append("Up_Right")
    elif inputName == "Up Left":
        img_names.append("Up_Left")
    else:
        img_names.append(inputName)


def translate():
    clearInputs()
    for numbers in inputEntry.get():
        try:
            number.append(int(numbers))
        except ValueError:
            letters.append(str(numbers))
    for numbers in number:
        inputs.append(numbTrans(numbers))
    for letter in letters:
        inputs.append(letterTrans(letter))
    if inputs[0] == "Right" and inputs[1] == "Right":
        del inputs[0]
        inputs[0] = "Dash Right"
    if inputs[0] == "Left" and inputs[1] == "Left":
        del inputs[0]
        inputs[0] = "Dash Left"
    fullCombo = ", ".join(inputs)
    comboLabel.config(text="Full Combo: " + str(fullCombo))
    for numbInputs in inputs:
        assignImage(numbInputs)
        index = 0
    images = []
    canvas.pack()
    for img_name in img_names:
        filename = f'C:/Users/epicz/Documents/GitHub/InputTranslator/resoruces/{img_name}.png'
        img = (Image.open(filename))
        resized_img = img.resize((25, 25), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(resized_img)
        images.append(new_img)
    for image in images:
        canvas.create_image(225 + 25 * index,212,image=images[index])
        index += 1
    clearInputs()
    root.mainloop()
    inputEntry.delete(0,tk.END)

transBtn = tk.Button(canvas,text="Translate",command=translate)

inputLabel.place(x=100,y=100)
inputEntry.place(x=150,y=100)
transBtn.place(x=125,y=150)
comboLabel.place(x=125,y=175)
show_input.place(x=125,y=200)
canvas.pack()

root.mainloop()