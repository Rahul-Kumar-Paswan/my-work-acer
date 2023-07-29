import math
n=int(input())
m=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
""" r=0
x=min(l1)
y=max(l1)

i=min(l2)
j=max(l2)

print(l1)
print(l2)

if  y>j:
    r=y-i
else:
    print("else")
    r=j-x """

""" 
if min(l1)>max(l2):
    print("first",min(l1)-max(l2))
else:
    print(max(l2)-min(l1)) """
# print(r)



md=float('-inf')
for n in l1:
    for i in l2:
        d=abs(n-i)
        if d>md:
            md=d

print(md)
