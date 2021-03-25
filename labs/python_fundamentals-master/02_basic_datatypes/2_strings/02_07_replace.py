'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# get sentence from user
sentence = input("Insert a sentence: ")
# get symbol
symbol = input("Chose a symbol: ")
# get first letter
first = sentence[0]
# replace occurences with symbol
print(sentence.replace(first, symbol))
