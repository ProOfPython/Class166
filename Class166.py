from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Canvas w/ Functions')
root.geometry('600x600')
root.configure(background = 'snow')

lblColor = Label(root, text = 'Enter Color:', background = 'lightblue')
lblColor.place(relx = 0.6, rely = 0.9, anchor = CENTER)

entColor = Entry(root)
entColor.insert(0, 'salmon1')
entColor.place(relx = 0.8, rely = 0.9, anchor = CENTER)

canvas = Canvas(root, width = 500, height = 450, bg = 'white', highlightbackground = 'light blue')
canvas.place(relx = 0.5, rely = 0.45, anchor = CENTER)

dir = ''
pos = [20, 20]

def trace(vector):
    global pos
    print('Traced!')
    fillColor = entColor.get()
    line = canvas.create_line(
        pos[0], 
        pos[1], 
        pos[0] + vector[0], 
        pos[1] + vector[1],
        fill = entColor.get(),
        width = 2.5   
    )

root.bind('<Up>', trace([0, -5]))
root.bind('<Down>', trace([0, 5]))
root.bind('<Left>', trace([-5, 0]))
root.bind('<Right>', trace([5, 0]))

root.mainloop()