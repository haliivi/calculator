import tkinter as tk

start = True
last_command = '='
result = 0


def click(text: str):
    global start
    global last_command
    global display
    if text.isdigit() or text == '.':
        if start:
            display.configure(text='')
            start = False
        # TODO: rewrite logic
        if text != '.' or display.cget('text').find('.') == -1:
            display.configure(text=display.cget('text') + text)
    else:
        if start:
            last_command = text
        else:
            calculate(float(display.cget('text')))
            last_command = text
            start = True


def calculate(num: float):
    global last_command
    global result
    global display
    if last_command == '+':
        result += num
    elif last_command == '-':
        result -= num
    elif last_command == '*':
        result *= num
    elif last_command == '/':
        try:
            result /= num
        except ZeroDivisionError:
            pass
    else:
        result = num
    display.configure(text=result)


root = tk.Tk()
root.title('Калькулятор')

buttons = [('7', '8', '9', '/'),
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           ('0', '.', '=', '+')]

display = tk.Label(root, text='0', font='tahoma 20', bd=10)
display.grid(row=0, column=0, columnspan=4)

for row in range(4):
    for col in range(4):
        btn = tk.Button(root, text=buttons[row][col], font='tahoma 20',
                        command=lambda text=buttons[row][col]: click(text))
        btn.grid(row=row + 1, column=col, padx=5,
                 pady=5, ipadx=20, ipady=20, sticky='nsew')

w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws - w) / 2)
y = int((hs - h) / 2)
root.geometry('+{0}+{1}'.format(x, y))

root.mainloop()
