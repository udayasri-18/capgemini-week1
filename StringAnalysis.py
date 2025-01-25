str1=input("Enter a string ")
vowels=0
consonant=0
digits=0
special=0
for i in str1:
    if i.isdigit():
        digits+=1
    elif i in ['a','e','i','o','u']:
        vowels+=1
    elif i in ['b','c','d','f','g','h','j','k','l','m','n''q','p','r','s','t','v','w','x','y','z']:
        consonant+=1
    else:
        special+=1

print(f"Number of Vowels in the string are {vowels}")  
print(f"Number of Consonants in the string are {consonant}")
print(f"Number of Digits in the string are {digits}")
print(f"Number of special in the string are {special}")