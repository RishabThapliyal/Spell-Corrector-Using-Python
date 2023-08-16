from tkinter import *
from textblob import TextBlob


def correct_spelling():
    corr = TextBlob(entry1.get())  # entry.get() <- incorrect spelling
    data = corr.correct()  # data <- correct spelling
    entry2.delete(0, END)  # delete data
    entry2.insert(0, data)  # insert data


def main_window():
    global entry1, entry2
    win = Tk()
    win.geometry('450x250')
    win.resizable(False, False)
    win.config(bg="Grey")
    win.title("My Spell Checker Project")

    label1 = Label(win, text="Enter the Word", font=("Time New Roman", 22, "bold"), bg="Black", fg="white")
    label1.place(x=65, y=10, height=35, width=320)

    entry1 = Entry(win, font=("Time New Roman", 15))
    entry1.place(x=40, y=55, height=30, width=370)

    label2 = Label(win, text="Correct Spelling", font=("Time New Roman", 22, "bold"), bg="Black", fg="white")
    label2.place(x=65, y=95, height=35, width=320)

    entry2 = Entry(win, font=("Time New Roman", 15))
    entry2.place(x=40, y=145, height=30, width=370)

    button = Button(win, text="Done", font=("Time New Roman", 21, "bold"), bg="Gold", command=correct_spelling)
    button.place(x=140, y=185, height=40, width=170)

    win.mainloop()


main_window()
