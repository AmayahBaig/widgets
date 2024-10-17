import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.config(background = "white")

def show() :
    print("Hello")
    

button = tk.Button(window, text = "delete", background = "blue" , fg = "purple", command = show )
button.place(x=100,y=200)

entry = tk.Entry(window, width = 20)
entry.place(x=200,y=200)

label = tk.Label(window, text ="hello", background = "pink")
label.place(x=300,y=300)













window.mainloop()