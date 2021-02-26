import tkinter as tk


start = True
last_command = '='
result_number = 0

def click(text):
    print(text)


root = tk.Tk()
root.title('Калькулятор')

btns = [('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '=', '+')]

result = tk.Label(root, text='0', font='tahoma 20', bd=10)
result.grid(row=0, column=0, columnspan=4)

for row in range(4):
    for col in range(4):
        btn = tk.Button(root, text=btns[row][col], font='tahoma 20', command=lambda text=btns[row][col]: click(text))
        btn.grid(row=row + 1, column=col, padx=5, pady=5, ipadx=20, ipady=20, sticky='nsew')

w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws - w) / 2)
y = int((hs - h) / 2)
root.geometry('+{0}+{1}'.format(x, y))

root.mainloop()
