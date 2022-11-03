# Function that recalls the Dracula textbook as a string
def readbook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#### Should I use functions or just create loops ?????
# Create variable to hold Dracula text
draculaText = readbook()

# Create an empty dictionary
draculaWords = {}

# Create count for most word
often = 0
# Create a for loop for most often
for word in readbook():

  # make all words lowercase 
  if(word.lower() in draculaText):

    # finish the count
    often += 1

# Create function for word that appears most often 
def mostOften(word, often):

  # Create for loop to find word in dracula text
  for word in readbook():

    # make all words lowercase
    word = word.lower()

# Create for loop to count four letter words 
def fourLetterWord():
  appearances = 0
  for fourLetter in readbook():
    # make all words lowercase
    fourLetter = fourLetter.lower()
  
    # if statement to count length
    if len(fourLetter) == 4:
    
      # finish the count starte earlier
      appearances += 1 
  
  # Create a print to print out how many four letter words there are
  print(f"There are {appearances} words that are four letters long")

# Start the count =
count = 0

# Create a for loop to count the words that show up at least 500 times 
for words in readbook():

  # if word appears more than 500 times
  if(count >= 500):

    # count the number of times
    count += 1

    # count in the dictionary created at the beginning
    draculaWords[words] = count 

# Create the print functions
print("=== Results ===")

#Space
print()

# Call the word that appears the most often 
mostOften(often, word)
print(f"{word} is the word that appears the most through the text, a total of {often} times ")

# Space
print()

# Call the amount of 4 letter words in dracula
fourLetterWord()
#print(f"There are {fourLetterWord} words that are four letters long ")

# Space
print()

# Call the dictionary for words in dracula 500 times
for key, value in draculaWords.items():

  # print the key value of dictionary, #### Not Working #### Do not know why
  print(f"{key} - {value}")

