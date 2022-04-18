class Dictionary:
    def __init__(self, dict=[]):
        """
        Creates a dictionary object for which spell checking is necessary
        :param words: a list of accepted words in that dictionary
        """
        self.dict = dict

    def setDictionary(self, dictName):
        """
        Sets the user's dictionary by entering the name of their dictionary in a txt file (must be UTF characters)
        :param dictName: the file name of their dictionary
        """
        with open(dictName, encoding='utf8') as f:  # Reads each word from the dictionary
            for line in f:
                self.dict.extend(line.split())  # Adds each word to the list

    def getDictionary(self):
        """
        Returns the user's dictionary to them
        :return: the user's chosen dictionary
        """
        return self.dict