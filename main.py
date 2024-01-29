import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='purple', width=300, height=300)
canvas.create_line((0,0), (100,100), (250,300), (0,0), fill='black')
canvas.pack()
win.mainloop()