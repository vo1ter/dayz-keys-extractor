import os
import shutil
debug = 0

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
failedToFindKeys = []

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
        if(childDirContents[i][ib].lower() == "keys" or childDirContents[i][ib].lower() == "key"):
            childDirKeys.append(os.listdir(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib])[0])
            childDirKeysPath.append(str(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib]) + "\\" + os.listdir(homeDir + homeDirContents[i] + "\\" + childDirContents[i][ib])[0])

for i in range(0, len(childDirKeysPath)):
    shutil.copyfile(childDirKeysPath[i], homeDir + "keys\\" + childDirKeys[i])

if(debug == 1):
    __debugLog__ = ""
    print("\n\n\n---------------DEBUG---------------\n")
    for name in dir():
        if not name.startswith('__'):
            __debugLog__ += name + " = " + str(eval(name)) + "\n\n"
    print(__debugLog__)
    print("\n-------------END DEBUG-------------\n\n\n")
    if os.path.exists(homeDir + "debug.txt"):
        os.remove(homeDir + "debug.txt")
    debugFile = open(homeDir + "debug.txt", "w")
    debugFile.write(__debugLog__)
    debugFile.close()
    debugFile = open(homeDir + "debug.txt", "r")
    print(debugFile.read())

print("Files copied successfully: %d\nFailed to copy: %d\n\n\nNOTE! Some mods may use same keys for multiple submods, so it may be marked as \"failed to copy\"" % (len(os.listdir(homeDir + "keys")), len(childDirKeys) - len(os.listdir(homeDir + "keys"))))