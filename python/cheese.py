def raccoon():
    one = " |~-~-~-~-~-~-~|"
    two = " |-~-~-~-~-~-~-|"

    print(" Cheese Grater")
    print(" _______________")
    print(one)
    print(two)
    print(one)
    print(two)
    print(one)
    print(two)
    print(" ^~^~^~^~^~^~^~^")
    print("for a raccoon boi")
    return

def adeptus():
    print("From the moment I understood the weakness of my flesh,")
    print("it disgusted me.")
    print("craved the strength and certainty of steel.")
    print("I aspired to the purity of the Blessed Machine.")
    print("Your kind cling to your flesh, as if it will not decay and fail you.")
    print("One day the crude biomass that you call a temple will wither,")
    print("and you will beg my kind to save you.")
    print("But I am already saved, for the Machine is immortal...")
    print("...even in death I serve the Omnissiah.")
    return

user_input = input("raccoon or adeptus\n")

if (user_input == "raccoon"):
    raccoon()
elif (user_input == "adeptus"):
    adeptus()
else:
    print("invalid input")