from re import search
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import json as js

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def psw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) + choice(symbols) + choice(numbers) for _ in range(5)]
    shuffle(password_list)
    password = "".join(password_list)
    password_ent.delete(0, END)
    window.clipboard_clear()
    password_ent.insert(0, password)
    window.clipboard_append(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_ent.get(): {
            'email': user_mail_ent.get(),
            'password': password_ent.get()
        }
    }

    if website_ent.get() == "" or password_ent.get() == "":
        messagebox.showinfo(title='Error', message='''Cannot leave any fields empty!''')
    else:
        try:
            with open('data.json', 'r') as data_file:
                #Read old data
                data = js.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                #Save new data
                js.dump(new_data, data_file, indent=4)
        else:
            # Update old data w/new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                #Save updated data
                js.dump(data, data_file, indent=4)
        finally:
            website_ent.delete(0, END)
            password_ent.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_details():
    find_key = website_ent.get()
    if find_key == '':
        messagebox.showinfo(title='Error', message='''Cannot leave website field empty!''')
    else:
        try:
            with open('data.json') as data_file:
                data = js.load(data_file)
                email = data[find_key]['email']
                psw = data[find_key]['password']
        except FileNotFoundError:
            messagebox.showinfo(title='Error', message='''No data file found''')
        except KeyError:
            messagebox.showinfo(title='Error', message=f'''No details for {find_key} exists''')
        else:
            window.clipboard_clear()
            window.clipboard_append(psw)
            messagebox.showinfo(title=website_ent.get(),
                                message=f'Email/Username: {email}\nPassword: {psw}\n\nPassword copied to clipboard!')
        finally:
            website_ent.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
#Init window
window = Tk()
window.title('PPM | Pendolino Password Manager')
window.config(padx=50, pady=50)

#ROW 0 (Canvas)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

#ROW 1
website_lbl = Label(text='Website:')
website_lbl.grid(column=0, row=1)

search_btn = Button(text='Search', width=15, command= find_details)
search_btn.grid(column=2, row=1, sticky= E)

website_ent = Entry(width=32)
website_ent.focus()
website_ent.grid(column=1, row=1, columnspan=2, sticky=W)

#ROW 2
user_mail_lbl = Label(text='Email/Username:')
user_mail_lbl.grid(column=0, row=2)

user_mail_ent = Entry(width=52)
user_mail_ent.insert(0, 'example@email.eu')
user_mail_ent.grid(column=1, row=2, columnspan=2, sticky=W)

#ROW 3
password_lbl = Label(text='Password:')
password_lbl.grid(column=0, row=3)

password_ent = Entry(width=32)
password_ent.grid(column=1, row=3, sticky=W)

gen_pass_btn = Button(text='Generate password', width=15, command=psw_generator)
gen_pass_btn.grid(column=2, row=3, sticky=E)

#ROW 4
add_btn = Button(text='Add', width=44, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()
