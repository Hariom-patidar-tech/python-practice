# Find Element of maximum frequency

a = "helloworld"
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
        
        
        
# Find Frequency of each elements: [1,1,2,3,3,2,3]
a = [1,1,2,3,3,2,3]
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)