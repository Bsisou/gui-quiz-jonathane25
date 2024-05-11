from tkinter import *

root = Tk() 

# Adjust size  
root.geometry("1920x1080") 

# Add image file 
bg = PhotoImage(file = "Homepage.png")

# Create Canvas 
canvas1 = Canvas( root, width = 1920, height = 1080) 
canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

#the buttons
button1 = Button(root, text = "Start")
button2 = Button(root, text = "Help")

#show buttons
button1_canvas = canvas1.create_window(100,10,
                                      anchor = "nw",
                                      window = button1)
button2_canvas = canvas1.create_window(100,10,
anchor = "nw",
window = button2)

#where the button is placed
button1.place(x=430, y=310)
button2.place(x=1030, y=596)

#button size
button1.config(width=16, height=2)
button2.config(width=8, height=2)

#background colour of button
button1.config(bg="white")
button2.config(bg="white")

#font and size of text in buttons in window 1 (homepage)
button1.config(font=("Georgia", 30))
button2.config(font=("Georgia", 30))

#start button leading to new window
def open_new_window():
    new_window = Toplevel(root)
    new_window.title("Question 1")
    new_window.geometry("1280x720")

    label = Label(new_window, text = "Question 1")
    label.pack()
button1.config(command=open_new_window)

#help button leading to new window
def open_new_window():
    new_window = Toplevel(root)
    new_window.title("Help")
    new_window.geometry("1280x720")

    label = Label(new_window, text = "Help")
    label.pack()
button2.config(command=open_new_window)

#window 2



# Execute tkinter 
root.mainloop()