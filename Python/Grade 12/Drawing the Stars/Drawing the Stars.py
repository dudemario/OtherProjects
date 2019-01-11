'''
Day 5 & 6
File IO Lesson
Read in and draw all the stars from the Northern Sky

Sept 18
'''
from Tkinter import *
starsFile = open("stars.txt", "r")
constellationsFile = open("constellations.txt", "r")
allStars = []
allNamedStars = {}
#generate a list of lists
#big list holds all the stars in the file.
#each star is stored as a list

for line in starsFile:
    t = line.split(" ",6)
    t[0] = float(t[0])#change data type of x, y coordinate to float
    t[1] = float(t[1])
    t.pop(2)#delete z coordinate
    t[2] = float(t[2])#change data draper number to int
    t[3] = float(t[3])#change magnitude number to int
    t[4] = float(t[4])#change harvard number to int
    if len(t)>5:
        names = t[5].split(";")
        t.pop(5)
        for name in names:
            t.append(name.strip())
            t2 = []
            for item in t:
                t2.append(item)
            allStars.append(t2)
            allNamedStars[t2[5]] = t2
            #print allNamedStars
            t.pop(5)
    else:
        allStars.append(t)
        
cWidth = 500
cHeight = 500
root = Tk()
mainframe = Frame(root)
w = Canvas(root, width=cWidth, height=cHeight)
w.create_rectangle(0, 0, cWidth, cHeight, fill="black")
for star in allStars:
    cRadius = star[3]/4
    cX = cWidth/2*star[0]+cWidth/2
    cY = -cHeight/2*star[1]+cHeight/2
    w.create_oval(cX-cRadius, cY-cRadius, cX+cRadius, cY+cRadius, fill="white")

#9,24, 31, 49, 64, 83, 99
for line in constellationsFile:
    #print line
    connection = line.split(",")
    star1 = allNamedStars[connection[0]]
    cX1 = cWidth/2*star1[0]+cWidth/2
    cY1 = -cHeight/2*star1[1]+cHeight/2
    star2 = allNamedStars[connection[1].strip()]
    cX2 = cWidth/2*star2[0]+cWidth/2
    cY2 = -cHeight/2*star2[1]+cHeight/2
    #print star1, star2
    w.create_line(cX1, cY1, cX2, cY2, fill="yellow", width = 1)
#mainframe.grid()
def changeLabel(event):
    myLabel.configure(text="Hi")
w.grid(column = 0, row = 0)
starsFile.close()
'''
myLabel = Label(root, text="Red Sun", bg="red", fg="white")
myLabel.grid(column = 1, row  = 0, padx = 50)
myLabel.bind("<Enter>", changeLabel)
'''
mainframe.mainloop()

