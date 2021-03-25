'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
#get name
name = input("Please insert your name: ")
# move first leter to end and add ay
f_letter = name[0]
print("your pig latin name is: " + name[1:] + name[0]+'ay')
