from tkinter import *
import tkinter as tk
from database.window.tkinter_window import root
from databaseupdate import databupdate
from db import sql, db
from datetime import datetime


def reg():
    tk.Label(root, text="Зарегистрируйтесь!").grid(row=4, column=1)
    tk.Label(root, text="Login: ", justify=RIGHT).grid(row=5, column=0)
    newuserlogin = tk.Entry(root)
    newuserlogin.grid(row=5, column=1)
    tk.Label(root, text="Password: ", justify=RIGHT).grid(row=6, column=0)
    newuserpassword = tk.Entry(root)
    newuserpassword.grid(row=6, column=1)
    tk.Label(root, text="Введите ФИО: ", justify=RIGHT).grid(row=7, column=0)
    newuserfio = tk.Entry(root)
    newuserfio.grid(row=7, column=1)
    tk.Label(root, text="Введите место работы: ", justify=RIGHT).grid(row=8, column=0)
    newuserrabota = tk.Entry(root)
    newuserrabota.grid(row=8, column=1)
    tk.Label(root, text="Введите номер телефона: ", justify=RIGHT).grid(row=9, column=0)
    newusernumber = tk.Entry(root)
    newusernumber.grid(row=9, column=1)
    tk.Label(root, text="Введите вашу заработную плату: ", justify=RIGHT).grid(row=10, column=0)
    newuserzp = tk.Entry(root)
    newuserzp.grid(row=10, column=1)

    def getnewdata():
        userlogin = newuserlogin.get()
        userpassword = newuserpassword.get()
        userfio = newuserfio.get()
        userrabota = newuserrabota.get()
        usernumber = newusernumber.get()
        userzp = newuserzp.get()
        sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
        print(userlogin, userpassword)
        if sql.fetchone() is None:
            deta = datetime.now().date()
            sql.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (userlogin, userpassword, userfio, userrabota, usernumber, userzp, deta))
            db.commit()
            tk.Label(root, text="Вы успешно зарегистрировались!")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                tk.Label(root, text=value).grid(row=13, column=1)
                tk.Button(root, text='Хотите изменить?', command=databupdate).grid(row=14, column=1)
        else:
            tk.Label(root, text="Такая запись уже существует вы вошли в учетную запись")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                tk.Label(root, text=value).grid(row=13, column=1)
                tk.Button(root, text='Хотите изменить?', command=databupdate).grid(row=14, column=1)
    tk.Button(root, text="Зарегистрироваться!", command=getnewdata).grid(row=11, column=1)
