from tkinter import *
root = Tk()
def vischitivanie():
    exit_text = int(entry_text.get())
    money_text = int(numb_text.get())
    mont_text = int(amount_text.get())
    text_label['text'] = int(exit_text/12/100*mont_text*money_text+money_text)




proc_text = Label()
proc_text['text'] = "how_much_procent?"
proc_text.pack()
entry_text = Entry()
entry_text.pack()

re_text = Label()
re_text['text'] = "how_much_money?"
re_text.pack()
numb_text = Entry()
numb_text.pack()

month_text = Label()
month_text['text'] = "how_much_month?"
month_text.pack()
amount_text = Entry()
amount_text.pack()

# кнопка активации функции
button_setting = Button(text="Scan",command=vischitivanie)
button_setting.pack()
# вывод результата
text_label= Label()
text_label.pack()
root.mainloop()
