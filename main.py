# Function that recalls the Dracula textbook as a string
def readbook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create variable to hold Dracula text
draculaText = readbook()

# Create an empty dictionary
draculaWords = {}

# Create a for loop for most often
for word in draculaText.split():
  if(word.lower() in draculaText):
    mostOften = word.count(draculaText)



appearances = 0
# Create for loop to count four letter words 
for fourLetter in draculaText.split(' '):
  # if statement to count length
  if len(fourLetter) == 4:
    # finish the count starte earlier
    appearances += 1 


count = 0
# Create a for loop to count the words that show up at least 500 times 
for number in range(0):
  if(number in draculaText >= 500):
    count += 1
    draculaWord[number] = count 

# Create the print functions
print("=== Results ===")

#Space
print()

# Call the word that appears the most often 
print(f"{word} is the word that appears the most through the text, a total of {mostOften} times ")

# Space
print()

# Call the amount of 4 letter words in dracula
print(f"There are {appearances} words that are four letters long ")

# Space
print()

# Call the dictionary for words in dracula 500 times
for key, value in draculaWords.items():
  print(f"{key} - {value}")

