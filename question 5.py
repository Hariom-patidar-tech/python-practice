# Count Frequency of Each Character

a = "hello"
freq = {}
for ch in a:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq) 
    
    
    
a = "helloworld"
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)