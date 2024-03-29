from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title("Python IDE")

file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def run():
    # command = f"Python {file_path}"
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # output, error = process.communicate()
    # code_output.insert('1.0', output)
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END)
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


menu_bar = Menu(compiler)

file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label='Open', command=open_file)
file_bar.add_command(label='Save', command=save_as)
file_bar.add_command(label='Save As', command=save_as)
file_bar.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label="File", menu=file_bar)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)


# menu_bar.add_cascade(lable='Run', menu=run_bar)
compiler.config(menu=menu_bar)


editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()