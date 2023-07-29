n=int(input())
l=list(map(int,input().split()))[:n]
x=min(l)
y=max(l)
l.sort()
# print(l)
c=0
for i in range(x,y+1):
    if i not in l:
        c=c+1
        # print(i)
print(c)
