from tkinter import *
root = Tk()
def scanner():
    exit_text = str(entry_text.get())
    text_label['text'] = str(entry_text.get())
    #print(str(entry_text.get()))



hp_text = Label()
hp_text['text'] = "HP_monitor"
hp_text.pack()
entry_text = Entry()
entry_text.pack()


# кнопка активации функции
button_setting = Button(text="Scan",command=scanner)
button_setting.pack()
# вывод результата
text_label= Label()
text_label.pack()
root.mainloop()
