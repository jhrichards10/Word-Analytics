# Function that recalls the Dracula textbook as a string
def readbook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-"." ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create variable to hold Dracula text
draculaText = readbook()

# Count appearnces of four letter word
appearnces = 0

# Create for loop to count four letter words 
for fourLetter in draculaText():
  # if statement to count length
  if len(fourLetter) == 4:
    # finish the count starte earlier
    appearances += 1 

# Create a count for most often word 
mostOften = 0

# Create for loop to count the most often word 
for mostOften in draculaText():


# Create a dictionary to store the lis
frequency = {}

# Create count for every word that shows up at least 500 times 
count = 0

# Create a for loop to count the words that show up at least 500 times 
for word in draculaText():
  if(word >= 500):
    count += 1 