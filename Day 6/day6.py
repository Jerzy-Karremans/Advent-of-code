inputCharStream = open("day6_input.txt","r").read()

keyLength = 14
for charindex in range(len(inputCharStream)):
    window = {char for char in inputCharStream[charindex:charindex + keyLength]}
    if len(window) == keyLength:
        break
print(charindex + keyLength)