# import tkinter as tk 
# from tkinter import messagebox

# # messagebox.showinfo(
# #     "Title",
# #     "Hello"
# # )
# root = tk.Tk()
# labels = tk.Label(
#     root,
#     text=" hello lakshya ",
#     font=("Arial", 20),
#     fg="red",
#     bg="yellow",
#     padx =20,
#     pady= 20
# )
# def hello():
#     print("Hello")
# button =  tk.Button(
#     root , 
#     text = "click me ",
#     font=("Arial",20),
#     padx=40,
#     pady=40,
#     fg="green",
#     bg = "black",
#     command=hello
# )
# # this is  a text box of python/
# entry = tk.Entry(root)
# name = entry.get()
# print(name)

# entry.pack()
# button.pack()
# labels.pack()


# root.title("my first app ")
# root.geometry("600x400")
# root.mainloop()
import tkinter as tk

# ----------------------------
# Functions
# ----------------------------
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ----------------------------
# Window
# ----------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# ----------------------------
# Entry
# ----------------------------
entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=8
)
entry.pack(fill="both", padx=10, pady=10, ipady=15)

# ----------------------------
# Buttons
# ----------------------------
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C', '⌫']
]

for row, button_row in enumerate(buttons):
    for col, text in enumerate(button_row):

        if text == "=":
            btn = tk.Button(
                frame,
                text=text,
                font=("Arial", 18),
                command=calculate
            )

        elif text == "C":
            btn = tk.Button(
                frame,
                text=text,
                font=("Arial", 18),
                command=clear
            )

        elif text == "⌫":
            btn = tk.Button(
                frame,
                text=text,
                font=("Arial", 18),
                command=backspace
            )

        else:
            btn = tk.Button(
                frame,
                text=text,
                font=("Arial", 18),
                command=lambda t=text: click(t)
            )

        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Make buttons resize evenly
for i in range(5):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()