import os
import shutil


source = r"/Users/krishashah/Desktop/Visual Studio Code"
destination = r"/Users/krishashah/Desktop/Python/Class 111/newFolder"

list_of_files = os.listdir(source)
#print(list_of_files)

for i in list_of_files:
    #print(i)

    name,extension = os.path.splitext(i)
    #print(extension)

    if extension == "":
        continue
    if extension in [".png", ".jpg", ".gif", ".pdf"]:
        path1 = source + "/" + i
        path2 = destination + "/" + "newFolder"
        path3 = destination + "/" + "newFolder" + "/" + i
        if os.path.exists(path2):
            print("moving files", i)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving files", i)
            shutil.move(path1, path3)
    