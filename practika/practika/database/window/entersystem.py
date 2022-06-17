import tkinter as tk
from generate_tkinter_window import root
from database.database_update import datab_update
from database.db import sql
from database.get_newuserdata import reg

tk.Label(root, text="Login: ").grid(row=0, column=0)
tk.Label(root, text="Password: ").grid(row=1, column=0)
enteruserlogin = tk.Entry(root)
enteruserpassword = tk.Entry(root)
enteruserlogin.grid(row=0, column=1)
enteruserpassword.grid(row=1, column=1)


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
            tk.Button(root, text='Хотите изменить?', command=datab_update).grid(row=14, column=1)


tk.Button(root, text="Войти", command=getentrytwo).grid(row=2, column=0)
tk.Button(root, text="Пройдите регистрацию", command=reg).grid(row=3, column=0)

