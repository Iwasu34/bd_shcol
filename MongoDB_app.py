import pymongo.errors
from pymongo import MongoClient
from bson.objectid import ObjectId
import re
from datetime import timedelta, date, datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time


def add_student():
    def add_db():
        value_first_name = First_name.get().title()
        value_last_name = Last_name.get().title()
        value_classes = Classes.get()
        collection = db["Students"]
        try:
            student = {
                "FirstName":value_first_name,
                "LastName": value_last_name,
                "Class": value_classes,
                "Grade":100
            }

            collection.insert_one(student)
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
        value_Title = Title.get().title()
        value_Author = Author.get().title()
        value_Genre = Genre.get().title()
        value_Year = Year.get()
        value_Pages = Pages.get()
        value_Description = Description.get().title()
        collection = db["Books"]
        try:
            book={
                "Title": value_Title,
                "Author": value_Author,
                "Genre": value_Genre,
                "Year":value_Year,
                "Pages": value_Pages,
                "Description": value_Description
            }
            collection.insert_one(book)
            messagebox.showinfo("Добавление в базу данных", "Книга успешно добавлена в базу данных")

        finally:

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
        value_student = entry_students.get().title()
        value_book = entry_books.get().title()
        value_bibliotekr = entry_bibliotekrs.get().title()
        value_datedue = entry_dateDue.get()
        date_obj = datetime.strptime(value_datedue, "%d.%m.%Y")
        value_datedue = date_obj.strftime("%Y-%m-%d")
        value_dateout = entry_dateOut.get()
        date_obj = datetime.strptime(value_dateout, "%d.%m.%Y")
        value_dateout = date_obj.strftime("%Y-%m-%d")
        collection_students = db["Students"]
        collection_books = db["Books"]
        collection_librarians = db["Librarians"]
        collection_loans=db["Loans"]

        try:
            query_student = collection_students.find_one({"LastName": {"$regex":f"^{value_student}"}})
            query_book = collection_books.find_one({"Title": {"$regex":f"^{value_book}"}})
            query_librarian = collection_librarians.find_one({"LastName": {"$regex":f"^{value_bibliotekr}"}})

            loans = {
                "Student_obj":query_student,
                "Book_obj":query_book,
                "Libararian_obj":query_librarian,
                "DateUot":value_datedue,
                "DateDue": value_dateout,
                "Returned":False
            }
            collection_loans.insert_one(loans)
            messagebox.showinfo("Добавление в базу данных", "Выдача успешна добавлена в базу данных")

        finally:

            all_clear_sucses()
    btn_add_issue = tk.Button(new_win, text="Создать выдачу", command=add_db).grid(row=6, column=1, padx=10,pady=10, stick='we')
    btn_all_clear = tk.Button(new_win, text="Очистить", command=all_clear).grid(row=6, column=0, padx=10,pady=10, stick='we')

def delete_issue():
    new_win = tk.Toplevel(win)
    new_win.geometry("1446x310+200+200")
    new_win.title("Удалить должника")
    collection_loans = db["Loans"]



    def delete_record():
        selected = listBox.selection()
        item = listBox.item(selected)
        if item:
            selected_id = item["values"][0]

            try:


                collection_loans.find_one_and_update({"_id":ObjectId(selected_id)},{"$set": {"Returned": True}})

                messagebox.showinfo("Удаление должника", "Отметка о возврате добавлена в базу данных")

                listBox.delete(*listBox.get_children())
                show()
            finally:
                pass
    def show():

        try:
            results = collection_loans.find({'Returned': False})
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values= (result['_id'],result['Student_obj']['FirstName'],result['Student_obj']['LastName'],result['Student_obj']['Class'],result['Book_obj']['Title'],result['DateUot'],result['DateDue']))
    cols=('id','Имя','Фамилия','Класс','Название книги','Дата выдачи','Дата возврата')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()
    listBox.bind('<<TreeviewSelect>>',delete_record)
    btn_delete_issue = tk.Button(new_win, text="удалить должника", command=delete_record).grid(row=2, column=0, padx=10, pady=10)
def view_students():
    collection = db["Students"]
    def show():

        try:
            results = collection.find()
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values= (result["_id"],result["FirstName"],result["LastName"],result["Class"], result["Grade"]))


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
    collection = db["Books"]
    def show():

        try:
            results = collection.find()
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values= (result['_id'],result["Title"],result["Author"],result["Genre"],result["Year"], result["Pages"], result["Description"]))


    new_win = tk.Toplevel(win)
    new_win.geometry("1446x300+200+200")
    new_win.title("Список книг")

    cols=('id','Название','Автор','Жанр','Год','Страниц','Описание')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()
def view_loans():
    collection = db["Loans"]
    def show():

        try:
            results = collection.find()
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values= (result['_id'],result['Student_obj']['FirstName'],result['Student_obj']['LastName'],result['Student_obj']['Class'],result['Book_obj']['Title'],result['DateUot'],result['DateDue']))

    new_win = tk.Toplevel(win)
    new_win.geometry("1446x300+200+200")
    new_win.title("Список выдач книг")

    cols = ('id', 'Имя', 'Фамилия', 'Класс', 'Название книги', 'Дата выдачи', 'Дата возврата')
    listBox= ttk.Treeview(new_win, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    show()
def view_fines():
    collection = db["Loans"]
    def show():

        try:
            results = collection.find({'Returned': False})
        finally:
            pass
        for result in results:
            listBox.insert("", "end", values=(
            result['_id'], result['Student_obj']['FirstName'], result['Student_obj']['LastName'],
            result['Student_obj']['Class'], result['Book_obj']['Title'], result['DateUot'], result['DateDue']))



    new_win = tk.Toplevel(win)
    new_win.geometry("1446x300+200+200")
    new_win.title("Список учеников которые еще не вернули книги")

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


cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["library_db"]
collection = db["Students"]

try:
    client = MongoClient("mongodb://localhost:27017/")
    succses_connect=tk.Label(win, text="Подключение к базе данных успешно",borderwidth=20).grid(row=4,column=0,columnspan=3,stick='we')

except pymongo.errors.ConnectionFailure as ex:
    win.geometry("1140x280")
    error_connect=tk.Label(win, text=f"Ошибка подключения...{ex}",borderwidth=20).grid(row=4,column=0,columnspan=3,stick='we')
    print("Ошибка подключения...")
    print(ex)





win.mainloop()
















