import os
from tkinter import *

#root window
root = Tk()
root.geometry("1280x720")

#Global Variables for images
homepage_bg = None 
question1_bg = None 
help_bg = None

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_homepage():
    global homepage_bg
    clear_window()

    #Homepage bacjground
    homepage_bg = PhotoImage(file="Homepage.png")

    #Make Canvas
    canvas1 = Canvas(root,width=1280, height=720)
    canvas1.pack(fill="both", expand=True)

    #SHow Homepage image
    canvas1.create_image(0, 0, image=homepage_bg, anchor="nw")

    #buttons
    button1 = Button(root, text="Start", borderwidth=0, command=open_question1_window)
    button2 = Button(root, text="Help", command=open_help_window)

    #Display buttons on window
    button1_canvas = canvas1.create_window(100, 10, anchor="nw", window=button1)
    button2_canvas = canvas1.create_window(100, 10, anchor="nw", window=button2)

    # Place buttons
    button1.place(x=430, y=310)
    button2.place(x=1030, y=596)

    #BUTTON size and font etc...
    button1.config(width=16, height=2, bg="white", font=("Georgia", 30))
    button2.config(width=8, height=2, bg="white", font=("Georgia", 30))

def open_question1_window():
    global question1_bg
    clear_window()

    #Question image background
    question1_image_path = os.path.join(os.getcwd(), "Question1.png")
    question1_bg = PhotoImage(file=question1_image_path)

    #canvas for question1 window
    question1_canvas = Canvas(root, width=1280, height=720)
    question1_canvas.pack(fill="both", expand=True)

    #Display Question1 Image
    question1_canvas.create_image(0, 0, image=question1_bg, anchor="nw")

    label = Label(root, text="question1", font=("Georgia", 30), bg="white")
    label.pack()

    #Button to come back to homepage
    return_button = Button(root, text="Return to Main Menu", command=show_homepage, font=("Georgia", 20), bg="white", width=16, height=2)
    return_button.place(x=18, y=20)

def open_help_window():
    global help_bg
    clear_window()

    #Help image BG
    help_image_path = os.path.join(os.getcwd(), "help.png")
    help_bg = PhotoImage(file=help_image_path)

    #Canvas for help window
    help_canvas = Canvas(root, width=1280, height=720)
    help_canvas.pack(fill="both", expand=True)

    #display help image
    help_canvas.create_image(0, 0, image=help_bg, anchor="nw")

    label = Label(root, text="Help", font=("Georgia", 30), bg="white")
    label.pack()

    #button to come back to homepage
    return_button = Button(root, text="Return to Main Menu", command=show_homepage, font=("Georgia", 25), bg="white", width=16, height=2)
    return_button.place(x=18, y=20)

#show the homepage initially
show_homepage()

#Execute tkinter
root.mainloop()

    
    



















