"""
Leila Lopez Marks
2/9/21
GUI Project
"""

from tkinter import *
master = Tk()
master.title("Test Window")
master.geometry("600x600")
# Change the label text
def show():
    label.config(text=clicked.get())

# Dropdown menu options
options = [
    "Monday",
]
# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Monday")

# Create Dropdown menu
drop = OptionMenu(master, clicked, *options)
drop.grid()

# Create button, it will change label text
button = Button(master, text="click Me", command=show).grid()

# Create Label
label = Label(master, text=" ")
label.grid()

master.configure(background="red")

def printfun():
    print("button1")
win = Canvas(master, width="300", height="300")
win.grid()


def lines():
    canvas_height = 20
    canvas_width = 200
    y = int(canvas_height / 2)
    x1 = 50
    x2 = 200
    y1 = 50
    y2 = 50
    master.create_line(x1, y1, x2, y2)
    master.create_line(x1, y1+counter, x2, y2+counter)
    counter = +50
#master.create_line(0, y, canvas_width, y)
x1 = 50
x2 = 200
y1 = 50
y2 = 50
win.create_line(x1, y1, x2, y2)
win.create_line(x1, y1+50, x2, y2+50)
for x in range(0, 100, 10):
    win.create_line(x1, y1, x2, y2)
    win.create_line(x1, y1 + x, x2, y2 + x)

draw_line_button = Button(master, text= "draw line", command=lines , bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
draw_line_button.grid(row=1, column=1)
delete_line_button = Button(master, text= "delete line", command=lines , bg="brown4", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
delete_line_button.grid(row=2, column=1)
draw_diagonal_line_button = Button(master, text= "draw diagonal line", command=lines , bg="purple3", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
draw_diagonal_line_button.grid(row=3, column=1)
draw_squiggle_line_button = Button(master, text= "draw squiggle line", command=lines , bg="gold", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
draw_squiggle_line_button.grid(row=4, column=1)

win = Scale(master, from_=300, to=400, orient=HORIZONTAL)
win = Scale(master, from_=0, to=42)

Label(master, text='Line drawer').grid(row=1, column=0)
Label(master, text='Line deleter').grid(row=2, column=0)
Label(master, text='Diagonal line drawer').grid(row=3, column=0)
Label(master, text='Squiggle line drawer').grid(row=4, column=0)

Checkbutton(master, text='Line drawn').grid(row=1, column=2)
Checkbutton(master, text='Line deleted').grid(row=2, column=2)
Checkbutton(master, text='Diagonal line drawn').grid(row=3, column=2)
Checkbutton(master, text='Squiggle line drawn').grid(row=4, column=2)

top = Toplevel()
top.title('Python')


#scrollbar = Scrollbar(win)
#scrollbar.grid( side = RIGHT, fill = Y )
#mylist = Listbox(win, yscrollcommand = scrollbar.set )
#for line in range(100):
 #  mylist.insert(END, 'This is line number' + str(line))
#mylist.grid( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )

win = Spinbox(master, from_ = 0, to = 10)
win.grid()

# Create text widget and specify size.
Label(win, text = "text box")

#v = IntVar()
#Radiobutton(win, text='GfG', variable=v, value=1).grid(anchor=win)
#Radiobutton(win, text='MIT', variable=v, value=2).grid(anchor=win)
master.mainloop()