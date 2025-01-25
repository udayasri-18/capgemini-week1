sentence = input("Enter a sentence: ")
words=sentence.split()
count={}

for word in words:
    word=word.lower()
    count[word]=count.get(word,0)+1

print(f"{count}")