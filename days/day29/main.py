from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 13, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def search_website():
    """Search for a website in data.json and return its credentials."""
    website_name = entry_for_website.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)  # Load JSON file

        # Check if website exists in the dictionary
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Not Found", message=f"Website {website_name} not found in database.")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Error: the database not found.")
    except json.JSONDecodeError:
        messagebox.showwarning(title="Warning", message="Error: Database file is corrupted.")


def generate_password():
    """Generate a random password and display it in the password entry field."""
    characters = string.ascii_letters + string.digits + string.punctuation  # A-Z, a-z, 0-9, special chars
    password = ''.join(random.choice(characters) for _ in range(random.randint(12, 21)))  # Generate a 12-character
    # password
    entry_for_password.delete(0, END)  # Clear the field before inserting new password
    entry_for_password.insert(0, password)  # Insert the generated password
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    """Retrieve data and store it in a list."""
    website = entry_for_website.get().title()
    email = entry_for_email.get()
    password = entry_for_password.get()
    new_data = {website:
        {
           "email": email,
           "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:  # Ensure no empty fields
        messagebox.showwarning(title="Warning", message="Please fill in all fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                # Updating the data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(title="Success", message="Your data has been added successfully!")
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                messagebox.showinfo(title="Success", message="Your data has been added successfully!")

        finally:
            entry_for_website.delete(0, END)
            entry_for_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Create a window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Load the image
canvas = Canvas(width=200, height=200,  highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(115, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Creating text fields
website_text = Label(text="Website:", font=FONT)
website_text.grid(row=1, column=0)
email_text = Label(text="Email/Username:", font=FONT)
email_text.grid(row=2, column=0)
password_text = Label(text="Password:", font=FONT)
password_text.grid(row=3, column=0)
# Creating entries
entry_for_website = Entry(width=32)
entry_for_website.grid(row=1, column=1)
entry_for_email = Entry(width=64)
entry_for_email.grid(row=2, column=1, columnspan=2)
entry_for_password = Entry(width=32)
entry_for_password.grid(row=3, column=1)
# Creating buttons
button_generate = Button(text="Generate Password", width=18, font=FONT, command=generate_password)
button_generate.grid(row=3, column=2)
button_search = Button(text="Search", font=FONT, width=18, command=search_website)
button_search.grid(row=1, column=2)
button_add = Button(text="Add", font=FONT, width=38, command=save_data)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
