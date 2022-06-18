import tkinter as tk
from database.window.entersystem import enteruserlogin, enteruserpassword
from database.window.generate_tkinter_window import root
from db import sql, db


def datab_update():
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    sql.execute("SELECT date FROM students WHERE login = ? AND password = ?", (userlogin, userpassword))
    tk.Label(text='Логин ').grid(row=21, column=0)
    tk.Label(text='Пароль ').grid(row=22, column=0)
    tk.Label(text='ФИО ').grid(row=23, column=0)
    tk.Label(text='Место Работы ').grid(row=24, column=0)
    tk.Label(text='Номер ').grid(row=25, column=0)
    tk.Label(text='ЗП').grid(row=26, column=0)
    newlg = tk.Entry(root)
    newlg.grid(row=21, column=1)
    newps = tk.Entry(root)
    newps.grid(row=22, column=1)
    newfio = tk.Entry(root)
    newfio.grid(row=23, column=1)
    newwk = tk.Entry(root)
    newwk.grid(row=24, column=1)
    newnumb = tk.Entry(root)
    newnumb.grid(row=25, column=1)
    newzp = tk.Entry(root)
    newzp.grid(row=26, column=1)

    def update():
        newlogin = newlg.get()
        sql.execute("""UPDATE students SET login = ? WHERE login = ? AND password = ?""",
                    (newlogin, userlogin, userpassword))
        newpassword = newps.get()
        sql.execute("""UPDATE students SET password = ? WHERE login = ? AND password = ?""",
                    (newpassword, userlogin, userpassword))
        newfior = newfio.get()
        sql.execute("""UPDATE students SET fio = ? WHERE login = ? AND password = ?""",
                    (newfior, userlogin, userpassword))
        newwork = newwk.get()
        sql.execute("""UPDATE students SET rabota = ? WHERE login = ? AND password = ?""",
                    (newwork, userlogin, userpassword))
        newnumber = newnumb.get()
        sql.execute("""UPDATE students SET number = ? WHERE login = ? AND password = ?""",
                    (newnumber, userlogin, userpassword))
        newzarplata = newzp.get()
        sql.execute("""UPDATE students SET zp = ? WHERE login = ? AND password = ?""",
                    (newzarplata, userlogin, userpassword))
        tk.Label(text='Запись успешно изменена!').grid(row=99, column=1)
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{newlogin}'"
                                 f"AND password = '{newpassword}'"):
            tk.Label(text=value).grid(row=66, column=1)
        db.commit()
    tk.Button(text='Изменить данные', command=update).grid(row=51, column=1)
