import nltk
import requests
import json
# from bs4 import BeautifulSoup
nltk.download('words')
from nltk.corpus import words
dictionary = set(words.words())
words = []
def brute(string, length, charset):
	global words
	if len(string) == length:
		return
	for char in charset:
		temp = string + char
		words.append(temp)
		brute(temp, length, charset)
	return(words)


def formatted(wordDict, middleLetter, dictionary):
	final = {}
	listOfSizes = list(wordDict.keys())
	listOfSizes.sort()
	largestWord = listOfSizes[-1]
	for x in range(0, largestWord+1):
		if(x >= 4):
			final[str(x)] = []
			if(x in wordDict.keys()):
				for word in wordDict[x]:
					if(word in dictionary and middleLetter in word):
						if(word not in final[str(x)]):
							final[str(x)].append(word)
	return final

def solver(middleLetter, otherLetters):
	global brute, words, formatted, dictionary
	print("MADE IT")
	middleLetter = str(middleLetter).lower()
	otherLetters = str(otherLetters).lower()
	otherLettersArray = list(otherLetters)
	allLetters = otherLettersArray
	allLetters.append(middleLetter)
	words = []
	wordsSorted = {}

	# GET ALL POSSIBLE WORDS
	brute("", len(allLetters)+1, "".join(allLetters))

	# Create arrays for dicts
	for word in words:
		wordsSorted[len(word)] = []

	# Append all the words
	for word in words:
		wordsSorted[len(word)].append(word)
	finalResult = formatted(wordsSorted, middleLetter, dictionary)
	return finalResult

def solverRaw(middleLetter, otherLetters):
	global solver
	data = solver(middleLetter,otherLetters)
	data = list(data.values())
	merged_list = []
	for l in data:
		merged_list += l
	return merged_list

# for x in range(0, largestWord+1):
# 	if(x >= 4):
# 		print("-"*10 + str(x) + " letter words" + "-"*10)
# 		if(x in wordsSorted.keys()):
# 			i = 1
# 			for word in wordsSorted[x]:
# 				if(word in dictionary and middleLetter in word):
# 					print(str(i) + ": " + word)
# 					i += 1

def webSolver():
	data = {}
	page = requests.get("https://www.nytimes.com/puzzles/spelling-bee")
	soup = BeautifulSoup(page.text, 'html.parser')
	answers = str(soup.find_all('script')[0]).replace('<script type="text/javascript">window.gameData = ', "").replace("</script>","")
	parsed = json.loads(answers)
	# NORMAL Answers
	answersList = list(parsed["today"]["answers"])
	answersList.sort(key=len)
	for answer in answersList:
		data[str(len(answer))] = []

	for answer in answersList:
		data[str(len(answer))].append(answer)
	return data