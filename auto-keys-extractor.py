import os
import shutil

userChoise = input("Enter your server path without \", & or any other symbol (- to use current path): ")
if(userChoise == "-"):
    homeDir = __file__.replace(os.path.basename(__file__), "")
else:
    homeDir = userChoise

homeDirContents = os.listdir(homeDir)
dirsToDelete = []

childDirContents = []
childDirKeys = []
childDirKeysPath = []

try:
    homeDirContents.index("keys")
except ValueError:
    print("There are no \"keys\" folder in the list. Creating one...")
    os.mkdir(homeDir + "keys", mode=777)
else:
    homeDirContents.remove("keys")

for i in range(0, len(homeDirContents)):
    if(len(homeDirContents[i].split(".")) > 1):
        dirsToDelete.append(homeDirContents[i])

for i in range(0, len(dirsToDelete)):
    homeDirContents.remove(dirsToDelete[i])

for i in range(0, len(homeDirContents)):
    childDirContents.append(os.listdir(homeDir + "\\" + homeDirContents[i]))

for i in range(0, len(childDirContents)):
    for ib in range(0, len(childDirContents[i])):
        if(childDirContents[i][ib] == "Keys"):
            childDirKeys.append(os.listdir(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib])[0])
            childDirKeysPath.append(str(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib]) + "\\" + os.listdir(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib])[0])

for i in range(0, len(childDirKeysPath)):
    shutil.copyfile(childDirKeysPath[i], homeDir + "keys\\" + childDirKeys[i])