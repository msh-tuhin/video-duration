import os, src.definitions

totalduration = 0
allFiles = []
for dirname, dirs, files in os.walk(src.definitions.directory3):
    for file in files:
        allFiles.append(dirname + "\\" + file)

f = open("C:\\Users\\Tuhin\\Desktop\\out.txt", "w")
for file in allFiles:
    if file.split('.').pop() in ['f4v', 'mp4', 'mov', 'avi', 'mkv', 'wmv']:
        duration = src.definitions.findduration(src.definitions.procname, file)
        totalduration += duration
        print(file, " :    ", src.definitions.secondtohms(duration))
        f.write(file + " :    " + src.definitions.secondtohms(duration) + "\n")


print(totalduration)
hms = src.definitions.secondtohms(totalduration)
print("Total Duration :   {}".format(hms))
f.write("Total Duration :   {}".format(hms))
f.close()
