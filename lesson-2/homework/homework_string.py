#Q1
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.")

#Q2
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]
print(f"Car 1: {car1}, Car 2: {car2}")

#q3
string=str(input("Enter a string: "))
print("string lenth:", len(string))
print("string uppercase", string.upper())
print("string lowercase", string.lower())

#q4
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
#q5
string1=input("Enter a string: ")
vowels='eaiuo'
vowels_num=sum(1 for char in string1 if char in vowels)
consonant_num=sum(1 for char in string1 if char.isalpha() and char not in vowels)
print(f'Vowels: {vowels_num} and Consonants: {consonant_num}')

#q6
str1=input("Enter a main string: ")
str2=input("enter string: ")
if str2 in str1:
    print("it exists")
else:
    print("it doesn't exist")

#q7
sentence=input("Enter a sentence: ")
old_word=input("Enter a word to replace: ")
new_word=input("Enter a new word: ")
print("New sentence: ", sentence.replace(old_word, new_word))

#q8
str=input("Enter a string: ")
print(f"first character: {str[0]}")
print(f"last character: {str[-1]}")

#q9
string2=input("Enter a string: ")
print("reversed string: ", string2[::-1])

#q10
string3=input("Enter a string: ")
word=string3.split()
print("number of words:", len(word))

#q11
string4=input("Enter a string: ")
if any(char.isdigit() for char in string4):
    print("contains digits")
else:
    print("does not contain digits")

#q12
string5=input("Enter words separated by spaces: ").split()
words=",".join(string5)
print("Joined words:", words)

#q13
string6=input("Enter a string: ")
nospace=string6.replace(" ", "")
print(nospace)

#14
string7=input("Enter a string: ")
string8=input("Enter a string2: ")
if string7==string8:
    print("yes")
else:
    print("no")

#q15
string9=input("Enter a string: ").split()
acronym=''.join(word[0].upper()for word in string9)
print(acronym)

#q16
string10=input("Enter a string: ")
remove=input("Enter a str to remove: ")
new_text=string10.replace(remove,"")
print(new_text)

#q17
string11=input("Enter a string: ")
vowels="AOIUEaoiue"
for vowel in vowels:
    string11=string11.replace(vowel,"*")
print(string11)

#q18
string12=input("Enter a string: ").split()
print("starts with:", string12[0], "and ends with:", string12[-1])






