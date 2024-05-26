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
  