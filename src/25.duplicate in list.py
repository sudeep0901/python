import collections

ls = [3, 99,3 ,35,44,6 , 6, 6, "Hello"]

itm = [ (item ,count) for item,count in collections.Counter(ls).items() if count > 1]
itm

seen = set()
uniq = []
print(ls.count(6))

for x in ls:
    print(x, ls.count(x))

for x in ls:
    print(x)
    if x not in seen:
        uniq.append(x)
        seen.add(x)
print(seen, uniq)

seen.add(6)
seen

res = map(str, ls)
for v in res:
    print(v, type(v)) 

# next(res)
sentence = ['this','is','a','sentence']
sentence
'0'.join(sentence)
