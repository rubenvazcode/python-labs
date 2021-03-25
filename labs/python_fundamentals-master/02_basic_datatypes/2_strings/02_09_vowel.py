'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
# get sentece from user
sentence = input("please insert a sentence: ")
sentence = sentence.lower()
# define list of vowels
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
# count the vowels and print the total
acount = sentence.count(a)
ecount = sentence.count(e)
icount = sentence.count(i)
ocount = sentence.count(o)
ucount = sentence.count(u)
# presenting the results
tvowels = acount + ecount + icount + ocount +ucount
print("The total number of vowels in this sentence are: ", tvowels)
print('The number of "a" are: ', acount)
print('The number of "e" are: ', ecount)
print('The number of "i" are: ', icount)
print('The number of "o" are: ', ocount)
print('The number of "u" are: ', ucount)
