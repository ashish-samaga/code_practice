userInput = input("Please enter a string : ")
rev_str = ""

for char in userInput:
    rev_str = char + rev_str

print("Given String is : ", userInput)
print("Revresed String is : ", rev_str)