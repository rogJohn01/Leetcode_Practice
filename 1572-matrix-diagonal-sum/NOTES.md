## 1. half two pointer! -> need for odd&even !!
```
​
​
def diagonal(mat):
​
a = 0 ; b = C -1
for r in range(R):
for c in range(C):
if r==c:
sumv += mat[r][c]
elif  r == a and c ==b:
sumv += mat[r][c]
a +=1 ; b -=1
​
​
```