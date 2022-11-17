# Function that recalls the Dracula textbook as a string
def readbook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create variable to hold Dracula text
draculaText = readbook()
# Split 
draculaText = draculaText.split()

# Create an empty dictionary
draculaWords = {}

# Create a for loop for most often
for word in draculaText:

  # create if statement to give 'word' meaning
  if(word in draculaWords):

    # add a word to count if in dictionary
    draculaWords[word] += 1
  
  # else the value is one  
  else:
    draculaWords[word] = 1

# open a count for the word that appears the most 
highRank = 0

# open a string to store the words being counted
word = ""

# open a count for each word that is at least four letters long
fourCount = 0

# create a for loop for the dictionary
for key, value in draculaWords.items():
  
  # create if statement to count the word that appears the most
  if value > highRank:
    
    # make highrank count eqaul the value in the dictionary
    highRank = value
    
    # make the word equal the key in the dictionary
    word = key
  
  # Create if statement with length to count four letter words  
  if len(key) == 4:

    # add 1 each time it finds a four letter word
    fourCount += 1 

  
# # Call the word that appears the most often 
print(f"'{word}' is the word that appears the most through the text, a total of {highRank} times ")

# Space
print()

# Call the amount of 4 letter words in dracula
print(f"There are {fourCount} words that are four letters long ")

# Space
print()

# Set up the 500 or more words
print("I noticed that these words show up 500 or more times:")

# Call the dictionary for words in dracula 500 or more times
for key, value in draculaWords.items():

  # create a greater than or equal to 500 count
  if value >= 500:

    # print the count
    print(f"{key} - {value}")