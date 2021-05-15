
# types of date in lists
friends_2= ['Kevin',2,False]
friends= ['Kevin','Karen','Jim']
#            0       1       2

#todo replace
friends[1] = 'Mike'

print(friends)
#forward
print(friends[1])
#backward
print(friends[-1])
#starts from x postion and forward
print(friends[1:])
#only between these two points
print(friends[1:3])

print(friends[3],friends_2[3])