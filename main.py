import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style
from quiz_data import quiz_data
from PIL import Image, ImageTk

#global variables for current question and score
current_question = 0
score = 0
return_to_quiz_flag = False

#Function to Display the questions and choices
def show_question():
    global background_photo
    #Get data from quiz_data
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    #Show choices on buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    #Clear feedback(correct or wrong) Disable Next button
    feedback_label.config(text="")
    next_btn.config(state ="disabled")

    #Update backgroun image
    background_image = Image.open(question["background"])
    background_image = background_image.resize((1280, 720), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)
    quiz_background_label.config(image=background_photo)
    quiz_background_label.image = background_photo

#Function to check the answer the user has selected and provide the user with feedback
def check_answer(choice):
    global score
    #Get the current question from quiz_data.py
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    #Check if users selected answer matches with the correct answer
    if selected_choice == question["answer"]:
        #Update score and show
        score +=1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_lbael.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    #Disable all the choice buttons and only allow the next button 
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

#Move to Next Question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        #If there is more question show them
        show_question()
    else:
        #if all questions have been answered by user show the final score and finish/end the quiz
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Fnal Score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

#START Quiz (homepage)
def start_quiz():
    global current_question
    global score

    #Resetting the score and question number when user has clicked restart/main menu HERE!!!!
    score = 0
    current_question = 0

    # Hide the home window and show quiz window
    home_window.withdraw()
    show_question()
    root.deiconify()

#Function to show the help window
def show_help(rerturn_to_quiz=False):
    global return_to_quiz_flag
    return_to_quiz_flag = return_to_quiz_flag
    help_window.deiconify()
    if return_to_quiz:
        root.withdraw()
        return_quiz_button.pack(pady=10)
        return_home_button.pack_forget()
    else:
        home_window.withdraw()
        return_quiz_button.pack_forget()
        return_home_button.pack(pady=10)

#Function to return to the homepage
def return_to_home():
    global current_question, score
    current_question = 0
    score = 0
    help_window.withdraw()
    setup_home_window()
    home_window.deiconify()

#Function to return to the quiz from help window
def return_to_quiz():
    help_window.withdraw()
    root.deiconify()

#Function to return to Main Menu from quiz HERE!!!
def return_to_main_menu_from_quiz():
    global current_question, score
    current_question = 0
    score = 0
    root.withdraw()
    setup_homewindow()
    home_window.deiconify()

#Function that will set up the home window
def setup_home_window():
    global background_photo
    background_image = Image.open("homepage.png")
    background_image = background_image.resize((1280,720), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label.config(image=background_photo)
    background_label.image = background_photo

#Make the main window for quiz (homepage)
root = tk.Tk()
root.title("Quiz App")
root.geometry("1280x720")
style = Style(theme="flatly")

#Size of the font for question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Make a background label for quiz window HERE
quiz_background_label = tk.Label(root)
quiz_background_label.place(relwidth=1, relheight=1)

#Maake a frame to hold question and choice 
quiz_frame = tk.Frame(root, bg='white', bd=5)
quiz_frame.place(relx=0.5, rely=0.5, anchor='center')

#Create question label
qs_label = ttk.Label(
    quiz_frame,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

#Make choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        quiz_frame,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

#Make feedback label
feedback_label = ttk.Label(
    quiz_frame,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

#Create the score label
score_label = ttk.Label(
    quiz_frame,
    text="score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

#Make next button
next_btn = ttk.Button(
    quiz_frame,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

#Make help button on quiz window
help_button_quiz = tk.Button(root, text="help", font=("Helvetica", 16), command=lambda: show_help(True))
help_button_quiz.place(relx=0.9, rely=0.1, anchor='center')

#Make return to main menu button from quiz window
return_main_menu_button = tk.Button(root, text="Return to Main Menu", font=("Helvetica", 16), command=return_to_main_menu_from_quiz)
return_main_menu_button.place(relx=0.1, rely=0.1, anchor='center')

#Hide quiz window if user clicks on this button
root.withdraw()

#Mame home window
home_window = tk.Toplevel()
home_window.title("Jonny's Flag Quiz")
home_window.geometry("1280x720")

#Load and display image for home window
background_label = tk.Label(home_window)
background_label.place(relwidth=1, relheight=1)
setup_home_window()


# Start the main event loop
root.mainloop()