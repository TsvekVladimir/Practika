import sqlite3

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
