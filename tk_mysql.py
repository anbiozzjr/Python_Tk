from tkinter import *
root = Tk()
import mysql.connector
from mysql.connector import Error
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
# connection = create_connection("localhost", "moron", "P@$$w0rd1", "bunch_of_morons")
connection = create_connection("mysql", "moron", "z,kfrj4c", "bunch_of_morons")

def s():
    moron_id = int(enter_id.get())
    moron_name = str(enter_name.get())
    moron_age = int(enter_age.get())
    with connection.cursor() as cursor:
        #cursor.execute("insert into one values(%s,%s,%s)", (id_moron, name_moron, age_moron))
        print("%i, %s, %i", (moron_id, moron_name, moron_age))
        cursor.execute("INSERT INTO morons VALUES(%s, %s, %s)", (moron_id, moron_name, moron_age))
        connection.commit()


enter_id = Entry()
enter_id.pack()
enter_name = Entry()
enter_name.pack()
enter_age = Entry()
enter_age.pack()
# # кнопка активации функции
start = Button(text="add my data",command=s)
start.pack()
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
