import tkinter as tk
from tkinter import NE, PhotoImage, filedialog, image_names

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
    for img_name in img_names:
        filename = "C:/Users/sammo/Python/resoruces/{}.png".format(img_name)
        img = PhotoImage(file=filename)
        img.subsample(2,2)
        canvas.create_image(150,200,image=img)
    inputEntry.delete(0,tk.END)

transBtn = tk.Button(canvas,text="Translate",command=translate)

inputLabel.place(x=100,y=100)
inputEntry.place(x=150,y=100)
transBtn.place(x=125,y=150)
comboLabel.place(x=125,y=175)
show_input.place(x=125,y=200)
canvas.pack()

root.mainloop()