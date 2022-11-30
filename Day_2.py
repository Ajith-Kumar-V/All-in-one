le=int(input())
arr=[x for x in input().split()][:le]
s=0
for i in arr:
    s+=int(i)
print(s)
