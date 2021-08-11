import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import image
# import geopandas
# import geoplot
# import mapclassify
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.models import ColumnDataSource
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

x = 0
y = 0
window = tk.Tk()
frame = tk.Frame(master=window, bg="midnight blue")
frame.pack(fill=tk.BOTH, expand=True)
frame.pack()
# new = Toplevel(window)
image = mpimg.imread("pic.jpg")
# img = PhotoImage(file='map.png')
window.geometry("750x550")
Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=15)
greeting = tk.Label(frame, text="Welcome to Covid assistant", font=(
    'Helvetica 20 bold'), fg="turquoise", bg="midnight blue")
greeting.pack()

Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=17)
label1 = tk.Label(frame, text="Username", width=20, font=(
    'Helvetica 17 bold'), fg="white", bg="midnight blue")
label2 = tk.Label(frame, text="Password", width=20, font=(
    'Helvetica 17 bold'), fg="white", bg="midnight blue")
entry2 = tk.Entry(frame, show="*", fg="deeppink", bg="white",
                  width=20, font=('Helvetica 17 bold'))
entry1 = tk.Entry(frame, fg="deeppink", bg="white",
                  width=20, font=('Helvetica 17 bold'))
label1.pack()
entry1.pack()
username = entry1.get()  # username get from user
label2.pack()
entry2.pack()
password = entry2.get()  # pass get from user


def showMsg():
    # if output!=0
    messagebox.showinfo(None, " Login successfuly ")


def open_win_map():
    new = Toplevel(frame)
    frame4 = tk.Frame(master=new, bg="midnight blue")
    frame4.pack(fill=tk.BOTH, expand=True)
    frame4.pack()
    # new.geometry("750x550")
    new.title("Map")
    fig = plt.Figure(figsize=(15, 15))
    plot1 = fig.add_subplot(111)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-0TH5LFS;'
                          'Database=SE_project;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('return_x_y ' + ';')
    records = cursor.fetchall()
    tot = len(records)
    plot1.imshow(image)
    color = ['red', 'green']
    for row in records:
        plot1.plot(np.array(row[0]), np.array(row[1]), "or", markersize=10, color=color[row[2]])
    conn.close()
    canvas = FigureCanvasTkAgg(fig,
                               master=frame4)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame4)
    toolbar.update()
    canvas.get_tk_widget().pack()
    # img = PhotoImage(file='k.png')

    #  plt.scatter(np.array(row[0]), np.array(row[1]), marker="x", color="red", s=200)


# input:
# Gender-> Male:1, Transgender:2, Female: 3
# Contact-> No:1, Don't-Know:2, Yes:3
# Age-> 0-9:1, 10-19:2, 20-24:3, 25-59:4, 60+:5
# Fever-> yes:1, no:0
# Tiredness-> yes:1, no:0
# Dry-cough-> yes:1, no:0
# Difficulty-in-breathing-> yes:1, no:0
# Sore-Throat-> yes:1, no:0
# Pains-> yes:1, no:0
# Nasal-Congestion-> yes:1, no:0
# Runny_Nose-> yes:1, no:0
# Diarrhea-> yes:1, no:0
# output:
# probability of being infected in scale of 0 to 100

def diagnose(features):
    arr = np.array([features]).astype('float')
    arr[0, 0] = arr[0, 0] / 6
    arr[0, 1] = arr[0, 1] / 6
    arr[0, 2] = arr[0, 2] / 20
    coef = np.array([[-0.02752593, 0.03977402, 0.02206546, -0.00929782, 0.01594905,
                      -0.00560558, -0.02683619, 0.00352665, -0.00270834, -0.02176323,
                      0.01276784, -0.00998991]])
    intercept = 1.10297915
    if np.sum(arr[0, 3:11]) == 0 and arr[0, 1] == 1 / 6:
        ret_value = 5.491
    elif np.sum(arr[0, 3:11]) == 0 and arr[0, 1] == 2 / 6:
        ret_value = 30.323
    else:
        ret_value = float(1 / (1 + np.exp(-1 * (intercept + np.sum(np.multiply(coef, arr)))))) * 100
    return np.round(ret_value, 3)


def open_win_predict():
    # messagebox.showinfo(None, " predict ")
    new = Toplevel(frame)
    frame2 = tk.Frame(master=new, bg="purple")
    frame2.pack(fill=tk.BOTH, expand=True)
    frame2.pack()
    # new.geometry("900x3000")
    new.title("Symptoms")
    label_gender = tk.Label(frame2, text="answer each question by entering the respective number", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    label_gender = tk.Label(frame2, text="Gender-> Male:1, Transgender:2, Female: 3", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_gender = tk.Entry(frame2, fg="deeppink", bg="white",
                            width=50, font=('Helvetica 9'))
    entry_gender.pack()
    label_contact = tk.Label(frame2, text="Contact-> No:1, Don't-Know:2, Yes:3", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_contact = tk.Entry(frame2, fg="deeppink", bg="white",
                             width=50, font=('Helvetica 9'))
    entry_contact.pack()
    label_age = tk.Label(frame2, text="Age-> 0-9:1, 10-19:2, 20-24:3, 25-59:4, 60+:5", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_age = tk.Entry(frame2, fg="deeppink", bg="white",
                         width=50, font=('Helvetica 9'))
    entry_age.pack()
    label_fever = tk.Label(frame2, text="Fever-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_fever = tk.Entry(frame2, fg="deeppink", bg="white",
                           width=50, font=('Helvetica 9'))
    entry_fever.pack()
    label_tiredness = tk.Label(frame2, text="Tiredness-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_tiredness = tk.Entry(frame2, fg="deeppink", bg="white",
                               width=50, font=('Helvetica 9'))
    entry_tiredness.pack()
    label_drycough = tk.Label(frame2, text="Dry_cough-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_drycough = tk.Entry(frame2, fg="deeppink", bg="white",
                              width=50, font=('Helvetica 9 '))
    entry_drycough.pack()

    label_difficulty_in_breathing = tk.Label(frame2, text="Difficulty-in-breathing-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_difficulty_breath = tk.Entry(frame2, fg="deeppink", bg="white",
                                       width=50, font=('Helvetica 9'))
    entry_difficulty_breath.pack()
    label_Sore_Throat = tk.Label(frame2, text="Sore-throat-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_sore_throat = tk.Entry(frame2, fg="deeppink", bg="white",
                                 width=50, font=('Helvetica 9'))
    entry_sore_throat.pack()
    label_pains = tk.Label(frame2, text="Pains-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_pains = tk.Entry(frame2, fg="deeppink", bg="white",
                           width=50, font=('Helvetica 9'))
    entry_pains.pack()
    label_nasal_congestion = tk.Label(frame2, text="Nasal-congestion-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_nasal_congestion = tk.Entry(frame2, fg="deeppink", bg="white",
                                      width=50, font=('Helvetica 9'))
    entry_nasal_congestion.pack()
    label_runny_nose = tk.Label(frame2, text="Runny-nose-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_runny_nose = tk.Entry(frame2, fg="deeppink", bg="white",
                                width=50, font=('Helvetica 9'))
    entry_runny_nose.pack()
    label_Diarrhea = tk.Label(frame2, text="Diarrhea-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="midnight blue", bg="pink").pack()
    entry_diarrhea = tk.Entry(frame2, fg="deeppink", bg="white",
                              width=50, font=('Helvetica 9'))
    entry_diarrhea.pack()

    def predict_symp():
        in_val = [entry_gender.get(), entry_contact.get(), entry_age.get(), entry_fever.get(),
                  entry_tiredness.get(), entry_drycough.get(), entry_difficulty_breath.get(),
                  entry_sore_throat.get(), entry_pains.get(), entry_nasal_congestion.get(),
                  entry_runny_nose.get(), entry_diarrhea.get()]
        messagebox.showinfo(None, "probability of infection: " + str(diagnose(in_val)))
        new.destroy()
        # call function with symptoms values

    submit_symp = Button(frame2, width=50, pady=10, font=('Helvetica 13 bold'),
                         fg="black", bg="deeppink", text="Submit", command=predict_symp).pack()


def open_win():
    # call databasefunc(username,password)
    # if output!=0
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-0TH5LFS;'
                          'Database=SE_project;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    username = entry1.get()
    password = entry2.get()
    cursor.execute('execute u_p_check ' + str(username) +
                   ', ' + str(password) + ';')
    for row in cursor:
        if row[0] == 1:
            for widgets in frame.winfo_children():
                widgets.destroy()
            # enter to page of services
            Label(frame, text="", bg="midnight blue",
                  font=('Helvetica 17 bold')).pack(pady=15)
            Label(frame, text="Choose your service from check list",
                  fg="turquoise", bg="midnight blue", font=('Helvetica 20 bold')).pack(pady=30)
            Label(frame, text="", bg="midnight blue",
                  font=('Helvetica 17 bold')).pack(pady=17)
            Button(frame, height=2,
                   width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Map",
                   command=open_win_map).pack()
            Label(frame, text="", bg="midnight blue",
                  font=('Helvetica 10 bold')).pack(pady=1)
            Button(frame, height=2,
                   width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise",
                   text="Prediction based on Symptoms", command=open_win_predict).pack()
            Label(frame, text="", bg="midnight blue",
                  font=('Helvetica 10 bold')).pack(pady=1)
            Button(frame, height=2,
                   width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Exit",
                   command=window.destroy).pack()

        else:
            messagebox.showinfo(None, "wrong username or password :(")
    conn.close()
    # Create a Label in New window

    # else
    # messagebox.showerror("error", "try again") #abort


# Create a label
Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=30)
# Create a button to open a New Window
tk.Button(frame, text="Login", command=open_win, width=20, font=(
    'Helvetica 17 bold'), fg="midnight blue", bg="turquoise").pack()
window.mainloop()