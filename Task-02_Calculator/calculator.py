from tkinter import *

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry("300x400")
    root.configure(bg="lightgrey")

    expression = ""
    equation = StringVar()

    entry_field = Entry(root, textvariable=equation, font=("Arial", 18), justify='right')
    entry_field.grid(columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
    ]

    for (text, row, col) in buttons:
        if text == "=":
            Button(root, text=text, width=7, height=2, command=equalpress)\
                .grid(row=row, column=col, padx=5, pady=5)
        else:
            Button(root, text=text, width=7, height=2, command=lambda t=text: press(t))\
                .grid(row=row, column=col, padx=5, pady=5)

    Button(root, text='Clear', width=30, height=2, command=clear)\
        .grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    root.mainloop()
