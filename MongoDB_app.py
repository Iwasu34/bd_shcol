import tkinter as tk
import pymysql
from config import host, user, password, db_name
from tkinter import messagebox

win= tk.Tk()
win.geometry("800x600")
win.title("База данных школьной библиотеки MongoDB")











try:

    connection = pymysql.connect(
        host=host,
        port=8889,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor,
    )
    print("Подключение успешно")
    print("#" * 20)


except Exception as ex:
    print("Ошибка подключения...")
    print(ex)



win.mainloop()