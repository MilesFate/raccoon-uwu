from tkinter import *

# Key down function
def click():
    entered_text=textentry.get() #? this will collect the text from the text entry box
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition="sorry there is no champ with this name"
    output.insert(END,definition)
def close_window():
    window.destroy()
    exit()

# main
window = Tk()
window.title('The Eevee Project')
window.configure(background="black")
window.resizable(0,0)

# photo
photo1 = PhotoImage(file="kappa.gif")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=N)

# create label
Label (window ,text = "Enter the name of the eevee type you would like to search for (lower case only):", bg="black",fg="white",font="none 12 bold") .grid(row=1,column=0,sticky=W)

# create a text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=3,column=0, sticky=W)

# create another label
Label (window, text ="\nDefinition:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

# create a text box
output= Text(window, width=75, height=5, wrap=WORD, background="tan")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# the dictionary
my_compdictionary ={

'eevee':"It has the ability to alter the composition of its body to suit its surrounding environment.", 

'vaporeon':"When Vaporeon’s fins begin to vibrate, it is a sign that rain will come within a few hours.",

'jolteon':"If it is angered or startled, the fur all over its body bristles like sharp needles that pierce foes.",

'flareon':"Once it has stored up enough heat, this Pokémon’s body temperature can reach up to 1,700 degrees Fahrenheit.",

'espeon':"By reading air currents, it can predict things such as the weather or its foe’s next move.",

'umbreon':"When this Pokémon becomes angry, its pores secrete a poisonous sweat, which it sprays at its opponent’s eyes.",

'leafeon':"Galarians favor the distinctive aroma that drifts from this Pokémon’s leaves. There’s a popular perfume made using that scent.",

'glaceon':"Any who become captivated by the beauty of the snowfall that Glaceon creates will be frozen before they know it.",

'sylveon':"By releasing enmity-erasing waves from its ribbonlike feelers, Sylveon stops any conflict.",

'list':'The list of eeveelutions: eevee, vaporean, jolteon, flareon, espeon, umbreon, leafeon, glaceon, sylveon'

}

# exit button
Label (window, text ="Exit:", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
Button(window, text='Exit',width=14, command=close_window) .grid(row=7, column=0, sticky=W)

# main loop
window.mainloop()