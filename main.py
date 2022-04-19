from dictionary import Dictionary
from spellchecker import SpellChecker

dict = Dictionary()
state = True
key = 0
while state:
    try:
        dictName = input('Hello! Enter the name of your dictionary (Current options: english.txt, '
                         'english_extended.txt (not recommended), espanol.txt for Spanish,\nitaliano.txt for '
                         'Italian, francais.txt for French, and deutsch.txt for German): ')
        dict.setDictionary(dictName)
        state = False
    except FileNotFoundError:
        print('Invalid file name. Try again.')
state = True
key = 1
print('Welcome to SpellChecker!')
while key != 9:
    if key == 1:
        text = input('Enter a passage of text (numbers in word form will work best): ')
        checker = SpellChecker(dict, text)
        print('Process complete.')
    elif key == 2:
        print(checker.suggestWords())
    elif key == 3:
        print(checker.checkDoubleLetters())
    elif key == 4:
        print(checker.getText())
    elif key == 5:
        print(checker.removeDoubleLetters())
    elif key == 6:
        print(checker.charsToNums())
    elif key == 7:
        print(dict.getDictionary())
    elif key == 8:
        print('Word count:', checker.countWords())
    state = True
    while state:
        try:
            key = int(input('\nEnter your next action\n1: Enter text to check\n2: Check your spelling by character '
                            'swapping\n3: Check '
                            'spelling by removing double letters\n4: Print your passage\n5: Remove all double letters '
                            'in your passage\n6: Get a list of numbers (<= 20, only functional in English) found in your '
                            'passage\n7: Inspect your dictionary\n8: Get a word count for your passage\n9: Exit the '
                            'application\n'))
            if key < 10 and key > 0:
                state = False
            else:
                print('Number not in range. Try again.')
        except ValueError:
            print('Invalid input. Try again.\n')
print('Thank you for using SpellSafe!')