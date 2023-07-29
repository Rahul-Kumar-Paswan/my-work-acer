str = input()

key = ''
ans = ''
first=''
last=''

if len(str)>6:
    key = str[:6]
else:
    key = str[:]

mid=key[len(key)//2]

for i in range(len(key)//2):
    first =key[i]+first

for i in range((len(key)//2)+1,len(key)):
    last =key[i]+last

print(mid+'@'+first+'341'+last)
