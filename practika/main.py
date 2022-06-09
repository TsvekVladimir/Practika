import sqlite3
import pandas as pd

from datetime import timedelta, datetime

db = sqlite3.connect("server.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
login VARCHAR[15],
password VARCHAR[15],
fio VARCHAR[35],
rabota VARCHAR(40),
number INTEGER,
zp INTEGER,
date TEXT
)""")

db.commit()


def reg():
    global userlogin
    global userpassword
    userlogin = input("login: ")
    userpassword = input("password: ")
    sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
    if sql.fetchone() is None:
        print("Пройдите регистрацию!")
        userlogin = input("login: ")
        userpassword = input("password: ")
        userfio = input("Введите ваши ФИО ")
        userrabota = input("Введите место работы: ")
        usernumber = input(f"Введите номер телефона: 8-")
        userzp = input("Введите вашу заработную плату: ")
        sql.execute(f"SELECT login FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'")
        if sql.fetchone() is None:
            deta = datetime.now().date()
            sql.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (userlogin, userpassword, userfio, userrabota, usernumber, userzp, deta))
            db.commit()
            print("Зарегистрировано!")
        else:
            print("Такая запись уже существует вы вошли в учетную запись")
            for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}'"
                                     f"AND password = '{userpassword}'"):
                print(*value)
    else:
        for value in sql.execute(f"SELECT * FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'"):
            print(*value)
    timedelete = timedelta(1095)
    sql.execute(f"""SELECT date FROM students WHERE login = '{userlogin}' AND password = '{userpassword}'""")
    a = sql.fetchone()
    a = list(a)
    a = " ".join(a)
    a = datetime.strptime(a, "%Y-%m-%d").date()
    deltime = a + timedelete
    sql.execute(f"""DELETE FROM students WHERE date = {deltime}""")
    db.commit()


sql.execute('select * FROM students')
val = sql.fetchall()
reg()
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


def databupdate():
    question = int(input("Что вы хотите изменить в учетной записи? "
                         "\n 1 - Login "
                         "\n 2 - Password "
                         "\n 3 - ФИО "
                         "\n 4 - Место работы "
                         "\n 5 - Номер телефона "
                         "\n 6 - Зарплату "))
    if question == 1:
        newlg = input("")
        sql.execute("""UPDATE students SET login = ? WHERE login = ? AND password = ?""",
                    (newlg, userlogin, userpassword))
        db.commit()
    elif question == 2:
        newps = input("")
        sql.execute("""UPDATE students SET password = ? WHERE login = ? AND password = ?""",
                    (newps, userlogin, userpassword))
        db.commit()
    elif question == 3:
        newfio = input()
        sql.execute("""UPDATE students SET fio = ? WHERE login = ? AND password = ?""",
                    (newfio, userlogin, userpassword))
        db.commit()
    elif question == 4:
        newwk = input("")
        sql.execute("""UPDATE students SET rabota = ? WHERE login = ? AND password = ?""",
                    (newwk, userlogin, userpassword))
        db.commit()
    elif question == 5:
        newnumb = input("")
        sql.execute("""UPDATE students SET number = ? WHERE login = ? AND password = ?""",
                    (newnumb, userlogin, userpassword))
        db.commit()
    elif question == 6:
        newzp = input("")
        sql.execute("""UPDATE students SET zp = ? WHERE login = ? AND password = ?""",
                    (newzp, userlogin, userpassword))
        db.commit()
    else:
        print("Ошибка некорректный ответ!")


databupdate()
