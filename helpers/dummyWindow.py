import tkinter as tk


def keep_windows_open():
    def on_closing():
        """Function to be called when the window is closed."""
        root.destroy()
        root.quit()

    root = tk.Tk()
    root.config(bg='yellow')
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.attributes('-topmost', True)

    label = tk.Label(root,
                     text="To stop the mainloop, close this window",
                     bg="yellow",
                     fg="red",
                     font=("Helvetica", 12, "bold"))
    label.pack(pady=20, padx=20)

    root.mainloop()
