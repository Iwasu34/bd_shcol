import tkinter as tk
import subprocess
from tkinter import messagebox
import time

def on_closing():
    if messagebox.askokcancel("Выход из приложения","Хотите выйти из программы"):
        win.destroy()

def choice_mysql():
    subprocess.Popen(['.venv/Scripts/python.exe','MySQL_app.py'])
    time.sleep(1)
    win.destroy()


def choice_postgre():
    subprocess.Popen(['.venv/Scripts/python.exe','PostgreSQL_app.py'])
    time.sleep(1)
    win.destroy()
def choice_mongo():
    subprocess.Popen(['.venv/Scripts/python.exe', 'MongoDB_app.py'])
    time.sleep(1)
    win.destroy()

win = tk.Tk()

win.protocol("WM_DELETE_WINDOW", on_closing)
win.geometry("400x150+700-700")
win.title("База данных школьной библиотеки")
win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
choice_bd = tk.Label(win,text="Выберите базу данных для работы", font=('Arial',15,'bold'),borderwidth=20).grid(row=0,column=0,columnspan=3,stick='ns')

btn_mysql=tk.Button(win, text="MySQL",command=choice_mysql).grid(row=1,column=0)
btn_postgre=tk.Button(win, text="PostgreSQL",command=choice_postgre).grid(row=1,column=1)
btn_mongo=tk.Button(win, text="MongoDB",command=choice_mongo).grid(row=1,column=2)

win.mainloop()


# добавление в таблицу имя таблицы через кнопку ё ``
# try:
#     with connection.cursor() as cursor:
#         insert_query = "INSERT INTO `books` (Title, Author, Genre, Year, Pages, Description) VALUES ('Гарри','Джоан Роулинг','Фентази','2019','544','Гарри Поттер снова проводит лето в доме Дурслей. Третьекурсники в Хогвартсе могут посещать деревню магов Хогсмид');"
#         cursor.execute(insert_query)
#         connection.commit()
# finally:
#     connection.close()

