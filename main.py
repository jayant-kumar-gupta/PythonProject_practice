text = input("Enter any string. ").lower()
mydict = {}
for letter in set(text):
    if letter == " ":
        continue
    mydict[letter] = text.count(letter)

result = sorted(mydict.items(), key= lambda x: x[1], reverse=True)
print(dict(result))
