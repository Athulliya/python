num=input("enter an integer list(space separated):")
num=list(map(int,num.split()))
num=[x for x in num if x%2!=0]
print("list after removing even numbers",end='')
print(num)
