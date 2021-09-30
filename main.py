
import datetime
from tkinter import *
from PIL import Image, ImageTk

# window
wind = Tk()
wind.geometry("390x490")
wind.title("Age Calculator")
wind.iconbitmap("window_icon.ico")

# text & pack
name = Label(text="Name")
year = Label(text="Year")
month = Label(text="Month")
date = Label(text="Day")

name.grid(column=0, row=1)
year.grid(column=0, row=2)
month.grid(column=0, row=3)
date.grid(column=0, row=4)

# data entry
name_entry = Entry()
year_entry = Entry()
month_entry = Entry()
date_entry = Entry()

name_entry.grid(column=1, row=1)
year_entry.grid(column=1, row=2)
month_entry.grid(column=1, row=3)
date_entry.grid(column=1, row=4)

# user input
def get_input():
    name = name_entry.get()
    mankey = Person(name, datetime.date(int(year_entry.get()), int(month_entry.get()), int(date_entry.get())))

    text_area = Text(master=wind, height=5, width=33)
    text_area.grid(column=1, row=6)
    answer = "Hey {mankey}! You are {age} years old!".format(mankey=name, age=mankey.age())
    text_area.insert(END, answer)

# button
butt = Button(wind, text="Calculate Age", command=get_input, bg="orange", fg="white")
butt.grid(column=1, row=5)

# class
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthday = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthday.year
        return age

# add image
picture = Image.open("img1.jpg")
picture.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(picture)
label_image = Label(image=photo)
label_image.grid(column=1, row=0, pady=10)

# close button
cl = Button(text="Close", bg="red", fg="white", command=wind.destroy)
cl.grid(column=1, row=20)


wind.mainloop()
