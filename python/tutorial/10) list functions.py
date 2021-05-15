lucky_numbers = [4,8,15,16,23,42]
friends = ['Kevin','Karen','Jim','Jim','Oscar','Toby']

print(friends)
#search list
print(friends.index('Kevin'))
#counts how many of each element
friends.count('Jim')
print(friends)
#sorts the list
friends.sort()
print(friends)
#reverse the order of the list
lucky_numbers.reverse()
print(lucky_numbers)
#combines 2 lists
friends.extend(lucky_numbers)
print(friends)
#copies a list
friends_2 = friends.copy()
print(friends_2)
#adds to the list
friends.append("Creed")
print(friends)
#inserts element
friends.insert(1,'Kelly')
print(friends)
#remove from list
friends.remove('Jim')
print(friends)
#removes the last element of the list
friends.pop()
print(friends)
#clears the list
friends.clear()
print(friends)
