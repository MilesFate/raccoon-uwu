from tkinter import *

window = Tk()

window.title('The Eevee Project')
window.configure(background="black")
window.resizable(0,0)

photo1 = PhotoImage(file="onion.png")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=N)

window.mainloop()
