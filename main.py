from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_char = [random.choice(letters) for i in range(8,10)]
    password_symbols = [random.choice(symbols) for i in range(2,4)]
    password_numbers = [random.choice(numbers) for i in range(2,4)]

    password_list = password_char + password_numbers + password_symbols
    random.shuffle(password_list)

    password = [i for i in password_list]
    password = "".join(password)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    test = messagebox.askokcancel("Conformation", f"Are you sure to save Password {password_input.get()} \n"
                                           f"Email/username {email_input.get()} ?")
    if test:
        if len(web_input.get()) == 0 or len(password_input.get()) == 0 or len(email_input.get()) == 0:
            messagebox.showwarning("unfilled", "Please fill the information")
        else:
            with open("data.txt", "a") as file:
                file.write(f"Website :{web_input.get()} || Email/username :{email_input.get()}"
                           f" || Password :{password_input.get()} \n")
                web_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 50, pady = 50)
window.title("Password Generator")

canvas = Canvas(width = 200, height = 200)
photo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image =photo)
canvas.grid( row = 0, column = 1)

web_title = Label(text = "Website :")
web_title.grid(row = 1, column = 0)

web_input = Entry(width = 53)
web_input.grid(row = 1,column = 1, columnspan = 2)
web_input.focus()

email_username_title = Label(text = "Email/Username :")
email_username_title.grid(row = 2, column = 0)
email_input = Entry(width = 53)
email_input.insert(0 ,"nitin@gmail.com")
email_input.grid(row = 2, column = 1, columnspan = 2)

password_title = Label(text = "Password :")
password_title.grid(row = 3, column = 0)

password_input = Entry(width = 35)
password_input.grid(row = 3, column = 1)

button_password = Button(text = "Generate password", command = generate_pass)
button_password.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 45, command = add_info)
add_button.grid(row = 4,column = 1 , columnspan = 2)

window.mainloop()