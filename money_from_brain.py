from tkinter import *
import mysql.connector
from mysql.connector import Error

root = Tk()

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"WTF")
        print(f"The error '{e}' occurred")

    return connection
#connection = create_connection("mysql", "moron", "z,kfrj4c", "bunch_of_morons")
connection = create_connection("mysql", "student", "P@$$w0rd1", "ScoreToMoney")

def button_add_year():
    id_year = int(enter_id.get())
    year = int(enter_year.get())
    with connection.cursor() as cursor_add_year:
        #print("%i, %i", (id_year, year))
        cursor_add_year.execute("INSERT INTO years VALUES(%s, %s)", (id_year, year))
        connection.commit()
    refresh_list = listbox_years_refresh().get()
    # print(type(refresh_list))
    # print(refresh_list)
    l_test = list()
    for x in refresh_list:
        l_test.append(x)
    listbox_years_var.set(l_test)

def listbox_years_refresh():
    with connection.cursor() as cursor_listbox:
        list_year = list()
        cursor_listbox.execute("select id_year, year from years")
        result_years = cursor_listbox.fetchall()
        # print(type(res))
        # print(res)
        for (year_id, year_name) in result_years:
            list_year.append(year_name)
        list_year_var = StringVar(value=list_year)
    return list_year_var

listbox_years_var = listbox_years_refresh()
print(listbox_years_var)
listbox_years = Listbox(listvariable=listbox_years_var)
listbox_years.pack()


enter_id = Entry()
enter_id.pack()
enter_year = Entry()
enter_year.pack()

# # кнопка активации функции
start = Button(text="add my data", command=button_add_year)
start.pack()

# refresh = Button(text="refresh", command=button_refresh)
# refresh.pack()

# with connection.cursor() as cursor_2:
#     list_year = list()
#     cursor_2.execute("select id_year, year from years")
#     res = cursor_2.fetchall()
#     print(type(res))
#     print(res)
#     for (id_year, year_name) in res:
#         list_year.append(year_name)
#     list_year_var = StringVar(value=list_year)
#     list_of_year = Listbox(listvariable=list_year_var)
#     list_of_year.pack()


#f = Button(text="show me data",command=show)
# f.pack()
# dell = Button(text="delete",command=delete)
# dell.pack()
# upd = Button(text="update",command=upd)
# upd.pack()
# вывод результата
label = Label()
label.pack()
lab = Label()
lab.pack()
root.mainloop()