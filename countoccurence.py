strl=input("enter a string:")
counts=dict()
words=strl.split()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
for k,v in counts.items():
    print (k,v)
