from tkinter import *
from tkinter import messagebox
import pickle
def registration():
    label_error = None
    frame = Frame(root, bd=10)
    frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)
    label = Label(frame, text='Sing Up', font='16')
    label.place(relwidth=1, relheight=0.1)
    label_login = Label(frame, text="Login:")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)
    login_entry = Entry(frame)
    login_entry.place(rely=0.2, relx=0.4, relwidth=0.55, relheight=0.1)

    label_password1 = Label(frame, text='Password: ')
    label_password1.place(rely=0.35, relwidth=0.35, relheight=0.2)
    password1_entry = Entry(frame, show ='*')
    password1_entry.place(rely=0.4, relx=0.4, relwidth=0.55)

    label_password2 = Label(frame, text='Confirm \npassword: ')
    label_password2.place(rely=0.55, relwidth=0.35, relheight=0.2)
    password2_entry = Entry(frame, show='*')
    password2_entry.place(rely=0.6, relx=0.4, relwidth=0.55)

    button = Button(frame, text='sing up', command=lambda: singup())
    button.place(relx=0.45, rely=0.8, relwidth=0.3)

    def singup():
        nonlocal label_error
        error = ''

        if label_error:
            label_error.destroy()

        if len(login_entry.get()) == 0:
            error = 'Login Error'
        elif len(password1_entry.get()) < 6:
            error = 'Password Error'
        elif password1_entry.get() != password2_entry.get():
            error = 'Password Error'
        else:
            save()
        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.9)
    def save():
        data = dict()
        data[login_entry.get()] = password1_entry.get()
        f = open('login.txt', 'wb')
        pickle.dump(data, f)
        f.close()
        login()


def login():
    label_error = None
    frame = Frame(root, bd=10)
    frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)
    label = Label(frame, text='Log In', font='16')
    label.place(relwidth=1, relheight=0.1)
    label_login = Label(frame, text="Login:")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)
    login_entry = Entry(frame)
    login_entry.place(rely=0.2, relx=0.4, relwidth=0.55, relheight=0.1)

    label_password = Label(frame, text='Password: ')
    label_password.place(rely=0.35, relwidth=0.35, relheight=0.2)
    password_entry = Entry(frame, show='*')
    password_entry.place(rely=0.4, relx=0.4, relwidth=0.55)

    button = Button(frame, text='log in', command=lambda: login_pass())
    button.place(relx=0.45, rely=0.8, relwidth=0.3)

    def login_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if login_entry.get() in a and password_entry.get() == a[login_entry.get()]:
            messagebox.showinfo('Welcome, to the game!')
        else:
            messagebox.showinfo('Error!')



root = Tk()
root.title("Login and Password")
root.geometry("600x550")

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='img/bg2.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text="Sign up", bg='gold', command=registration)
button_signup.place(relx=0.2, rely=0.1, relwidth=0.3)


button_login = Button(root, text="Log in", bg='gold', command=login)
button_login.place(relx=0.55, rely=0.1, relwidth=0.3)

root.mainloop()