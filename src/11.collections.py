from collections import Counter, OrderedDict
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1

print(cnt)
dir(Counter)
dir(OrderedDict)


od =  OrderedDict()

od["a"] = 1
od["b"]= 2

print(od)

odu = dict(od)

odu['test'] = 100
odu['nevermid'] = 1212
print(str(odu))


sentence = 'HI I am working on ythong to practice it to get good hands on'
[len(word) for word in sentence.split() if len(word) > 3]
[ [word]*3  for word in sentence.split() if len(word) > 3]


def gen123():
        yield 1
        yield 2
        yield 3
        return

g = gen123()

try:
        print(next(g))        
        print(next(g))        
        print(next(g))     
        print(next(g))        
except StopIteration as e:
        print("Finished elements in generator")
        
print("program ended")


locals()
collections.__file__
collections.__path__