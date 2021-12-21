from tkinter import *
import string
import random
import pyperclip

##########     Password Generator     ##########
password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0, END)
    length = 16
    password = "".join([random.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)
    pyperclip.copy(password)

##########     User Interface     ##########
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="#383e56")

label_title = Label(text="Password Generator",
                    bg="#383e56",
                    fg="#c5d7bd",
                    font=("Arial", 35, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=30)

generate_password_button = Button(text="Generate Password & Copy to Clipboard",
                                  bg="#fb743e",
                                  height=4,
                                  width=55,
                                  command=password_generator)
generate_password_button.grid(row=2, column=0, columnspan=3, padx=50, pady=50)

password_field = Entry(bg="#383e56",
                       font=("Arial", 15, "bold"))
password_field.grid(row=3, column=0, columnspan=3, rowspan=40, pady=40, padx=40)


window.mainloop()
