#""""
#write a script that will ask for a string and tell 
#if a letter in the string is a vowel or consonant
#"""
my_string=input("please enter a word: ").strip()


for i in my_string:
    if i in 'aeiou':
       print(f"{i} is a vowel")
    else:
        print(f"{i} is a consonant")
