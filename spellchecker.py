from dictionary import Dictionary
import string
import re


class SpellChecker:
    def __init__(self, dictionary: Dictionary, passage):
        """
        Object declaration for a spell checker
        :param dictionary: the dictionary that the user will be checking their text against (for the purposes of our
        class, English is the only provided dictionary
        :param passage: the text that the user wants to check for spelling errors
        """
        self.dictionary = dictionary
        punctSep = re.compile(r"[\w']+|\s+|[^\w'\s]+")  # Separates actual words from punctuation in the list version of the passage, which makes implementing word suggestions possible without removing punctuation
        self.text = punctSep.findall(passage)   # List of words to operate on for spell checking, separated from punctuation
        self.rawText = passage     # Actual passage entered by user

    def incorrectWords(self):
        """
        Compares the user's entered text against the dictionary that was chosen, and returns a list of incorrectly
        spelled words
        :return: a list of words not found in the provided dictionary
        """
        incorrect = []
        for word in self.text:
            if word in string.punctuation or word == ' ':
                continue
            if word not in self.dictionary.dict:
                finalChecker = chr(ord(word[0]) + 32) + word[1:]  # Accounts for uppercase characters (not present in the dictionaries I make use of)
                if finalChecker not in self.dictionary.dict:  # Adds the word to the incorrect list if it cannot be found in the dictionary
                    incorrect.append(word.lower())
        return incorrect

    def getIncorrectWords(self):
        """
        Returns a list of incorrectly spelled words (for user inspection, rather than code operation)
        :return: a string including a list of words that were not found in the user's chosen dictionary
        """
        return f'Incorrectly spelled words: {self.incorrectWords()}'

    def suggestWords(self):
        """
        Takes each word that the user misspelled, and swaps each pair of adjacent characters, and suggesting that word
        to the user if it is found in their dictionary
        :return: When the function is finished operating on incorrectly spelled words
        """
        suggested = []
        incorrectWords = self.incorrectWords()  # Getting a list of incorrectly spelled words
        if len(incorrectWords) == 0:
            return 'No incorrectly spelled words detected.'
        else:
            print('Incorrectly spelled words:', incorrectWords)
        for word in incorrectWords:
            for i in range(len(word) - 1):
                for j in range(1, len(word)):   # Chose two loops because it also finds words misspelled by more than one
                    # transposition space (i.e. both dfeault and dtfaule have default suggested when used)
                    listed = list(word)     # Creates a list of characters for each word, and swapping characters based on indices i and j
                    listed[i], listed[j] = listed[j], listed[i]
                    newWord = ''.join(listed)   # Rejoin the list of characters into a word
                    if newWord in self.dictionary.dict:
                        if newWord not in suggested:  # Accounting for repeated incorrect entries
                            print(f'Unknown word: {word}. Did you mean "{newWord}"? Enter "Yes" if so.')
                            statement = input()
                            if statement == 'Yes':
                                if word not in self.text:
                                    if word.capitalize() in self.text:
                                        self.text[self.text.index(word.capitalize())] = newWord.capitalize()
                                    else:
                                        print(f'"{word}" was not found in its expected location. You must have corrected it already.')
                                else:
                                    self.text[self.text.index(word)] = newWord
                                suggested.append(newWord)
        self.rawText = ''.join(self.text)
        return

    def checkDoubleLetters(self):
        incorrectWords = self.incorrectWords()
        seen = []
        if len(incorrectWords) == 0:
            return 'No incorrectly spelled words detected.'
        for word in incorrectWords:
            listed = list(word)
            for i in range(len(listed) - 1, 0, -1):  # Traverse the word in reverse order (had errors trying to access invalid indices when I tried to traverse forward)
                if listed[i] == listed[i - 1]:  # Checks adjacent characters for sameness
                    listed.pop(i)
            newWord = ''.join(listed)  # Rejoin the list of characters into a word
            if newWord in self.dictionary.dict:
                if newWord not in seen:  # Accounting for repeated incorrect entries
                    print(f'Unknown word: {word}. Did you mean "{newWord}"? Enter "Yes", or "No"')
                    statement = input()
                    if statement == 'Yes':
                        if word not in self.text:
                            if word.capitalize() in self.text:  # To account for capitalized words
                                self.text[self.text.index(word.capitalize())] = newWord.capitalize()
                            else:
                                print(f'"{word}" was not found in its expected location. You must have corrected it already.')
                    else:
                        self.text[self.text.index(word)] = newWord
                    seen.append(newWord)

    def removeDoubleChars(self):
        """
        Removes all set of double characters found in the user's entered passage, and updates their text based on this
        operation, and returns their updated raw passage to them
        :return: the user's updated raw passage after double characters have been removed
        """
        listed = [char for char in self.rawText]  # Creates a list of characters in the passage
        for i in range(len(listed) - 1, 0, -1):  # Encountered index errors trying to traverse the list forward, so this function checks characters from back to front
            if listed[i] == listed[i - 1]:  # Checks adjacent characters for sameness
                if ord(listed[i]) >= 65 and ord(listed[i]) <= 90:   #Accounts for repeated punctuation, which need not be removed in many cases
                    listed.pop(i)   # Removes one of the characters if the above case is true
                if ord(listed[i]) >= 97 and ord(listed[i]) <= 122:
                    listed.pop(i)
        self.rawText = ''.join([str(item) for item in listed])  # Rejoins the characters into a string
        interim = self.rawText.translate(str.maketrans('', '', string.punctuation))
        self.text = interim.split()     # Updates the list of words with removed double characters
        return f'Your passage after removing double letters: {self.rawText}'

    def getText(self):
        """
        Returns the user's raw passage
        :return: the user's entered text
        """
        return self.rawText

    def charsToNums(self):
        """
        Creates a list of all numbers found in the user's text (all numbers less than or equal to 100, and greater than
        zero)
        :return: a list of numbers found in the user's text (<= 100), or a message indicating if no numbers have been
        found within that range
        """
        lowerWords = [word.lower() for word in self.text]  # Makes all words lowercase for detection purposes
        nums = []
        for i in range(len(lowerWords) - 1):
            if lowerWords[i] == 'zero':  # Straightforward: If the word is a number, add that number to the list of numbers
                nums.append(int(0))
            if lowerWords[i] == 'one':
                nums.append(int(1))
            if lowerWords[i] == 'two':
                nums.append(int(2))
            if lowerWords[i] == 'three':
                nums.append(int(3))
            if lowerWords[i] == 'four':
                nums.append(int(4))
            if lowerWords[i] == 'five':
                nums.append(int(5))
            if lowerWords[i] == 'six':
                nums.append(int(6))
            if lowerWords[i] == 'seven':
                nums.append(int(7))
            if lowerWords[i] == 'eight':
                nums.append(int(8))
            if lowerWords[i] == 'nine':
                nums.append(int(9))
            if lowerWords[i] == 'ten':
                nums.append(int(10))
            if lowerWords[i] == 'eleven':
                nums.append(int(11))
            if lowerWords[i] == 'twelve':
                nums.append(int(12))
            if lowerWords[i] == 'thirteen':
                nums.append(int(13))
            if lowerWords[i] == 'fourteen':
                nums.append(int(14))
            if lowerWords[i] == 'fifteen':
                nums.append(int(15))
            if lowerWords[i] == 'sixteen':
                nums.append(int(16))
            if lowerWords[i] == 'seventeen':
                nums.append(int(17))
            if lowerWords[i] == 'eighteen':
                nums.append(int(18))
            if lowerWords[i] == 'nineteen':
                nums.append(int(19))
            if lowerWords[i] == 'twenty':
                if lowerWords[i + 2] == 'one':  # Accounts for numbers separated by hyphens
                    nums.append(int(21))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(22))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(23))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(24))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(25))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(26))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(27))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(28))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(29))
                else:
                    nums.append(int(20))
            if lowerWords[i] == 'thirty':
                if lowerWords[i + 2] == 'one':
                    nums.append(int(31))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(32))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(33))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(34))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(35))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(36))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(37))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(38))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(39))
                else:
                    nums.append(int(30))
            if lowerWords[i] == 'forty':
                if lowerWords[i + 2] == 'one':
                    nums.append(int(41))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(42))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(43))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(44))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(45))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(46))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(47))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(48))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(49))
                else:
                    nums.append(int(40))
            if lowerWords[i] == 'fifty':
                if lowerWords[i + 2] == 'one':
                    nums.append(int(51))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(52))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(53))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(54))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(55))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(56))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(57))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(58))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(59))
                else:
                    nums.append(int(50))
            if lowerWords[i] == 'sixty':
                if lowerWords[i + 2] == 'one':
                    nums.append(int(61))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(62))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(63))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(64))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(65))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(66))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(67))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(68))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(69))
                else:
                    nums.append(int(60))
            if lowerWords[i] == 'seventy':
                if lowerWords[i + 2] == 'one':
                    nums.append(int(71))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(72))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(73))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(74))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(75))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(76))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(77))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(78))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(79))
                else:
                    nums.append(int(70))
            if lowerWords[i] == 'eighty':
                nums.append(int(80))
                if lowerWords[i + 2] == 'one':
                    nums.append(int(81))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(82))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(83))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(84))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(85))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(86))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(87))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(88))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(89))
                else:
                    nums.append(int(80))
            if lowerWords[i] == 'ninety':
                if lowerWords[i + 2] == 'one':
                    nums.append(int(91))
                elif lowerWords[i + 2] == 'two':
                    nums.append(int(92))
                elif lowerWords[i + 2] == 'three':
                    nums.append(int(93))
                elif lowerWords[i + 2] == 'four':
                    nums.append(int(94))
                elif lowerWords[i + 2] == 'five':
                    nums.append(int(95))
                elif lowerWords[i + 2] == 'six':
                    nums.append(int(96))
                elif lowerWords[i + 2] == 'seven':
                    nums.append(int(97))
                elif lowerWords[i + 2] == 'eight':
                    nums.append(int(98))
                elif lowerWords[i + 2] == 'nine':
                    nums.append(int(99))
                else:
                    nums.append(int(90))
        if len(nums) == 0:
            return 'No numbers within range detected in your passage.'
        return f'Numbers found in your passage: {nums}'

    def countWords(self):
        """
        Returns a word count for the user's entered passage
        :return: a word count for the user's text
        """
        counter = 0
        for word in self.text:
            if word not in string.punctuation and word != ' ':
                counter += 1
        return counter