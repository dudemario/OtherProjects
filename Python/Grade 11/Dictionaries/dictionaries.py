from Tkinter import *
import functools
from PIL import Image, ImageTk ######Import http://www.pythonware.com/products/pil/

root = Tk()
mainframe = Frame(root)

title = Label(mainframe, text = "Dictionaries", font=("Helvetica", 40))

mainframe.grid()
title.grid(row = 1, column = 1, columnspan = 8, padx = 50, pady = 50)
myDict = {1:"\"A\"", 2:"\"B\"", 3:"\"C\"", 4:"\"D\"", 5:"\"E\""}

image = Image.open("arrow.png")
arrowPhoto = ImageTk.PhotoImage(image)

cw = 200
ch = 200
canvas = Canvas(mainframe, width=cw, height=ch)
def createDrawing():
    background = canvas.create_rectangle(0,0,350,350,fill="#FFCC99")
    canvas.grid(row = 2, column = 2, padx = 50, pady = 20)

    for i in xrange(5):
        canvas.create_text(cw*3/12, ch*(i+1)/6, text = i+1)
        canvas.create_text(cw*9/12, ch*(i+1)/6, text = "\""+chr(i+65)+"\"")


def createLine(row):
    canvas.create_line(60, 33.3*(row), 135, 33.3*(row))

def Scene1():
    def nextScreen(event):
        heading1.grid_remove()
        termFrame.grid_remove()
        arrow.grid_remove()
        defFrame.grid_remove()
        heading2.grid_remove()
        keyFrame.grid_remove()
        arrow2.grid_remove()
        valueFrame.grid_remove()
        nextSceneLabel.grid_remove()
        Scene2()
        
    heading1 = Label(mainframe, text = "Regular Dictionaries:", font=("Helvetica",25))
    heading1.grid(row = 2, column = 1, columnspan = 3, padx = 50, pady = 20)
    
    termFrame = LabelFrame(mainframe, text = "Term", font=("Helvetica",15))
    termFrame.grid(row = 3, column = 1, padx = 50, pady = 20, sticky = "N")
    
    term = Label(termFrame, text = "Dictionary")
    term.grid(row = 4, column = 1, padx = 50, pady = 20)
    
    arrow = Label(mainframe, image=arrowPhoto)
    arrow.grid(row = 3, column = 2, pady = 20, sticky = "N")
    
    defFrame = LabelFrame(mainframe, text = "Definition", font=("Helvetica",15))
    defFrame.grid(row = 3, column = 3, padx = 50, pady = 20)
    
    definition = Label(defFrame, text = "A book or electronic resource that lists the words\nof a language (typically in alphabetical order)\nand gives their meaning, or gives the\nequivalent words in a different language,\noften also providing information\nabout pronunciation, origin, and usage.")
    definition.grid(row = 4, column = 3, padx = 50, pady = 20)

    heading2 = Label(mainframe, text = "Python Dictionaries:", font=("Helvetica",25))
    heading2.grid(row = 5, column = 1, columnspan = 3, padx = 50, pady = 20)
    
    keyFrame = LabelFrame(mainframe, text = "Key", font=("Helvetica",15))
    keyFrame.grid(row = 6, column = 1, padx = 50, pady = 20, sticky = "N")
    
    key = Label(keyFrame, text = "\"Dictionary\"")
    key.grid(row = 7, column = 1, padx = 50, pady = 20)
    
    arrow2 = Label(mainframe, image=arrowPhoto)
    arrow2.grid(row = 6, column = 2, pady = 20, sticky = "N")
    
    valueFrame = LabelFrame(mainframe, text = "Value", font=("Helvetica",15))
    valueFrame.grid(row = 6, column = 3, padx = 50, pady = 20)
    
    value = Label(valueFrame, text = "\"A wonderful book,\nfull of wonders and knowledge\"")
    value.grid(row = 7, column = 3, padx = 50, pady = 20)
    
    nextSceneLabel = Label(mainframe, text = "Next >>>")
    nextSceneLabel.grid(row = 8, column = 1, columnspan = 4, sticky = "SE")
    nextSceneLabel.bind("<Enter>", nextScreen)

def Scene2():
    def nextScene(event, param):
        canvas.grid_remove()
        group1.grid_remove()
        group2.grid_remove()
        instructions.grid_remove()
        prevSceneLabel.grid_remove()
        nextSceneLabel.grid_remove()
        if param == 1:
            Scene1()
        else:
            Scene3()
    group1 = LabelFrame(mainframe, text = "Input")
    inputEntry = Entry(group1, width = 10, textvariable = InputVar)
    group1.grid(row = 2, column = 1, padx = 20, pady = 20)
    inputEntry.grid(row = 3, column = 1, padx = 20, pady = 20)
    createDrawing()
        
    group2 = LabelFrame(mainframe, text = "Output")
    OutputEntry = Label(group2, width = 10, textvariable = OutputVar)
    group2.grid(row = 2, column = 3, padx = 20, pady = 20)
    OutputEntry.grid(row = 3, column = 3, padx = 20, pady = 20)

    instructions = Label(mainframe, text = "Type in a key number and the output\nwill be that key's value", font = ("Helvetica", 20))
    instructions.grid(row = 4, column = 1, columnspan = 3, padx = 20, pady = 20)

    prevSceneLabel = Label(mainframe, text = "<<< Back")
    prevSceneLabel.grid(row = 5, column = 1, sticky = "SW")
    prevSceneLabel.bind("<Enter>", functools.partial(nextScene, param=1))

    nextSceneLabel = Label(mainframe, text = "Next >>>")
    nextSceneLabel.grid(row = 5, column = 2, columnspan = 2, sticky = "SE")
    nextSceneLabel.bind("<Enter>", functools.partial(nextScene, param=2))

def Scene3():
    def prevScene(event):
        for i in xrange(len(codeLabels)):
            codeLabels[i].grid_remove()
        group1.grid_remove()
        group2.grid_remove()
        group3.grid_remove()
        responseLabel.grid_remove()
        infoLabel.grid_remove()
        infoLabel2.grid_remove()
        prevSceneLabel.grid_remove()
        Scene2()
        
    codeResponses = ["The variable name,\nwhere the dictionary is stored", "Assignment Operator", "Opening Bracket", "Keys", "", "Values", "Closing Bracket", "Print statement", "Variable name", "Key", "Returned value of key\nIn this case would be 1"]
    dictionaryCode = ["myDict", " = ", "{", "\"A\"\n\"B\"\n\"C\"\n\"D\"\n\"E\"", ":\n:\n:\n:\n:", "1\n2\n3\n4\n5", "}", "print ", "myDict", "[\"A\"]", "-> 1"]
    dictionaryMethods = ["myDict = {1:\"A\", 2:\"B\", 3:\"C\", 4:\"D\", 5:\"E\"}", "myDict[1] -> \"A\"", "myDict.keys() -> [1, 2, 3, 4, 5]", "dict.values() -> [\"A\", \"B\", \"C\", \"D\", \"E\"]", "myDict.has_key(1) -> True", "dict.pop(1)"]
    methodResponses = ["Initializes the dictionary", "Returns the key's\ncorresponding value", "Returns a list of all the keys", "Returns a list of all the values", "Checks if the dictionary\ncontains the key specified", "Removes the key and its value"]
    
    emptys = []

    def CodeResponse(event, param):
        responseLabel.configure(text = codeResponses[param])

    def MethodResponse(event, param):
        responseLabel.configure(text = methodResponses[param])

    def CodeEnter(event):
        responseLabel.configure(text = "The code to initialize\na dictionary")

    def CodeLeave(event):
        responseLabel.configure(text = "")

    def RunnerEnter(event):
        responseLabel.configure(text = "Uses the dictionary,\nusually within the main function")

    def RunnerLeave(event):
        responseLabel.configure(text = "")

    def MethodsEnter(event):
        responseLabel.configure(text = "Some sample methods that can be used with dictionaries")

    def MethodsLeave(event):
        responseLabel.configure(text = "")

    for i in xrange(10):
        emptys.append(Label(mainframe, text = ""))

    group1 = LabelFrame(mainframe, text = "The Code")
    group1.bind("<Enter>", CodeEnter)
    group1.bind("<Leave>", CodeLeave)
    group2 = LabelFrame(mainframe, text = "The Runner")
    group2.bind("<Enter>", RunnerEnter)
    group2.bind("<Leave>", RunnerLeave)
    codeLabels = []
    for i in xrange(len(dictionaryCode)-4):
        codeLabels.append(Label(group1, text = dictionaryCode[i]))
    for i in xrange(len(dictionaryCode)-4, len(dictionaryCode)):
        codeLabels.append(Label(group2, text = dictionaryCode[i]))
    for i in xrange(len(codeLabels)):
        codeLabels[i].bind("<Enter>", functools.partial(CodeResponse, param = i))
    group1.grid(row = 2, column = 1, columnspan = 7, padx = 100, pady = 50)
    group2.grid(row = 3, column = 1, columnspan = 7, padx = 100, pady = 50)
        
    for i in xrange(3):
        codeLabels[i].grid(row = 2, column = 1+i, pady = 20, sticky = "NE")
    for i in range(3, 6):
        codeLabels[i].grid(row = 2, column = 1+i, pady = 20)
    codeLabels[6].grid(row = 2, column = 8, pady = 20, sticky = "SW")
    codeLabels[7].grid(row = 3, column = 1, pady = 20)
    codeLabels[8].grid(row = 3, column = 2, pady = 20)
    codeLabels[9].grid(row = 3, column = 3, pady = 20)
    codeLabels[10].grid(row = 3, column = 4, pady = 20)
    
    group3 = LabelFrame(mainframe, text = "Dictionary Methods")
    group3.bind("<Enter>", MethodsEnter)
    group3.bind("<Leave>", MethodsLeave)
    methodLabels = []
    for i in xrange(len(dictionaryMethods)):
        methodLabels.append(Label(group3, text = dictionaryMethods[i]))
    for i in xrange(len(methodLabels)):
        methodLabels[i].bind("<Enter>", functools.partial(MethodResponse, param = i))
    group3.grid(row = 2, column = 8, padx = 100, pady = 50)
    for i in xrange(len(methodLabels)):
        methodLabels[i].grid(row = 6+i, column = 8, sticky = "W")

    responseLabel = Label(mainframe, text = "", font = ("Helvetica", 15))
    responseLabel.grid(row = 3, column = 8, padx = 50, pady = 20)

    infoLabel = Label(mainframe, text = "Hover over each part for description", font = ("Helvetica", 20))
    infoLabel.grid(row = 5, column = 1, columnspan = 8, pady = 10)

    infoLabel2 = Label(mainframe, text = "\" -> \" shows what the code returns or prints", font = ("Helvetica", 17))
    infoLabel2.grid(row = 6, column = 1, columnspan = 8, pady = 20)

    prevSceneLabel = Label(mainframe, text = "<<< Back")
    prevSceneLabel.grid(row = 7, column = 1, sticky = "SW")
    prevSceneLabel.bind("<Enter>", prevScene)

InputVar = StringVar()
OutputVar = StringVar()
Scene1()

def scene2Entry(*args):
    global myDict
    createDrawing()
    if InputVar.get().isdigit():
        value = int(InputVar.get())
        if value < 6 and value > 0:
            OutputVar.set(myDict[value])
            createLine(value)
        else:
            OutputVar.set("Error")
    else:
        OutputVar.set("Error")

    
InputVar.trace("w", scene2Entry)
root.mainloop()

