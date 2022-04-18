from dictionary import Dictionary
from spellchecker import SpellChecker

dict = Dictionary()
dictName = input('Hello! Enter the name of your dictionary: ')
dict.setDictionary(dictName)

key = int(input('Welcome to SpellChecker! Please see the menu below for your options.\n1: Enter text to check\n'
            '2: Check your spelling\n3: Print your passage\n4: Remove all double letters in your passage\n5: Get a list'
            ' of numbers (<= 100) found in your passage\n6: Inspect your dictionary\n7: Get a word count for your'
            'passage\n8: Exit the application\n'))
while key != 8:
    if key == 1:
        text = input('Enter a passage of text: ')
        checker = SpellChecker(dict, text)
        print('Process complete.')
    elif key == 2:
        checker.getIncorrectWords()
        print(checker.suggest())
    elif key == 3:
        print(checker.getText())
    elif key == 4:
        print(checker.removeDoubleLetters())
    elif key == 5:
        print(checker.getNums())
    elif key == 6:
        print(dict.getDictionary())
    elif key == 7:
        print('Word count:', checker.countWords())
    key = int(input('\nEnter your next action\n1: Enter text to check\n2: Check your spelling\n3: Print your passage\n4:'
                    ' Remove all double letters in your passage\n5: Get a list of numbers (<= 20) found in your '
                    'passage\n6: Inspect your dictionary\n7: Get a word count for your passage\n8: Exit the '
                    'application\n'))
print('Thank you for using my spell checker!')