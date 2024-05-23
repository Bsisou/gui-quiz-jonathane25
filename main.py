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

  