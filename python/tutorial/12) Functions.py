#this code is not used until called upon
def sayhi():
    print("hello user")


print("top")
#this calls on the function
#it will execute all the code in the function before moving on
sayhi()
print('bottom')

#this function needs a parameter to run
def say_hi(name, age):
    print("hello user "+ name + ' you are '+ str(age))
#this is the parameter for the function say_hi
say_hi('Mike',18)