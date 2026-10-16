# playfair cipher

import string

key = "MONARCHY"
alphas = string.ascii_uppercase

mat = [[] for i in range(5)]

j = 0
for i in key:
    j = j%5
    if i == 'I':
        mat[j].append('IJ')
    elif i == 'J':
        continue
    else:
        mat[j].append(i)
    j+=1

for i in alphas:
    if not any (i in row for row in mat):
        j = j%5
        if i == 'I':
            mat[j].append('IJ')
        elif i == 'J':
                continue
        else:
            mat[j].append(i)
        j+=1

print(mat)
