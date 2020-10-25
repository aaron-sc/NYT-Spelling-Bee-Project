import nltk

nltk.download('words')
from nltk.corpus import words
dictionary = set(words.words())
middleLetter = str(input("Middle Letter: ").lower())
otherLetters = str(input("Other letters (Seperated by commas (6 letters)): ").lower())
otherLettersArray = otherLetters.split(",")
allLetters = otherLettersArray
allLetters.append(middleLetter)
print("Solving with letters: " + "".join(allLetters))
words = []
wordsSorted = {}
def brute(string, length, charset):
	global words
	if len(string) == length:
		return
	for char in charset:
		temp = string + char
		words.append(temp)
		brute(temp, length, charset)
	return(words)
# GET ALL POSSIBLE WORDS
print("Getting All Possible Results")
brute("", len(allLetters)+1, "".join(allLetters))
print("Finished... Now sorting")

# Create arrays for dicts
for word in words:
	wordsSorted[len(word)] = []

# Append all the words
for word in words:
	wordsSorted[len(word)].append(word)

listOfSizes = list(wordsSorted.keys())
listOfSizes.sort()
largestWord = listOfSizes[-1]
print("Sorted!")
print("Largest word is " + str(largestWord) + " letters long!")



for x in range(0, largestWord+1):
	if(x >= 4):
		print("-"*10 + str(x) + " letter words" + "-"*10)
		if(x in wordsSorted.keys()):
			i = 1
			for word in wordsSorted[x]:
				if(word in dictionary and middleLetter in word):
					print(str(i) + ": " + word)
					i += 1