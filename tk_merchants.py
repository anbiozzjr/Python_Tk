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
#connection = create_connection("mysql", "moron", "z,kfrj4c", "bunch_of_morons")
connection = create_connection("mysql", "merchant", "z,kfrj4c", "discord")

def calc_zp():
    merchant_income = int(enter_income.get())
    with connection.cursor() as cursor:
        cursor.execute("select * from merchants")
        merchant_items = cursor.fetchall()
        # connection.commit()
        name = 1
        taxe = 2
        rent = 3
        box_zp.delete(0, END)
        box_zp.select_clear
        for item in merchant_items:
            # print(item)
            # label['text'] = int(merchant_income - item[taxe] - item[rent])
            box_zp.insert(END, merchant_income - item[taxe] - item[rent])

            print(merchant_income-item[taxe]-item[rent])





enter_income = Entry()
enter_income.pack()
# # кнопка активации функции
start = Button(text="add my data",command=calc_zp)
start.pack()

box_zp = Listbox()
box_zp.pack()

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