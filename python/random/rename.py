import os

path = os.chdir(" ")

i = 0

for file in os.listdir(path):
    #new_file_name = "{}.png".format(i)
    #new_file_name = "{}.jpg".format(i)
    new_file_name = "{}.gif".format(i)
    #new_file_name = "{}.mp4".format(i)
    os.rename(file, new_file_name)
    
    i = i + 1