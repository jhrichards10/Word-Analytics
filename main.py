# Function that recalls the Dracula textbook as a string
def readbook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#### Should I use functions or just create loops ?????
# Create variable to hold Dracula text
draculaText = readbook()
# Split 
draculaText = draculaText.split()

# Create an empty dictionary
draculaWords = {}

# Create a for loop for most often
for word in draculaText:
  if(word in draculaWords):
    draculaWords[word] += 1
  else:
    draculaWords[word] = 1

highRank = 0
word = ""
fourCount = 0
for key, value in draculaWords.items():
  if value > highRank:
    highRank = value
    word = key
  if len(key) == 4:
    fourCount += 1 

  # make all words lowercase 
 # if(word.lower() in draculaText):


# Create function for word that appears most often 
#def mostOften(word, often):

  # Create for loop to find word in dracula text
 # for word in readbook():

    # make all words lowercase
  #  word = word.lower()

# Create for loop to count four letter words 
# def fourLetterWord():
#   appearances = 0
#   for fourLetter in readbook():
#     # make all words lowercase
#     fourLetter = fourLetter.lower()
  
#     # if statement to count length
#     if len(fourLetter) == 4:
    
#       # finish the count starte earlier
#       appearances += 1 
  
#   # Create a print to print out how many four letter words there are
#   print(f"There are {appearances} words that are four letters long")

# # Start the count =
# count = 0

# # Create a for loop to count the words that show up at least 500 times 
# for words in readbook():

#   # if word appears more than 500 times
#   if(count >= 500):

#     # count the number of times
#     count += 1

#     # count in the dictionary created at the beginning
#     draculaWords[words] = count 

# # Create the print functions
# print("=== Results ===")

# #Space
# print()

# # Call the word that appears the most often 
# mostOften(often, word)
print(f"'{word}' is the word that appears the most through the text, a total of {highRank} times ")

# Space
print()

# Call the amount of 4 letter words in dracula
print(f"There are {fourCount} words that are four letters long ")

# Space
print()

# Set up the 500 or more words
print("I noticed that these words show up 500 or more times:")
# # Call the dictionary for words in dracula 500 times
for key, value in draculaWords.items():
  if value >= 500:
    print(f"{key} - {value}")