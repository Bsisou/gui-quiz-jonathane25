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
def show_qustion():
  global background_photo
  #Get data from quiz_data
  question = quiz_data[current_question]
  qs_label.config(test=question["Question"])

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
def next_qestion():
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
  