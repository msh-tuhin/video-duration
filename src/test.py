import os
import src.definitions

allFiles = []
for dirname, dirs, files in os.walk(src.definitions.directory2):
    print(dirname)
    for file in files:
        allFiles.append(dirname + "\\" + file)

print("***********files******************")
for file in allFiles:
    print(file)
print(len(allFiles))
