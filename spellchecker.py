from dictionary import Dictionary
import string


class SpellChecker:
    def __init__(self, dictionary: Dictionary, text):
        """
        Object declaration for a spell checker
        :param dictionary: the dictionary that the user will be checking their text against (for the purposes of our
        class, English is the only provided dictionary
        :param text: the text that the user wants to check for spelling errors
        """
        self.dictionary = dictionary
        finalText = text.translate(str.maketrans('', '', string.punctuation))  # Removes punctuation from word list
        self.text = finalText.split()   # List of words to operate on for spell checking
        self.rawText = text     # Actual passage entered by user

    def incorrectWords(self):
        """
        Compares the user's entered text against the dictionary that was chosen, and returns a list of incorrectly
        spelled words
        :return: a list of words not found in the provided dictionary
        """
        incorrect = []
        for word in self.text:
            if word not in self.dictionary.dict:
                finalChecker = chr(ord(word[0]) + 32) + word[1:]  # Accounts for uppercase characters (not present in the dictionary I make use of)
                if finalChecker not in self.dictionary.dict:  # Adds the word to the incorrect list if it cannot be found in the dictionary
                    incorrect.append(word)
        return incorrect

    def getIncorrectWords(self):
        """
        Returns a list of incorrectly spelled words (for user inspection, rather than code operation)
        :return: a string including a list of words that were not found in the user's chosen dictionary
        """
        return f'Incorrectly spelled words: {self.incorrectWords()}'

    def suggest(self):
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
                for j in range(1, len(word)):
                    listed = list(word)     # Creates a list of characters for each word, and swapping characters based on indices i and j
                    listed[i], listed[j] = listed[j], listed[i]
                    newWord = ''.join(listed)   # Rejoin the list of characters into a word
                    if newWord in self.dictionary.dict:
                        if word not in suggested:  # Accounting for repeated incorrect entries
                            print('Unknown word: ', word, '. Did you mean "', newWord, '"?', sep='')
                            suggested.append(word)
        return

    def removeDoubleLetters(self):
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

    def getNums(self):
        """
        Creates a list of all numbers found in the user's text (all numbers less than or equal to 100, and greater than
        zero)
        :return: a list of numbers found in the user's text (<= 100), or a message indicating if no numbers have been
        found within that range
        """
        lowerWords = [word.lower() for word in self.text]  # Makes all words lowercase for detection purposes
        nums = []
        for word in lowerWords:
            if word == 'zero':  # Straightforward: If the word is a number, add that number to the list of numbers
                nums.append(int(0))
            if word == 'one':
                nums.append(int(1))
            if word == 'two':
                nums.append(int(2))
            if word == 'three':
                nums.append(int(3))
            if word == 'four':
                nums.append(int(4))
            if word == 'five':
                nums.append(int(5))
            if word == 'six':
                nums.append(int(6))
            if word == 'seven':
                nums.append(int(7))
            if word == 'eight':
                nums.append(int(8))
            if word == 'nine':
                nums.append(int(9))
            if word == 'ten':
                nums.append(int(10))
            if word == 'eleven':
                nums.append(int(11))
            if word == 'twelve':
                nums.append(int(12))
            if word == 'thirteen':
                nums.append(int(13))
            if word == 'fourteen':
                nums.append(int(14))
            if word == 'fifteen':
                nums.append(int(15))
            if word == 'sixteen':
                nums.append(int(16))
            if word == 'seventeen':
                nums.append(int(17))
            if word == 'eighteen':
                nums.append(int(18))
            if word == 'nineteen':
                nums.append(int(19))
            if word == 'twenty':
                nums.append(int(20))
            if word == 'twentyone':  # Accounts for numbers separated by parentheses (i.e. twenty-one), I also had to account for this in the dictionary
                nums.append(int(21))
            if word == 'twentytwo':
                nums.append(int(22))
            if word == 'twentythree':
                nums.append(int(23))
            if word == 'twentyfour':
                nums.append(int(24))
            if word == 'twentyfive':
                nums.append(int(25))
            if word == 'twentysix':
                nums.append(int(26))
            if word == 'twentyseven':
                nums.append(int(27))
            if word == 'twentyeight':
                nums.append(int(28))
            if word == 'twentynine':
                nums.append(int(29))
            if word == 'thirty':
                nums.append(int(30))
            if word == 'thirtyone':
                nums.append(int(31))
            if word == 'thirtytwo':
                nums.append(int(32))
            if word == 'thirtythree':
                nums.append(int(33))
            if word == 'thirtyfour':
                nums.append(int(34))
            if word == 'thirtyfive':
                nums.append(int(35))
            if word == 'thirtysix':
                nums.append(int(36))
            if word == 'thirtyseven':
                nums.append(int(37))
            if word == 'thirtyeight':
                nums.append(int(38))
            if word == 'thirtynine':
                nums.append(int(39))
            if word == 'forty':
                nums.append(int(40))
            if word == 'fortyone':
                nums.append(int(41))
            if word == 'fortytwo':
                nums.append(int(42))
            if word == 'fortythree':
                nums.append(int(43))
            if word == 'fortyfour':
                nums.append(int(44))
            if word == 'fortyfive':
                nums.append(int(45))
            if word == 'fortysix':
                nums.append(int(46))
            if word == 'fortyseven':
                nums.append(int(47))
            if word == 'fortyeight':
                nums.append(int(48))
            if word == 'fortynine':
                nums.append(int(49))
            if word == 'fifty':
                nums.append(int(50))
            if word == 'fiftyone':
                nums.append(int(51))
            if word == 'fiftytwo':
                nums.append(int(52))
            if word == 'fiftythree':
                nums.append(int(53))
            if word == 'fiftyfour':
                nums.append(int(54))
            if word == 'fiftyfive':
                nums.append(int(55))
            if word == 'fiftysix':
                nums.append(int(56))
            if word == 'fiftyseven':
                nums.append(int(57))
            if word == 'fiftyeight':
                nums.append(int(58))
            if word == 'fiftynine':
                nums.append(int(59))
            if word == 'sixty':
                nums.append(int(60))
            if word == 'sixtyone':
                nums.append(int(61))
            if word == 'sixtytwo':
                nums.append(int(62))
            if word == 'sixtythree':
                nums.append(int(63))
            if word == 'sixtyfour':
                nums.append(int(64))
            if word == 'sixtyfive':
                nums.append(int(65))
            if word == 'sixtysix':
                nums.append(int(66))
            if word == 'sixtyseven':
                nums.append(int(67))
            if word == 'sixtyeight':
                nums.append(int(68))
            if word == 'sixtynine':
                nums.append(int(69))
            if word == 'seventy':
                nums.append(int(70))
            if word == 'seventyone':
                nums.append(int(71))
            if word == 'seventytwo':
                nums.append(int(72))
            if word == 'seventythree':
                nums.append(int(73))
            if word == 'seventyfour':
                nums.append(int(74))
            if word == 'seventyfive':
                nums.append(int(75))
            if word == 'seventysix':
                nums.append(int(76))
            if word == 'seventyseven':
                nums.append(int(77))
            if word == 'seventyeight':
                nums.append(int(78))
            if word == 'seventynine':
                nums.append(int(79))
            if word == 'eighty':
                nums.append(int(80))
            if word == 'eightyone':
                nums.append(int(81))
            if word == 'eightytwo':
                nums.append(int(82))
            if word == 'eightythree':
                nums.append(int(83))
            if word == 'eightyfour':
                nums.append(int(84))
            if word == 'eightyfive':
                nums.append(int(85))
            if word == 'eightysix':
                nums.append(int(86))
            if word == 'eightyseven':
                nums.append(int(87))
            if word == 'eightyeight':
                nums.append(int(88))
            if word == 'eightynine':
                nums.append(int(89))
            if word == 'ninety':
                nums.append(int(90))
            if word == 'ninetyone':
                nums.append(int(91))
            if word == 'ninetytwo':
                nums.append(int(92))
            if word == 'ninetythree':
                nums.append(int(93))
            if word == 'ninetyfour':
                nums.append(int(94))
            if word == 'ninetyfive':
                nums.append(int(95))
            if word == 'ninetysix':
                nums.append(int(96))
            if word == 'ninetyseven':
                nums.append(int(97))
            if word == 'ninetyeight':
                nums.append(int(98))
            if word == 'ninetynine':
                nums.append(int(99))
            if word == 'onehundred':
                nums.append(int(100))
        if len(nums) == 0:
            return 'No numbers within range detected in your passage.'
        return f'Numbers found in your passage: {nums}'

    def countWords(self):
        """
        Returns a word count for the user's entered passage
        :return: a word count for the user's text
        """
        return len(self.text)