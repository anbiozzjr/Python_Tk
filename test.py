from tkinter import *
root = Tk()


# функция сложения
def s():
    h = str(a.get())
    s = int(b.get())
    if h=="Негра" or h=="Негры" or h=="Негров" or h=="Ниггерсов":
        r = "Тебе в 1600 год"
        label['text'] = str(r)


    if h=="Яблоки" or h=="яблоки" or h=="яблоко" or h=="Яблоки":
        r = s*990
        label['text'] = str(r)


q = Label()
q['text']="Что будешь брать"
q.pack()
a = Entry()
a.pack()

w = Label()
w['text']="Сколько штук"
w.pack()
b = Entry()
b.pack()

# кнопка активации функции
t =Button(text="Взять",command=s)
t.pack()
# вывод результата
label = Label()
label.pack()
root.mainloop()