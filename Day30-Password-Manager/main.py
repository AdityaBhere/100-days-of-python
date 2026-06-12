from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(choice(letters)) for x in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for y in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for z in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_name = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email,
            "password": password
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as df:
                data = json.load(df)
        except FileNotFoundError:
            with open("data.json", "w") as df:
                json.dump(new_data, df, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as df:
                json.dump(data, df, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No Data File Found.")
    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website.upper(), message=f"Email:{email}\nPassword:{password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="ERROR", message="Password not saved for this website.")

# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

#entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "abc@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

#buttons
generate_password_button = Button(text="Generate Password",width=13, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)


window.mainloop()