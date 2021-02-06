import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_en.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_en.get()
    email = email_en.get()
    password = pass_en.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Missing values", message="Please do not leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_en.delete(0, END)
            pass_en.delete(0, END)


def find_password():
    website = website_en.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="oppss!", message="No DataFile Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"website", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="ops", message=f"No details for the {website} exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.iconbitmap('myicon.ico')
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_lb = Label(text="Website:", bg=YELLOW)
website_lb.grid(column=0, row=1)
website_en = Entry(width=21)
website_en.grid(column=1, row=1, padx=(10, 0))
website_en.focus()
search_bt = Button(text="Search", width=12, command=find_password)
search_bt.grid(column=2, row=1, columnspan=2, padx=(0, 21))
email_lb = Label(text="Email/Username: ", bg=YELLOW)
email_lb.grid(column=0, row=2)
email_en = Entry(width=35)
email_en.insert(0, "ahmad@gmail.com")
email_en.grid(column=1, row=2, columnspan=2)
pass_lb = Label(text="Password:", bg=YELLOW)
pass_lb.grid(column=0, row=3)
pass_en = Entry(width=21)
pass_en.grid(column=1, row=3, padx=(10, 0))
gen_bt = Button(text="Generate Pass", command=generate_password)
gen_bt.grid(column=2, row=3, padx=(0, 18))
add_bt = Button(text="Add", width=35, command=save)
add_bt.grid(column=1, row=4, columnspan=2)

window.mainloop()
