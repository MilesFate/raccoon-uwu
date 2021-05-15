is_male = True
is_tall = True

if is_male:
    #this will run if condition is true
    print("You are a male")
#this adds more conditions to check for
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    #this will run if previos conditions are not met
    print("you are not a male")

#this one checks if either variable is true
if is_male or is_tall:
    #this will run if condition is true
    print("You are a male or tall or both")
else:
    #this will run if previos conditions are not met
    print("you are neither male or tall")

#this one checks if both are true
if is_male and is_tall:
    #this will run if condition is true
    print("You are a male and tall")
else:
    #this will run if previos conditions are not met
    print("you are either not male or tall or both")