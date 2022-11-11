from tkinter import *
import random
import webbrowser as wb

#? these are global and mostly just how the program looks
based = 'https://scp-wiki.wikidot.com/scp-'
root = Tk()
root.geometry("590x250")
root.configure(background="bisque")
root.resizable(0,0)
root.title("SCP Wiki Search")

#? this allows for random
def random_wiki():
    random_article = random.randint(2,6999)
    numgies = str(random_article)
    if random_article < 100 and random_article > 10:
        numgies = '0'+numgies
        wb.open(f'{based}{numgies}')
    elif random_article < 10:
        numgies = '00'+numgies
        wb.open(f'{based}{numgies}')
    else:
        wb.open(f'{based}{numgies}')

#? this allows for the user to select the wiki number
e = Entry(root)

def select_wiki():
    wki_num = e.get()
    wb.open(f'{based}{wki_num}')

#? this explains what the program is
read = Label(root, text="This program will let you search SCP Articles.",bg="bisque",font=14)
read2 = Label(root, text="Search should use 3 or 4 numbers, Ex: 5000, 096.",bg="bisque",font=14)

#? this is for the buttons
Random_button = Button(root,text="Click for Random",bg='Pink',font=14, padx=50, pady= 60, command=random_wiki)
choice = Button(root,text="Enter Number \nBelow and Click",bg='Cyan',font=14,padx=50, pady= 50,command=select_wiki)
quit_button = Button(root,text="Exit",bg='Yellow',font=14,padx=10,pady=10,command=root.quit)

#? this positions everything
read.grid(row=0,column=0)
read2.grid(row=1,column=0)
Random_button.grid(row=2,column=1)
choice.grid(row=2,column=0)
e.grid(row=3,column=0)
quit_button.grid(row=3,column=1)

#? this allows the program to run
root.mainloop()
