row_a=int(input("ENTER NO OF ROWS FOR MATRIX A:"))
col_a=int(input("ENTER NO OF COLUMNS FOR MATRIX A:"))
a=[]
print("ENTER ELEMENTS FOR MATRIX A :")
for i in range(row_a):
    l=[]
    for j in range(col_a):
        l.append(int(input("ENTER ELEMENTS :")))
    a.append(l)

row_b=int(input("ENTER NO OF ROWS FOR MATRIX B:"))
col_b=int(input("ENTER NO OF COLUMNS FOR MATRIX B:"))

if col_a != row_b :
    print("MATRIX MULTIPLICATION NOT POSIBLE ")
    exit(0)

print("ENTER ELEMENTS FOR MATRIX B :")
b=[]
for i in range(row_b):
    l=[]
    for j in range(col_b):
        l.append(int(input("ENTER ELEMENTS :")))
    b.append(l)

print("PRINTING MATRIX A :")
for i in a:
    print(i)

print("PRINTING MATRIX B :")
for i in b:
    print(i)

ans = [[0 for i in range(col_b)] for j in range(row_a)]
print(ans)
# ans = [[0]*col_b]*row_a
# print(ans)
# print(len(ans))
# print(len(ans[0]))

for i in range(len(ans)):
    for j in range(len(ans[0])):
        ans[i][j]=1
        print(ans[i][j],end=' ')

print("MULTIPLICATION OF TWO MATRIX :")

for i in range(row_a):
    for j in range(col_b):
        for k in range(row_b):
            ans[i][j]+= a[i][k] * b[k][j] 
        print(ans[i][j])

for i in ans:
    print(i)