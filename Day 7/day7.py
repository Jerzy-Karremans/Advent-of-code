lines = open("./Day 7/day7_input.txt","r").read().split("\n")\


# transform input into a file tree with [("name",size or [contents])]
def transformCommandsToFileTree(commandArr):
    fileTree = {"/" : {}}
    pointer = []
    for command in commandArr:
        if command.startswith("$ cd .."):
            pointer.pop()
        elif command.startswith("$ cd"):
            pointer.append(command[5:])
        elif command.startswith("$ ls"):
            fileWorkingOn = fileTree
            for pos in pointer:
                fileWorkingOn = fileWorkingOn[pos]
        else:
            [extention, name] = command.split(" ")
            if extention == "dir":
                fileWorkingOn[name] = {}
            else:
                fileWorkingOn[name] = extention
    return fileTree

# recursivly calculate all dir sizes
# find a way to return a list of all dirs/ files and thier sizes
def recursivelyPrintFiles(file,key,count):
    count += 1
    outputFiles = []
    if(type(file) == dict):
        if(len(file.keys()) > 0):
            if key != "":
                print("   " * count + "-",key,"(dir)")
            for key in file.keys():
                outputFiles.append(recursivelyPrintFiles(file[key],key,count))
    else:
        print("   " * count + "-", key,f"(file, size=({file})")
        return file
    return outputFiles
    
    

fileTree = transformCommandsToFileTree(lines)

print(recursivelyPrintFiles(fileTree,"",-2))
# print(fileTree)

# find dirs smaller or equal to 100_000
# eliminate child dirs
# calculate sum size these dirs