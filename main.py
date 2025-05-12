from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
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
    if website_ent.get() == "" or password_ent.get() == "":
        messagebox.showinfo(title='Error', message='''Please don't leave any fields empty!''')
    else:
        is_ok = messagebox.askokcancel(title='Confirm details', message=f'Website: {website_ent.get()}\n'
                                                                f'Email/Username: {user_mail_ent.get()}\n'
                                                                f'Password: {password_ent.get()}')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{website_ent.get()} | {user_mail_ent.get()} | {password_ent.get()}\n')
            website_ent.delete(0, END)
            password_ent.delete(0, END)

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

website_ent = Entry(width=52)
website_ent.focus()
website_ent.grid(column=1, row=1, columnspan=2, sticky=W)

#ROW 2
user_mail_lbl = Label(text='Email/Username:')
user_mail_lbl.grid(column=0, row=2)

user_mail_ent = Entry(width=52)
user_mail_ent.insert(0, 'francesco@difraia.com')
user_mail_ent.grid(column=1, row=2, columnspan=2, sticky=W)

#ROW 3
password_lbl = Label(text='Password:')
password_lbl.grid(column=0, row=3)

password_ent = Entry(width=33)
password_ent.grid(column=1, row=3, sticky=W)

gen_pass_btn = Button(text='Generate password', command=psw_generator)
gen_pass_btn.grid(column=2, row=3, sticky=W)

#ROW 4
add_btn = Button(text='Add', width=44, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()
