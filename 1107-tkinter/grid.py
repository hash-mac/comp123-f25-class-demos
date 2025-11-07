# https://www.studytonight.com/tkinter/python-tkinter-geometry-manager

import tkinter as tk

win = tk.Tk()

# add an orange frame
frame1 = tk.Frame(master=win, width=100, height=100, bg="orange")
frame1.grid(row=0, column=0)

# add blue frame
frame2 = tk.Frame(master=win, width=50, height=50, bg="blue")
frame2.grid(row=0, column=1)

# add green frame
frame3 = tk.Frame(master=win, width=25, height=25, bg="green")
frame3.grid(row=0, column=2)

win.mainloop()
