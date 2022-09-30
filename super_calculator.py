import tkinter as tk

langas = tk.Tk()

# rasau funkcija add_digit ir perduodu skaciaus pavydalu, ir kreipiosi i calc ir 
# pridedu insert metoda,
# dabar isivedineja skaiciai
  
def add_digit(digit):
    calc.insert(0,digit)


ikonele = tk.PhotoImage(file="pict/calculator.png")
langas.iconphoto(False, ikonele)


langas.geometry("240x250")
langas.config(bg="#14066F")
langas.title("Super Calculator")

langas.minsize(300,400)
langas.maxsize(500,550)
langas.resizable(True, True)

# culumnspan sujungia kelias koloneles, sio atveju man reikia 3
calc = tk.Entry(langas)
calc.grid(row=0, column=0, columnspan=3)

# stick - mygtukas issiplecia i visas  pasaulio puses stick="wens"
# atributai padx,pady atsako uz tarpus tarp mygtuku bus po 5
# bd darau seselius mygtuku. bd funkcija rasoma prie mygtuku
# command= rasomas prie tk.Button lambda kuri iskviecia identiska funkcija ir + add_diggit
# parasyti funkcija add_digit


tk.Button(text="1", bd=3, command= lambda : add_digit(1)).grid(row=1, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="2", bd=3, command= lambda : add_digit(2)).grid(row=1, column=1, stick="wens", padx=5, pady=5)
tk.Button(text="3", bd=3, command= lambda : add_digit(3)).grid(row=1, column=2, stick="wens", padx=5, pady=5)
tk.Button(text="4", bd=3, command= lambda : add_digit(3)).grid(row=2, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="5", bd=3, command= lambda : add_digit(4)).grid(row=2, column=1, stick="wens", padx=5, pady=5)
tk.Button(text="6", bd=3, command= lambda : add_digit(5)).grid(row=2, column=2, stick="wens", padx=5, pady=5)
tk.Button(text="7", bd=3, command= lambda : add_digit(6)).grid(row=3, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="8", bd=3, command= lambda : add_digit(7)).grid(row=3, column=1, stick="wens", padx=5, pady=5)
tk.Button(text="9", bd=3, command= lambda : add_digit(8)).grid(row=3, column=2, stick="wens", padx=5, pady=5)
tk.Button(text="0", bd=3, command= lambda : add_digit(9)).grid(row=4, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="0", bd=3, command= lambda : add_digit(0)).grid(row=4, column=0, stick="wens", padx=5, pady=5)
 
# duodu minimalu dydi kolonelei ir surasau nr
langas.grid_columnconfigure(0,minsize=60)
langas.grid_columnconfigure(1,minsize=60)
langas.grid_columnconfigure(2,minsize=60)

# eiliu dydi pakeiciu
langas.grid_rowconfigure(1,minsize=60)
langas.grid_rowconfigure(2,minsize=60)
langas.grid_rowconfigure(3,minsize=60)
langas.grid_rowconfigure(4,minsize=60)


langas.mainloop()
