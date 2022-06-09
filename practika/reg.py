import sqlite3
import pandas as pd
from tkinter import *
import tkinter as tk
from datetime import timedelta, datetime

db = sqlite3.connect("server.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
login VARCHAR[15],
password VARCHAR[15],
fio VARCHAR[35],
rabota VARCHAR(40),
number VARCHAR(11),
zp VARCHAR(20),
date TEXT
)""")


db.commit()
root = Tk()
root.geometry("600x900+100+100")
root.title('Программа для студентов')

Label(root, text="Login: ").grid(row=0, column=0)
Label(root, text="Password: ").grid(row=1, column=0)

enteruserlogin = tk.Entry(root)
enteruserpassword = tk.Entry(root)
enteruserlogin.grid(row=0, column=1)
enteruserpassword.grid(row=1, column=1)


def timedel():
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    timedelete = timedelta(1095)
    sql.execute("SELECT date FROM students WHERE login = ? AND password = ?", (userlogin, userpassword))
    a = sql.fetchone()
    a = (" ".join(map(str, a)))
    a = datetime.strptime(a, "%Y-%m-%d").date()
    print(a)
    deltime = a + timedelete
    sql.execute(f"""DELETE FROM students WHERE date = {deltime}""")
    db.commit()


def databupdate():
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    sql.execute("SELECT date FROM students WHERE login = ? AND password = ?", (userlogin, userpassword))
    Label(text='Логин ').grid(row=21, column=0)
    Label(text='Пароль ').grid(row=22, column=0)
    Label(text='ФИО ').grid(row=23, column=0)
    Label(text='Место Работы ').grid(row=24, column=0)
    Label(text='Номер ').grid(row=25, column=0)
    Label(text='ЗП').grid(row=26, column=0)
    newlg = Entry(root)
    newlg.grid(row=21, column=1)
    newps = Entry(root)
    newps.grid(row=22, column=1)
    newfio = Entry(root)
    newfio.grid(row=23, column=1)
    newwk = Entry(root)
    newwk.grid(row=24, column=1)
    newnumb = Entry(root)
    newnumb.grid(row=25, column=1)
    newzp = Entry(root)
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
        Label(root, text='Запись успешно изменена!').grid(row=99, column=1)
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{newlogin}'"
                                 f"AND password = '{newpassword}'"):
            Label(root, text=value).grid(row=66, column=1)
        Button(root, text='Хотите изменить?', command=databupdate).grid(row=100, column=1)
        db.commit()
    Button(root, text='Изменить данные', command=update).grid(row=51, column=1)


def getentrytwo():
    userlogin = enteruserlogin.get()
    userpassword = enteruserpassword.get()
    sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
    if sql.fetchone() is None:
        Label(root, text="Такой учетной записи не существует!").grid(row=19, column=1)
    else:
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                 f"AND password = '{userpassword}'"):
            Label(root, text=value).grid(row=13, column=1)
            Button(root, text='Хотите изменить?', command=databupdate).grid(row=14, column=1)
            timedel()


Button(root, text="Войти", command=getentrytwo).grid(row=2, column=0)


def reg():
    Label(root, text="Зарегистрируйтесь!").grid(row=4, column=1)
    Label(root, text="Login: ", justify=RIGHT).grid(row=5, column=0)
    newuserlogin = tk.Entry(root)
    newuserlogin.grid(row=5, column=1)
    Label(root, text="Password: ", justify=RIGHT).grid(row=6, column=0)
    newuserpassword = tk.Entry(root)
    newuserpassword.grid(row=6, column=1)
    Label(root, text="Введите ФИО: ", justify=RIGHT).grid(row=7, column=0)
    newuserfio = tk.Entry(root)
    newuserfio.grid(row=7, column=1)
    Label(root, text="Введите место работы: ", justify=RIGHT).grid(row=8, column=0)
    newuserrabota = tk.Entry(root)
    newuserrabota.grid(row=8, column=1)
    Label(root, text="Введите номер телефона: ", justify=RIGHT).grid(row=9, column=0)
    newusernumber = tk.Entry(root)
    newusernumber.grid(row=9, column=1)
    Label(root, text="Введите вашу заработную плату: ", justify=RIGHT).grid(row=10, column=0)
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
            Label(root, text="Вы успешно зарегистрировались!")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                Label(root, text=value).grid(row=13, column=1)
                Button(root, text='Хотите изменить?', command=databupdate).grid(row=14, column=1)
        else:
            Label(root, text="Такая запись уже существует вы вошли в учетную запись")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                Label(root, text=value).grid(row=13, column=1)
                Button(root, text='Хотите изменить?', command=databupdate).grid(row=14, column=1)
    Button(root, text="Зарегистрироваться!", command=getnewdata).grid(row=11, column=1)


Button(root, text="Пройдите регистрацию", command=reg).grid(row=3, column=0)
root.mainloop()

sql.execute('select * FROM students')
val = sql.fetchall()

print(val)


def exel():
    sql.execute('select * FROM students')
    val = sql.fetchall()
    val = {'Логин': [a_tuple[0] for a_tuple in val], 'Пароль': [a_tuple[1] for a_tuple in val],
           'ФИО': [a_tuple[2] for a_tuple in val], 'Работа': [a_tuple[3] for a_tuple in val],
           'Номер телефона': [a_tuple[4] for a_tuple in val], 'Зарплата': [a_tuple[5] for a_tuple in val]}
    z = pd.DataFrame(val)
    z.to_excel("file.xlsx", sheet_name='Студенты', index_label='id')
    print(val)


exel()
