import tkinter as tk


langas = tk.Tk()

# foto = tk.PhotoImage(file="calc.jpg")
# langas.iconphoto(False, foto)

langas.config(bg="#14066F")
langas.title("Super Calculator")
langas.geometry("240x260")

langas.minsize(300,400)
langas.maxsize(700,800)
langas.resizable(True, True)

calc = tk.Entry(langas)
calc.grid(row=0, column=0)

tk.Button(text="1").grid(row=1, column=0)
tk.Button(text="2").grid(row=1, column=1)
tk.Button(text="3").grid(row=1, column=2)
tk.Button(text="4").grid(row=2, column=0)
tk.Button(text="5").grid(row=2, column=1)
tk.Button(text="6").grid(row=2, column=2)
tk.Button(text="7").grid(row=3, column=0)
tk.Button(text="8").grid(row=3, column=1)
tk.Button(text="9").grid(row=3, column=2)
tk.Button(text="0").grid(row=4, column=0)

langas.mainloop