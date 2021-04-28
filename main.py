#imports
import base64,os,random,sqlite3,string,bcrypt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#database checker
def checkForDB():
    global c,conn
    #connect to db
    if os.path.isfile('data.db'):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
    #create db
    else:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE passwords (passwordTitle text,password text )""")
    conn.commit()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        conn.close()
        sys.exit()

def getSalt():
    global salt
    if os.path.isfile('salt.txt'):
        with open('salt.txt','rb') as saltFile:
            salt = saltFile
    else:
        with open('salt.txt','wb') as saltFile:
            salt = bcrypt.gensalt()
            saltFile.write(salt)



checkForDB()

#main loop
while True:
    if os.path.isfile('users.txt'):
        #Creating a window object
        login = Tk()

        login.protocol("WM_DELETE_WINDOW", on_closing)

        #Window Size
        login.geometry("300x150")

        #Set Height & Width
        Tk_Width = 300
        Tk_Height = 150

        #Postion Variables
        x_Left = int(login.winfo_screenwidth() / 2 - Tk_Width / 2)
        y_Top = int(login.winfo_screenheight() / 2 - Tk_Height / 2)

        #Window Postion
        login.geometry("+{}+{}".format(x_Left,y_Top))

        #Window Title
        login.title("Login")

        #Create lable
        label = Label(login, text="Login").pack()

        #Create a frame
        loginFrame = Frame()

        #Create string variables for text entry extraction
        usernameEntryValue = StringVar()
        passwordEntryValue = StringVar()

        #Create Lables
        usernameLabel = Label(loginFrame,text="Username:").grid(row=0,column=0)
        passwordLabel = Label(loginFrame,text="Password:").grid(row=1,column=0)

        #Creating Entries
        usernameEntry = tk.Entry(loginFrame,textvariable=usernameEntryValue).grid(row=0,column=1)
        passwordEntry = tk.Entry(loginFrame,textvariable=passwordEntryValue,show='*').grid(row=1,column=1)

        #Create Submit Button
        loginSubmitButton = Button(loginFrame,text="Submit").grid(row=4,column=0)

        #Pack the frame
        loginFrame.pack()

        #Create a delete button
        deleteUserButton = Button(login,text="Delete").pack()

        #Run window
        login.mainloop()

    else:
        register = Tk()

        register.protocol("WM_DELETE_WINDOW", on_closing)

        # Window Size
        register.geometry("300x150")

        # Set Height & Width
        Tk_Width = 300
        Tk_Height = 150

        # Postion Variables
        x_Left = int(register.winfo_screenwidth() / 2 - Tk_Width / 2)
        y_Top = int(register.winfo_screenheight() / 2 - Tk_Height / 2)

        # Window Postion
        register.geometry("+{}+{}".format(x_Left, y_Top))

        # Window Title
        register.title("Register")

        #Create label
        label = Label(register,text="Create a user!")

        #Create Frame
        registerFrame = Frame()

        #Create entry string variables
        usernameEntryValue = StringVar()
        passwordEntryValue = StringVar()

        #Create labels
        usernameLabel = Label(registerFrame,text="Username:").grid(row=0,column=0)
        passwordLabel = Label(registerFrame,text="Password:").grid(row=1,column=0)

        #Create entries
        usernameEntry = tk.Entry(registerFrame,textvariable=usernameEntryValue).grid(row=0,column=1)
        passwordEntry = tk.Entry(registerFrame,textvariable=passwordEntryValue).grid(row=1,column=1)

        #Create Button
        registerSubmitButton = Button(registerFrame,text="Submit").grid(row=2,column=1)

        #Pack frame
        registerFrame.pack()

        #Create Window
        register.mainloop()