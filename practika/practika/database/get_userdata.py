import tkinter as tk
from database.window.tkinter_window import enteruserlogin, enteruserpassword, root
from databaseupdate import databupdate
from db import sql


def getentrytwo():
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
    if sql.fetchone() is None:
        tk.Label(root, text="Такой учетной записи не существует!").grid(row=19, column=1)
    else:
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                 f"AND password = '{userpassword}'"):
            tk.Label(root, text=value).grid(row=13, column=1)
            tk.Button(root, text='Хотите изменить?', command=databupdate).grid(row=14, column=1)
