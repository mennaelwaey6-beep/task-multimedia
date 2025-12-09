from tkinter import *

win = Tk()
win.title("To-Do List")
win.geometry("300x400")
win.configure(bg="#ccf5cc")  

entry = Entry(win, width=25, font=("Arial", 14), bg="#e8ffe8")
entry.pack(pady=10)

tasks = Listbox(
    win,
    width=30,
    height=15,
    font=("Arial", 12),
    bg="#f0fff0", 
    highlightbackground="#90ee90"
)
tasks.pack(pady=10)

def add_task():
    task = entry.get()
    if task != "":
        tasks.insert(END, task)
        entry.delete(0, END)

def delete_task():
    try:
        index = tasks.curselection()[0]
        tasks.delete(index)
    except:
        pass

add_btn = Button(win, text="Add", width=10, bg="#4CAF50", fg="white", command=add_task)
add_btn.pack(pady=5)

del_btn = Button(win, text="Delete", width=10, bg="#388E3C", fg="white", command=delete_task)
del_btn.pack(pady=5)

win.mainloop()