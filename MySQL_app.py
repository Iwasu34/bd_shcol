
from datetime import timedelta, date, datetime
import tkinter as tk
from tkinter import ttk

import pymysql
from config import host, user, password, db_name
from tkinter import messagebox
import time

def add_student():
    def add_db():
        value_first_name = First_name.get()
        value_last_name = Last_name.get()
        value_classes = Classes.get()
        try:
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO `students` (FirstName, LastName, Class,Grade) VALUES ('{value_first_name}','{value_last_name}','{value_classes}','100');"
                cursor.execute(insert_query)
                connection.commit()
                messagebox.showinfo("Добавление в базу данных", "Ученик успешно добавлен в базу данных")
        finally:
            #connection.close()
            all_clear_sucses()
    def all_clear():
        if messagebox.askokcancel("Очиститка", "Вы действительно хотите очистить все данные"):
            First_name.delete(0,'end')
            Last_name.delete(0,'end')
            Classes.delete(0,'end')

    def all_clear_sucses():
        First_name.delete(0, 'end')
        Last_name.delete(0, 'end')
        Classes.delete(0, 'end')


    new_win=tk.Toplevel(win)
    new_win.geometry("340x280+500+200")
    new_win.title("Добавить ученика")

    tk.Label(new_win,text='Имя').grid(row=0,column=0,padx=10,pady=10,stick='w')
    First_name= tk.Entry(new_win)
    First_name.grid(row=0, column=1,padx=10)

    tk.Label(new_win, text='Фамилия').grid(row=1, column=0, padx=10, pady=10, stick='w')
    Last_name = tk.Entry(new_win)
    Last_name.grid(row=1, column=1, padx=10)

    tk.Label(new_win, text='Класс').grid(row=2, column=0, padx=10, pady=10, stick='w')
    Classes = tk.Entry(new_win)
    Classes.grid(row=2, column=1, padx=10)

    btn_add_student = tk.Button(new_win, text="Добавить ученика", command=add_db).grid(row=3, column=1, padx=10,pady=10, stick='we')
    btn_all_clear = tk.Button(new_win, text="Очистить", command=all_clear).grid(row=3, column=0, padx=10,pady=10, stick='we')
def add_book():
    def add_db():
        value_Title = Title.get()
        value_Author = Author.get()
        value_Genre = Genre.get()
        value_Year = Year.get()
        value_Pages = Pages.get()
        value_Description = Description.get()
        try:
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO `books` (Title, Author, Genre, Year, Pages, Description) VALUES ('{value_Title}','{value_Author}','{value_Genre}','{value_Year}','{value_Pages}','{value_Description}');"
                cursor.execute(insert_query)
                connection.commit()
                messagebox.showinfo("Добавление в базу данных", "Книга успешно добавлена в базу данных")
        finally:
            #connection.close()
            all_clear_sucses()
    def all_clear():
        if messagebox.askokcancel("Очиститка", "Вы действительно хотите очистить все данные"):
            Title.delete(0,'end')
            Author.delete(0,'end')
            Genre.delete(0,'end')
            Year.delete(0,'end')
            Pages.delete(0,'end')
            Description.delete(0,'end')

    def all_clear_sucses():
        Title.delete(0, 'end')
        Author.delete(0, 'end')
        Genre.delete(0, 'end')
        Year.delete(0, 'end')
        Pages.delete(0, 'end')
        Description.delete(0, 'end')


    new_win=tk.Toplevel(win)
    new_win.geometry("510x300+500+200")
    new_win.title("Добавить книгу")

    tk.Label(new_win,text='Название').grid(row=0,column=0,padx=10,pady=10,stick='w')
    Title= tk.Entry(new_win)
    Title.grid(row=0, column=1,padx=10)

    tk.Label(new_win, text='Автор').grid(row=1, column=0, padx=10, pady=10, stick='w')
    Author = tk.Entry(new_win)
    Author.grid(row=1, column=1, padx=10)

    tk.Label(new_win, text='Жанр').grid(row=2, column=0, padx=10, pady=10, stick='w')
    Genre = tk.Entry(new_win)
    Genre.grid(row=2, column=1, padx=10)

    tk.Label(new_win, text='Год').grid(row=3, column=0, padx=10, pady=10, stick='w')
    Year = tk.Entry(new_win)
    Year.grid(row=3, column=1, padx=10)

    tk.Label(new_win, text='Количество страниц').grid(row=4, column=0, padx=10, pady=10, stick='w')
    Pages = tk.Entry(new_win)
    Pages.grid(row=4, column=1, padx=10)

    tk.Label(new_win, text='Описание').grid(row=5, column=0, padx=10, pady=10, stick='w')
    Description = tk.Entry(new_win, width=50)
    Description.grid(row=5, column=1, padx=10)


    btn_add_student = tk.Button(new_win, text="Добавить книгу", command=add_db).grid(row=6, column=1, padx=10,pady=10, stick='we')
    btn_all_clear = tk.Button(new_win, text="Очистить", command=all_clear).grid(row=6, column=0, padx=10,pady=10, stick='we')

def issue_book():
    def all_clear():
        if messagebox.askokcancel("Очиститка", "Вы действительно хотите очистить все данные"):
            entry_students.delete(0, 'end')
            entry_books.delete(0, 'end')
            entry_bibliotekrs.delete(0, 'end')

    def all_clear_sucses():
        entry_students.delete(0, 'end')
        entry_books.delete(0, 'end')
        entry_bibliotekrs.delete(0, 'end')



    new_win = tk.Toplevel(win)
    new_win.geometry("810x300+500+200")
    new_win.title("Добавить книгу")

    tk.Label(new_win, text='Выберите ученика').grid(row=0, column=0, padx=10, pady=5, stick='w')
    entry_students = tk.Entry(new_win)
    entry_students.grid(row=1, column=0, padx=10, pady=2, stick='w')


    tk.Label(new_win, text='Выберите книгу').grid(row=0, column=1, padx=10, pady=5, stick='w')
    entry_books = tk.Entry(new_win)
    entry_books.grid(row=1, column=1, padx=10, pady=2, stick='w')


    tk.Label(new_win, text='Выберите библиотекаря').grid(row=0, column=2, padx=10, pady=5, stick='w')
    entry_bibliotekrs = tk.Entry(new_win)
    entry_bibliotekrs.grid(row=1, column=2, padx=10, pady=2, stick='w')

    tk.Label(new_win, text='Дата выдачи').grid(row=0, column=3, padx=10, pady=5, stick='w')
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%d.%m.%Y", named_tuple)
    entry_dateDue = tk.Entry(new_win)
    entry_dateDue.insert(0,time_string)
    entry_dateDue.grid(row=1, column=3, padx=10, pady=2)


    tk.Label(new_win, text='Дата возврата').grid(row=0, column=4, padx=10, pady=5, stick='w')
    end_date = (date.today() + timedelta(days=10)).strftime("%d.%m.%Y")
    entry_dateOut = tk.Entry(new_win)
    entry_dateOut.insert(0, end_date)
    entry_dateOut.grid(row=1, column=4, padx=10, pady=2,stick='w')

    def add_db():
        value_student = entry_students.get()
        value_book = entry_books.get()
        value_bibliotekr = entry_bibliotekrs.get()
        value_datedue = entry_dateDue.get()
        date_obj = datetime.strptime(value_datedue, "%d.%m.%Y")
        value_datedue = date_obj.strftime("%Y-%m-%d")
        value_dateout = entry_dateOut.get()
        date_obj = datetime.strptime(value_dateout, "%d.%m.%Y")
        value_dateout = date_obj.strftime("%Y-%m-%d")
        try:
            with connection.cursor() as cursor:
                query_student = f"SELECT Id FROM `students` WHERE `LastName` LIKE '{value_student}%'"
                query_book = f"SELECT Id FROM `books` WHERE `Title` LIKE '{value_book}%'"
                query_librarian = f"SELECT Id FROM `librarians` WHERE `LastName`  LIKE '{value_bibliotekr}%'"


                cursor.execute(query_student)
                result_student = cursor.fetchone().get("Id")
                cursor.execute(query_book)
                result_book = cursor.fetchone().get("Id")
                cursor.execute(query_librarian)
                result_librarian = cursor.fetchone().get("Id")
                insert_query = f"INSERT INTO `loans` (StudentId, BookId, LibrariansId, DateOut, DateDue) VALUES ('{result_student}','{result_book}','{result_librarian}','{value_datedue}','{value_dateout}');"
                cursor.execute(insert_query)
                connection.commit()
                messagebox.showinfo("Добавление в базу данных", "Выдача успешна добавлена в базу данных")
        finally:
            #connection.close()
            all_clear_sucses()
    btn_add_issue = tk.Button(new_win, text="Создать выдачу", command=add_db).grid(row=6, column=1, padx=10,pady=10, stick='we')
    btn_all_clear = tk.Button(new_win, text="Очистить", command=all_clear).grid(row=6, column=0, padx=10,pady=10, stick='we')

def delete_issue():
    new_win = tk.Toplevel(win)
    new_win.geometry("1446x310+200+200")
    new_win.title("Удалить должника")




    def delete_record():
        selected = listBox.selection()
        item = listBox.item(selected)
        if item:
            selected_id = item["values"][0]
            try:
                with connection.cursor() as cursor:
                    query = (f"Update loans SET Returned = 1 WHERE id = {selected_id}")
                    cursor.execute(query)
                    connection.commit()
                    messagebox.showinfo("Добавление в базу данных", "Выдача успешна добавлена в базу данных")
                    listBox.delete(*listBox.get_children())
                    show()
            finally:
                pass
    def show():

        try:
            with connection.cursor() as cursor:
                query = ("SELECT loans.id, students.FirstName, students.LastName, students.Class, books.Title, loans.DateOut, loans.DateDue FROM loans LEFT JOIN students ON loans.StudentId = students.Id LEFT JOIN books ON loans.BookId = books.Id WHERE loans.`Returned` = 0;")
                cursor.execute(query)
                results = cursor.fetchall()
        finally:
            pass
        for result in results:

            listBox.insert("", "end", values= (result['id'],result['FirstName'],result['LastName'],result['Class'],result['Title'],result['DateOut'],result['DateDue']))
    cols=('id','Имя','Фамилия','Класс','Название книги','Дата выдачи','Дата возврата')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()

    listBox.bind('<<TreeviewSelect>>',delete_record)
    btn_delete_issue = tk.Button(new_win, text="удалить должника", command=delete_record).grid(row=2, column=0, padx=10, pady=10)
def view_students():
    def show():

        try:
            with connection.cursor() as cursor:

                query = ("SELECT * FROM `students`")
                cursor.execute(query)
                results = cursor.fetchall()
        finally:
            pass
        for result in results:

            listBox.insert("", "end", values= (result['Id'],result['FirstName'],result['LastName'],result['Class'], result['Grade']))


    new_win = tk.Toplevel(win)
    new_win.geometry("1046x300+200+200")
    new_win.title("Список учеников")

    cols=('id','Имя','Фамилия','Класс','Рейтинг')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()
def view_books():
    def show():

        try:
            with connection.cursor() as cursor:

                query = ("SELECT * FROM `books`")
                cursor.execute(query)
                results = cursor.fetchall()
        finally:
            pass
        for result in results:

            listBox.insert("", "end", values= (result['id'],result['Title'],result['Author'],result['Genre'], result['Year'], result['Pages'], result['Description']))


    new_win = tk.Toplevel(win)
    new_win.geometry("1446x300+200+200")
    new_win.title("Список учеников")

    cols=('id','Название','Автор','Жанр','Год','Страниц','Описание')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()
def view_loans():
    def show():

        try:
            with connection.cursor() as cursor:

                query = ("SELECT loans.id, students.FirstName, students.LastName, students.Class, books.Title, loans.DateOut, loans.DateDue FROM loans LEFT JOIN students ON loans.StudentId = students.Id LEFT JOIN books ON loans.BookId = books.Id")
                cursor.execute(query)
                results = cursor.fetchall()
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values=(
            result['id'], result['FirstName'], result['LastName'], result['Class'], result['Title'], result['DateOut'],
            result['DateDue']))



    new_win = tk.Toplevel(win)
    new_win.geometry("1446x300+200+200")
    new_win.title("Список учеников")

    cols = ('id', 'Имя', 'Фамилия', 'Класс', 'Название книги', 'Дата выдачи', 'Дата возврата')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()
def view_fines():
    def show():

        try:
            with connection.cursor() as cursor:

                query = ("SELECT loans.id, students.FirstName, students.LastName, students.Class, books.Title, loans.DateOut, loans.DateDue FROM loans LEFT JOIN students ON loans.StudentId = students.Id LEFT JOIN books ON loans.BookId = books.Id WHERE loans.`Returned` = 0;")
                cursor.execute(query)
                results = cursor.fetchall()
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values=(
            result['id'], result['FirstName'], result['LastName'], result['Class'], result['Title'], result['DateOut'],
            result['DateDue']))



    new_win = tk.Toplevel(win)
    new_win.geometry("1446x300+200+200")
    new_win.title("Список учеников")

    cols = ('id', 'Имя', 'Фамилия', 'Класс', 'Название книги', 'Дата выдачи', 'Срок возврата')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()





win= tk.Tk()

win.geometry("340x280")
win.title("База данных школьной библиотеки MySQL")
btn_add_student=tk.Button(win, text="Добавить ученика",command=add_student).grid(row=0,column=0, padx=10, stick='we')
btn_add_books=tk.Button(win, text="Добавить книгу",command=add_book).grid(row=1,column=0, padx=10, stick='we')
btn_issue_book=tk.Button(win, text="Выдать книгу",command=issue_book).grid(row=2,column=0, padx=10, stick='we')
btn_remove_debtor=tk.Button(win, text="Удалить должника",command=delete_issue).grid(row=3,column=0, padx=10, stick='we')


btn_show_all_students=tk.Button(win, text="Показать всех учеников",command=view_students).grid(row=0,column=1, padx=10, stick='we')
btn_show_all_books=tk.Button(win, text="Показать все книги",command=view_books).grid(row=1,column=1, padx=10, stick='we')
btn_show_all_issue=tk.Button(win, text="Показать все выдачи",command=view_loans).grid(row=2,column=1, padx=10, stick='we')
btn_show_all_debtor=tk.Button(win, text="Показать всех должников",command=view_fines).grid(row=3,column=1, padx=10, stick='we')

for c in range(4): win.rowconfigure(index=c, minsize=60)
win.columnconfigure(1, pad=10)

try:

    connection = pymysql.connect(
        host=host,
        port=8889,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor,
    )
    succses_connect=tk.Label(win, text="Подключение к базе данных успешно",borderwidth=20).grid(row=4,column=0,columnspan=3,stick='we')


except Exception as ex:
    win.geometry("1140x280")
    error_connect=tk.Label(win, text=f"Ошибка подключения...{ex}",borderwidth=20).grid(row=4,column=0,columnspan=3,stick='we')
    print("Ошибка подключения...")
    print(ex)



win.mainloop()
















