from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ast

root = Tk()
root.title('Login')
root.geometry('925x500+250+150')
root.config(bg='#fff')

# Function
def sign_in():
    user_name = username.get()
    pass_word = password.get()

    file = open('sheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if user_name in r.keys() and pass_word == r[user_name]:
        screen = Toplevel(root) 
        screen.title('Window')
        screen.geometry("925x500+250+150")
        screen.config(bg='#fff')

        Label(screen, text= "Hello Everyone!", bg= '#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'Invalid username and password')

#-----------------------------------------------
def sign_up_command():
    window = Toplevel(root)
    window.title('Sign Up')
    window.geometry("925x500+250+150")
    window.config(bg = '#fff')

# Function area
    def sign_up():
        full_name = name.get()
        user_name_ = username.get()
        pass_word_ = password.get()
        confirm_password = confirm_pass.get()

        if pass_word_ == confirm_password:

            try:
                file= open('sheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {user_name_:pass_word_}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('sheet.txt','w')
                w = file.write(str(r))

                messagebox.showinfo('Sign up', 'Successfully Sign up')
                window.destroy()

            except:
                file= open('sheet.txt', 'w')
                pp = str({'username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', 'Both Password not match')

    def log_in():
        window.destroy()

#Image Section 
    img = ImageTk.PhotoImage(Image.open("signup.png"))

    Label(window, image = img, bg = "white").place(x = 50, y = 50)

# Sign up Frame
    frame = Frame(window, width= 350, height= 350, bg = 'white')
    frame.place(x = 500, y = 50)

    heading = Label(frame, text = 'Sign Up', fg = '#57a1f8', bg = 'white', font = ('comicsansms', 25, 'bold'))
    heading.place(x = 120, y = 5)

# Name
    def enter(e):
        name.delete(0, 'end')

    def leave(e):
        name_ = name.get()
        if name_ == '':
            name.insert(0, 'You Name')

    name = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11) )
    name.place( x= 55, y = 65)
    name.insert(0, 'Your Name')
    name.bind('<FocusIn>', enter)
    name.bind('<FocusOut>', leave)

    Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 90)

# Username
    def enter(e):
        username.delete(0, 'end')

    def leave(e):
        user = username.get()
        if user == '':
            username.insert(0, 'username')

    username = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11) )
    username.place( x= 55, y = 115)
    username.insert(0, 'username')
    username.bind('<FocusIn>', enter)
    username.bind('<FocusOut>', leave)

    Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 140)

# Password
    def enter(e):
        password.delete(0, 'end')

    def leave(e):
        pass_ = password.get()
        if pass_ == '':
            password.insert(0, 'password')

    password = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11) )
    password.place( x= 55, y = 165)
    password.insert(0, 'password')
    password.bind('<FocusIn>', enter)
    password.bind('<FocusOut>', leave)

    Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 190)

# Confirm Password
    def enter(e):
        confirm_pass.delete(0, 'end')

    def leave(e):
        cf_pass = confirm_pass.get()
        if cf_pass == '':
            confirm_pass.insert(0, 'Confirm Password')

    confirm_pass = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11))
    confirm_pass.place( x= 55, y = 215)
    confirm_pass.insert(0, 'Confirm Password')
    confirm_pass.bind('<FocusIn>', enter)
    confirm_pass.bind('<FocusOut>', leave)

    Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 240)

# Button Section 
    btn = Button(frame, text = 'Sign Up', cursor='hand2', width = 35, pady = 7, bg = '#57a1f8', fg = 'white', border = 0, command = sign_up)
    btn.place(x= 50, y = 255)

# Bottom Section 
    label = Label(frame, text = "I have an account?", fg = 'black', bg = 'white', font = ('Microsoft YaHei UI Light', 9))
    label.place(x = 100, y = 300)

    log_in_btn = Button(frame, text = 'Log in', cursor='hand2', width  = 6, border = 0, bg = 'white', fg = '#57a1f8', command = log_in)
    log_in_btn.place(x = 210, y = 300)

    window.mainloop()

#---------------------------------------------------


# Image Section
img = ImageTk.PhotoImage(Image.open('Login.png'))

Label(root, image= img , bg='white').place(x= 50, y= 50)

# Login Frame
frame = Frame(root, width=350, height=350, bg= 'white')
frame.place(x=500, y= 70)

heading = Label(frame, text= 'Sign in', fg= '#57a1f8', bg= 'white', font= ('Microsoft YaHei UI Light', 25,'bold'))
heading.place(x=125, y = 5)

# username
def on_enter(e):
    username.delete(0, 'end')

def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')

username = Entry(frame, width= 30,fg = 'black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
username.place(x=55, y=80)
username.insert(0,'Username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=2,bg='black').place(x=50,y=107)

# Password
def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')

password = Entry(frame, width= 30,fg = 'black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
password.place(x=55, y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=2,bg='black').place(x=50,y=177)

# Button Section
btn = Button(frame, width=35, pady=7, text='Sign in', bg= '#57a1f8', fg= 'white',border=0, command= sign_in)
btn.place(x=50, y=204)

# Bottom Section 
label = Label(frame, text="Don't have an account?", fg='black', bg= 'white', font=('Microsoft YaHei UI Light',9))
label.place(x=75, y=260)

sign_up_btn = Button(frame, width=6, text= 'Sign up', border = 0, bg = 'white', cursor='hand2', fg= '#57a1f8', command = sign_up_command)
sign_up_btn.place(x=215, y=260)

root.mainloop()