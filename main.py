import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from quiz_data import quiz_data
import re

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0
        self.return_to_quiz_flag = False
        self.background_photo = None

        # Initialize the GUI
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Quiz App")
        self.root.geometry("1280x720")
        self.style = Style(theme="flatly")

        # Configure the font size for the question and choice buttons
        self.style.configure("TLabel", font=("Helvetica", 20))
        self.style.configure("TButton", font=("Helvetica", 16))

        # Create the background label for the quiz window
        self.quiz_background_label = tk.Label(self.root)
        self.quiz_background_label.place(relwidth=1, relheight=1)

        # Create a frame to hold the question and choice widgets
        self.quiz_frame = tk.Frame(self.root, bg='white', bd=5)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create the question label
        self.qs_label = ttk.Label(
            self.quiz_frame,
            anchor="center",
            wraplength=500,
            padding=10
        )
        self.qs_label.pack(pady=10)

        # Create the choice buttons
        self.choice_btns = []
        for i in range(4):
            button = ttk.Button(
                self.quiz_frame,
                command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5)
            self.choice_btns.append(button)

        # Create the feedback label
        self.feedback_label = ttk.Label(
            self.quiz_frame,
            anchor="center",
            padding=10
        )
        self.feedback_label.pack(pady=10)

        # Create the score label
        self.score_label = ttk.Label(
            self.quiz_frame,
            text="Score: 0/{}".format(len(quiz_data)),
            anchor="center",
            padding=10
        )
        self.score_label.pack(pady=10)

        # Create the next button
        self.next_btn = ttk.Button(
            self.quiz_frame,
            text="Next",
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack(pady=10)

        # Create the help button for the quiz window
        self.help_button_quiz = tk.Button(self.root, text="Help", font=("Helvetica", 18), command=lambda: self.show_help(True))
        self.help_button_quiz.place(relx=0.89, rely=0.08, anchor='center', width=240, height=60)

        # Create the return to main menu button for the quiz window
        self.return_main_menu_button = tk.Button(self.root, text="Return to Main Menu", font=("Helvetica", 16), command=self.return_to_main_menu_from_quiz)
        self.return_main_menu_button.place(relx=0.02, rely=0.04, anchor='nw', width=240, height=60)

        # Initially hide the quiz window
        self.root.withdraw()

        # Create the home window
        self.home_window = tk.Toplevel()
        self.home_window.title("Jonny's Flag Country Quiz")
        self.home_window.geometry("1280x720")

        # Load and display the background image for the home window
        self.background_label = tk.Label(self.home_window)
        self.background_label.place(relwidth=1, relheight=1)
        self.setup_home_window()

        # Create a frame for the input and start button
        self.frame = tk.Frame(self.home_window, bg='#ffffff', bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create a label and entry for the user's name
        self.name_label = tk.Label(self.frame, text="Enter your name:", font=("Helvetica", 20))
        self.name_label.pack(pady=10)
       
        self.name_entry = tk.Entry(self.frame, font=("Helvetica", 20))
        self.name_entry.pack(pady=10)

        # Create the start button
        self.start_button = tk.Button(self.frame, text="Start Quiz", font=("Helvetica", 20), command=self.start_quiz)
        self.start_button.pack(pady=10)

        # Create the help button for the home window
        self.help_button_home = tk.Button(self.home_window, text="Help", font=("Helvetica", 32), command=lambda: self.show_help(False))
        self.help_button_home.place(relx=0.9, rely=0.9, anchor='center')

        # Create the help window
        self.help_window = tk.Toplevel()
        self.help_window.title("Help")
        self.help_window.geometry("1280x720")

        # Load and display the background image for the help window
        self.help_background_image = Image.open("help.png")
        self.help_background_image = self.help_background_image.resize((1280, 720), Image.LANCZOS)
        self.help_background_photo = ImageTk.PhotoImage(self.help_background_image)
        self.help_background_label = tk.Label(self.help_window, image=self.help_background_photo)
        self.help_background_label.place(relwidth=1, relheight=1)

        # Create a frame for the help buttons
        self.help_frame = tk.Frame(self.help_window, bg='#ffffff', bd=5)
        self.help_frame.place(relx=0.05, rely=0.05, anchor='nw')

        # Create the return to main menu button for help page from homewindow
        self.return_home_button = tk.Button(self.help_frame, text="Return to Main Menu", font=("Helvetica", 20), command=self.return_to_home)
        self.return_home_button.place(relx=0.02, rely=0.04, anchor='nw', width=140, height=60)

        # Create the return to quiz button
        self.return_quiz_button = tk.Button(self.help_frame, text="Return to Quiz", font=("Helvetica", 20), command=self.return_to_quiz)
        self.return_quiz_button.pack_forget()

        # Initially hide the help window
        self.help_window.withdraw()

    def show_question(self):
        # Get the current question from the quiz_data list
        question = quiz_data[self.current_question]
        self.qs_label.config(text=question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            self.choice_btns[i].config(text=choices[i], state="normal")  # Reset button state

        # Clear the feedback label and disable the next button
        self.feedback_label.config(text="")
        self.next_btn.config(state="disabled")

        # Update the background image
        background_image = Image.open(question["background"])
        background_image = background_image.resize((1280, 720), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.quiz_background_label.config(image=self.background_photo)
        self.quiz_background_label.image = self.background_photo

    def check_answer(self, choice):
        # Get the current question from the quiz_data list
        question = quiz_data[self.current_question]
        selected_choice = self.choice_btns[choice].cget("text")

        # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
            # Update the score and display it
            self.score += 1
            self.score_label.config(text="Score: {}/{}".format(self.score, len(quiz_data)))
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            self.feedback_label.config(text="Incorrect!", foreground="red")

        # Disable all choice buttons and enable the next button
        for button in self.choice_btns:
            button.config(state="disabled")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(quiz_data):
            # If there are more questions, show the next question
            self.show_question()
        else:
            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed", "Quiz Completed! Final score: {}/{}".format(self.score, len(quiz_data)))
            self.root.destroy()

    def start_quiz(self):
        #Get the users name that they entered before
        name = self.name_entry.get()

        # Check if the name passes the rules (only letters and numbers)
        if not re.match("^[a-zA-Z0-9]{3,12}$", name):
            self.show_invalid_name_message()
            return
    
        # Reset score and question index
        self.score = 0
        self.current_question = 0

        # Hide the home window and show the quiz window
        self.home_window.withdraw()
        self.show_question()
        self.root.deiconify()

    def show_invalid_name_message(self):
        #Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #work out centeer of the screen
        x = (screen_width - 300) // 2
        y = (screen_height - 150) // 2

        #Make te message box in middle of sreen.
        messagebox.showerror("Invalid Name", "Please enter a Valid Name - Only Letters and Numbers are allowed, and it must be between 3 and 12 characters. Press OK to continue", parent=self.home_window)
    
    def show_help(self, return_to_quiz=False):
        self.return_to_quiz_flag = return_to_quiz
        self.help_window.deiconify()
        if return_to_quiz:
            self.root.withdraw()
            self.return_quiz_button.pack(pady=10)
            self.return_home_button.pack_forget()
        else:
            self.home_window.withdraw()
            self.return_quiz_button.pack_forget()
            self.return_home_button.pack(pady=10)

    def return_to_home(self):
        self.current_question = 0
        self.score = 0
        self.help_window.withdraw()
        self.setup_home_window()
        self.home_window.deiconify()

    def return_to_quiz(self):
        self.help_window.withdraw()
        self.root.deiconify()

    def return_to_main_menu_from_quiz(self):
        self.current_question = 0
        self.score = 0
        self.root.withdraw()
        self.setup_home_window()
        self.home_window.deiconify()

    def setup_home_window(self):
        background_image = Image.open("homepage.png")
        background_image = background_image.resize((1280, 720), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_label.config(image=self.background_photo)
        self.background_label.image = self.background_photo

# Create the main window
root = tk.Tk()

# Create the QuizApp instance
quiz_app = QuizApp(root)

# Start the main event loop
root.mainloop()
