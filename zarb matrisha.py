import random
n = int(input('enter n:'))
m = int(input('enter n:')) 
k = int(input('enter n:'))  
mx1 = [[random.randint(1,10) for i in range(n)] for j in range(m)]
mx2 = [[random.randint(1,10) for i in range(k)] for j in range(n)]
res = [[0 for i in range(k)] for j in range(m)]

print('matrix1 :')
for i in range(m):
    for j in range(n):
        print(mx1[i][j] , end=' ') 
    print()

print('matrix2 :')
for i in range(n):
    for j in range(k):
        print(mx2[i][j] , end=' ') 
    print()

for i in range(m):
    for j in range(k):
        for h in range(n):
            res[i][j]+=(mx1[i][h] * mx2[h][j])
print(res)
