userInput = input("Please enter a string : ")

uniqueString = []

for char in userInput:
    if char not in uniqueString:
        uniqueString.append(char)
stringCount = len(uniqueString)

print("The number of unique characters in the given string is : ", stringCount)