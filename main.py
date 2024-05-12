import os
from tkinter import *

root = Tk()

# Adjust size
root.geometry("1280x720")

# Add image file
bg = PhotoImage(file="Homepage.png")

# Create Canvas
canvas1 = Canvas(root, width=1280, height=720)
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

# the buttons
button1 = Button(root, text="Start")
button2 = Button(root, text="Help")

# show buttons
button1_canvas = canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button1,
)
button2_canvas = canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button2,
)

# where the button is placed
button1.place(x=430, y=310)
button2.place(x=1030, y=596)

# button size
button1.config(width=16, height=2)
button2.config(width=8, height=2)

# background colour of button
button1.config(bg="white")
button2.config(bg="white")

# font and size of text in buttons in window 1 (homepage)
button1.config(font=("Georgia", 30))
button2.config(font=("Georgia", 30))

# Global variable to store question image
question_bg = None

#from start page to q1
# start button that will lead to the ne window
def open_question_window():
    global question_bg  

    new_window = Toplevel(root)
    new_window.title("Question 1")
    new_window.geometry("1280x720")

    #  working diectory
    current_directory = os.getcwd()

    # Add the image  name to the directory
    question_image_path = os.path.join(current_directory, "Question1.png")
    print("Question image path:", question_image_path)


    # Load the image on the Q1 windoww
    question_bg = PhotoImage(file=question_image_path)

    # Create Canvas for question window
    question_canvas = Canvas(new_window, width=1280, height=720)
    question_canvas.pack(fill="both", expand=True)

    # Display image for question window
    question_canvas.create_image(0, 0, image=question_bg, anchor="nw")

    label = Label(new_window, text="Question 1")
    label.pack()

    #button to return to homepage
    return_button = Button(new_window, text="Return to Main Menu", command=new_window.destroy, font=("Georgia", 20), bg="white", width=16, height=2)
    return_button.place(x=18, y=20)



button1.config(command=open_question_window)


# from start page to help page
# start button that will lead to the ne window

# Global variable to store help image
help_bg = None

def open_help_window():
    global help_bg  

    new_window = Toplevel(root)
    new_window.title("Help Page")
    new_window.geometry("1280x720")

    #  working diectory
    current_directory = os.getcwd()

    # Add the image  name to the directory
    help_image_path = os.path.join(current_directory, "help.png")
    print("Help image path:", help_image_path)

    # Check if the file exists
    if not os.path.exists(help_image_path):
        print("Error: Image file not found")
    else:
        print("Image file found!")

    # Load the image on the Help windoww
    help_bg = PhotoImage(file=help_image_path)

    # Create Canvas for help window
    help_canvas = Canvas(new_window, width=1280, height=720)
    help_canvas.pack(fill="both", expand=True)

    # Display image for help window
    help_canvas.create_image(0, 0, image=help_bg, anchor="nw")

    label = Label(new_window, text="Help")
    label.pack()

    #button to return to homepage
    return_button = Button(new_window, text="Return to Main Menu", command=new_window.destroy, font=("Georgia", 25), bg="white", width=16, height=2)
    return_button.place(x=18, y=20)

button2.config(command=open_help_window)


# Execute tkinter
root.mainloop()



