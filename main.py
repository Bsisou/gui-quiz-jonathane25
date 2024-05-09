from tkinter import *

root = Tk() 

# Adjust size  
root.geometry("1920x1080") 

# Add image file 
bg = PhotoImage(file = "Homepage.png")

# Show image using label 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 

# Execute tkinter 
root.mainloop()