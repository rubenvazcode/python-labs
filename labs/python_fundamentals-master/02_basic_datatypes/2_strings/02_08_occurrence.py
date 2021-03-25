'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
# get sentence
sentence = input("Insert a sentence: ")
# get letter
letter = input("Chose a letter: ")
# print the place of the letter
print(sentence.find(letter))
