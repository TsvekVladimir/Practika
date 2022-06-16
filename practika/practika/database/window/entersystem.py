from tkinter_window import root
import tkinter as tk
from database.get_userdata import getentrytwo
from database.get_newuserdata import reg


def entertosystem():
    tk.Label(root, text="Login: ").grid(row=0, column=0)
    tk.Label(root, text="Password: ").grid(row=1, column=0)
    enteruserlogin = tk.Entry(root)
    enteruserpassword = tk.Entry(root)
    enteruserlogin.grid(row=0, column=1)
    enteruserpassword.grid(row=1, column=1)

    tk.Button(root, text="Войти", command=getentrytwo).grid(row=2, column=0)

    tk.Button(root, text="Пройдите регистрацию", command=reg).grid(row=3, column=0)
