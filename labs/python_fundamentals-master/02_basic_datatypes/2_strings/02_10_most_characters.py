'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
# get the user
f_word = input("Please insert the first word: ")
s_word = input("Please insert the second word: ")
t_word = input("Please insert the third word: ")
# get the length of each input
first = (len(f_word))
second = (len(s_word))
third = (len(t_word))
# assuming that the str have all different sizes
if first > second:
    if first > third:
        print(len(f_word), ",", f_word)
    else:
        print(len(t_word), ",", t_word)
elif second > third:
    print(len(s_word), ",", s_word)
else:
    print(len(t_word), ",", t_word)

# print all the results
print("All the results are:")
print(len(f_word),",", f_word)
print(len(s_word),",", s_word)
print(len(t_word),",", t_word)