dicta = {'a':1,'b':2,'c':3,'d':4,'f':'hello'}
dictb = {'b':3,'d':5,'e':7,'m':9,'k':'world'}

dic = {}
for key1 in dicta:
    for key2 in dictb:
        if key1 == key2:
            dic[key1] = dicta[key1] + dictb[key2]

for a in dicta:
    if a not in dic:
        dic[a] = dicta[a]

for b in dictb:
    if b not in dic:
        dic[b] = dictb[b]
print(dic)
# dictc = {'a':1,'b':5,'c':3,'d':9,'e':7,'m':9,'f':'hello','k':'world'}