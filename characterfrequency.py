dict={}
str1=input("enter a string")
for n in str1:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
print("character frequency")
for k,v in dict.items():
    print(k,v)
