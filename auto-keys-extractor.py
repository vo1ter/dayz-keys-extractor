import os
import shutil
debug = 0

userChoise = input("Enter your mods location path without \", & or any other symbol (- to use current path): ")
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

for i in range(0, len(homeDirContents)): # find files in the folder
    if(os.path.isdir(homeDir + homeDirContents[i]) == False):
        dirsToDelete.append(homeDirContents[i])

for i in range(0, len(dirsToDelete)): # clear list from files
    homeDirContents.remove(dirsToDelete[i])

for i in range(0, len(homeDirContents)): # find all child dirs contents
    childDirContents.append(os.listdir(homeDir + "\\" + homeDirContents[i]))

for i in range(0, len(childDirContents)):
    for ib in range(0, len(childDirContents[i])):
        if(childDirContents[i][ib].lower() == "keys" or childDirContents[i][ib].lower() == "key"): # search for keys folder
            childDirKeys.append(os.listdir(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib])[0]) # add key file name
            childDirKeysPath.append(str(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib]) + "\\" + os.listdir(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib])[0]) # add key file path

for i in range(0, len(childDirKeysPath)):
    shutil.copyfile(childDirKeysPath[i], homeDir + "keys\\" + childDirKeys[i]) # copy key from mod folder to keys folder

print("\nFiles copied successfully: %d\nFailed to copy: %d\nNOTE! Some mods may use same keys for multiple submods, so it may be marked as \"failed to copy\"\n" % (len(os.listdir(homeDir + "keys")), len(childDirKeys) - len(os.listdir(homeDir + "keys"))))
userChoise = input("Do you want to create list with all mods? (y/n) ")
if(userChoise.lower() == "y" or userChoise.lower() == "yes"):
    modsList = ""
    for i in range(0, len(homeDirContents)):
        modsList += homeDirContents[i] + ";"
    print("\nMods list:\n" + modsList + "\n")

if(debug == 1):
    __debugLog__ = "\n\n\n---------------DEBUG---------------\n"
    print("\n\n\n---------------DEBUG---------------\n")
    for name in dir():
        if not name.startswith('__'):
            __debugLog__ += name + " = " + str(eval(name)) + "\n\n"
    __debugLog__ += "__file__ = " + str(__file__)
    print(__debugLog__)
    print("\n-------------END DEBUG-------------\n\n\n")
    __debugLog__ += "\n-------------END DEBUG-------------\n\n\n"
    if os.path.exists(homeDir + "debug.txt"):
        os.remove(homeDir + "debug.txt")
    debugFile = open(homeDir + "debug.txt", "w")
    debugFile.write(__debugLog__)
    debugFile.close()
os.system("pause")