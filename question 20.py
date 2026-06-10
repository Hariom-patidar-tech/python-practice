# Convert list of strings to uppercase
a = "hariom"
print(a.upper())



lst = ["hariom", "python", "ai"]
for i in range(len(lst)):
    new_word = ""
    for ch in lst[i]:
        if 'a' <= ch <= 'z':
            new_word += chr(ord(ch) - 32)
        else:
            new_word += ch
    lst[i] = new_word

print(lst)