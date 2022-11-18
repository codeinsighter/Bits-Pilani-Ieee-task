#q5
import itertools

finalSet = []

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

 
s = list(input("Enter list:"))
s.remove("[")
s.remove("]")

for i in range(int((len(s)-1)/2)):
    s.remove(',')

for j in range(len(s)+1):
    temp = findsubsets(s,j)
    for i in range(len(temp)):
        finalSet.append(temp[i])

print(finalSet)