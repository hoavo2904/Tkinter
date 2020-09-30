import tkinter as tk
from tkinter import messagebox

def load():
    age =  entAge.get()
    if age.isdigit():
         messagebox.showinfo('YOUR INFOMATION', message='Name : ' + entName.get() +'\n'+ 'Age : ' + entAge.get() + '\n'+ 'Address : ' + entAddress.get())
    else :
        messagebox.showerror("THÔNG BÁO", "Nhập sai tuổi")    

root = tk.Tk()

#title
root.title("My Program")

#label
tk.Label(root, text = 'What is your name?', font = 'Times 15 bold').grid(row = 0, column = 0, ipadx = 10, ipady = 12)
tk.Label(root, text = 'How old are you?', font = 'Times 15 bold').grid(row = 1, column = 0, ipadx = 10, ipady = 12)
tk.Label(root, text = 'What is your address?', font = 'Times 15 bold').grid(row = 2, column = 0, ipadx = 10, ipady = 12)

#entry
entName = tk.Entry(root, font = 'Times 15 bold')
entName.grid(row = 0, column = 1)
entAge = tk.Entry(root, font = 'Times 15 bold')
entAge.grid(row = 1, column = 1)
entAddress = tk.Entry(root, font = 'Times 15 bold')
entAddress.grid(row = 2, column = 1)

#button
btnEnter = tk.Button(root, text = 'Enter', font = 'Times 15 bold italic', command = load).grid(row = 3, columnspan = 2)
root.geometry('450x550')

tk.mainloop()
