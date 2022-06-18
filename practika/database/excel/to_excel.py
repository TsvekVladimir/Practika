import pandas as pd
from database.db import sql


def exel():
    sql.execute('select * FROM students')
    val = sql.fetchall()
    val = {'Логин': [a_tuple[0] for a_tuple in val], 'Пароль': [a_tuple[1] for a_tuple in val],
           'ФИО': [a_tuple[2] for a_tuple in val], 'Работа': [a_tuple[3] for a_tuple in val],
           'Номер телефона': [a_tuple[4] for a_tuple in val], 'Зарплата': [a_tuple[5] for a_tuple in val]}
    z = pd.DataFrame(val)
    z.to_excel("file.xlsx", sheet_name='Студенты', index_label='id')
