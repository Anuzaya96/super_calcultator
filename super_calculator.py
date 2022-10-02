
from tkinter import *


def sudetis():
    rezultatas = int(skaicius_1.get()) + int(skaicius_2.get())
    label_atsakymas["text"] = rezultatas

def atimtis():
    rezultatas = int(skaicius_1.get()) - int(skaicius_2.get())
    label_atsakymas["text"] = rezultatas

def daugyba():
    rezultatas = int(skaicius_1.get()) * int(skaicius_2.get())
    label_atsakymas["text"] = rezultatas
    
def dalyba():
    rezultatas = int(skaicius_1.get()) / int(skaicius_2.get())
    label_atsakymas["text"] = rezultatas

def istrint():
    skaicius_1.delete(0, END)
    skaicius_2.delete(0, END)
    label_atsakymas["text"] = "Atsakymas:"

langas = Tk()

langas['bg'] = '#14066F'
langas.title('Calculator')
langas.geometry('350x170')

ikonele = PhotoImage(file="pict/calculator.png")
langas.iconphoto(False, ikonele)

langas.minsize(320,170)
langas.maxsize(400,250)
langas.resizable(True, True)


frame_1 = Frame(langas)
frame_1.grid(row=2, column=1)


mygtukas1 = Button(frame_1, text="+",command=sudetis)
mygtukas2 = Button(frame_1, text="-",command=atimtis)
mygtukas3 = Button(frame_1, text="*",command=daugyba)
mygtukas4 = Button(frame_1, text="/", command=dalyba)


mygtukas1.grid(row=0, column=0, stick="wens",)
mygtukas2.grid(row=0, column=1, stick="wens",)
mygtukas3.grid(row=0, column=2, stick="wens",)
mygtukas4.grid(row=0, column=3, stick="wens",)


label_skaicius1 = Label(langas, text="iveskite pirma skaiciu:", width=25)
label_skaicius1.grid(row=0, column=0, padx=5, pady=5)
skaicius_1 = Entry(langas)
skaicius_1.grid(row=0, column=1, padx=5, pady=5)


label_skaicius2 = Label(langas, text="iveskite antra skaiciu:",width=25)
label_skaicius2.grid(row=1, column=0, padx=5, pady=5)
skaicius_2 = Entry(langas)
skaicius_2.grid(row=1, column=1, padx=5, pady=5)


label_atsakymas= Label(langas, text="Atsakymas:" )
label_atsakymas.grid(row=3, column=1)
rezultatas = Label(langas, text="rezultatas", width=25)
rezultatas.grid(row=3, column=0, padx=5, pady=5)

operacija = Label(langas, text="Pasirinkite matematini veiksma:",width=25)
operacija.grid(row=2, column=0,padx=5, pady=5)

delete = Button(langas, text="Istrnti", command=istrint)
delete.grid(row=4, column=0, padx=5, pady=5)


langas.mainloop()