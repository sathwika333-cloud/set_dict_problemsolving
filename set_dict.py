a={1,2,3}
a.add(4)
print(a)

a={1,2,3,4}
a.remove(4)
print(a)

a={1,2,3,4}
b={1,2,4}
r=a.union(b)
print(r)

a={1,2,3}
b={1,2,4}
r=a.intersection(b)
print(r)

a={1,2,3}
b={1,2}
r=a.difference(b)
print(r)

a={1,2}
b={1,2,3}
r=a.issubset(b)
print(r)

a={1,2,3}
print(len(a))

a={1,2,3}
a.clear()
print(a)

a={1,2,3,4}
b={2,3}
r=a.symmetric_difference(b)
print(r)

a=[1,2,2,3]
print(set(a))

a=['a','b','c']
b=[1,2,3]
r=dict(zip(a,b))
print(r)

a={"a":1,"b":2}
a["a"]=3
print(a)
a.update({"c":4})
print(a)

a={'a':1,'b':2,'c':3}
a.pop("a")
print(a)
del a['b']
print(a)

s={'a':1,'b':2,'c':3}
print('a' in s)

s={'a':1,'b':2}
for i,j in s.items():
    print(i,j,end=' ')

a={"a":1,"b":2}
print(len(a))

a={"a":1}
b={"b":2}
a.update(b)
print(a)

a={"a":1}
r=a.get("b")
print(r)

def freq(lst):
  res={}
  for num in lst:
    res.update({num:lst.count(num)})
  return res
print(freq([1,2,2,3]))

s={"a":1,"b":2}
flip={}
for k,v in s.items():
  flip[v]=k
print(flip)

s={"a":12,"b":89,"c":9}
res=max(s, key=s.get)
print(res)

d = {"a": 3, "b": 1, "c": 2}
res = sorted(d.items(), key=lambda x: x[1])
print(res)

sq={}
for i in range(1,4):
  sq[i]=i*i
print(sq)

d={"a": 10, "b": 5, "c": 15}
res={key:value for key,value in d.items() if value>10}
print(res)

d1 = {"a": 1, "b": 2}
d2 = {"a": 3, "c": 4}
res = d1.copy()
for key in d2:
    if key in res:
        res[key] = res[key] + d2[key]
    else:
        res[key] = d2[key]
print(res)

n="apple banana apple"
sen=n.split()
d={}
for i in sen:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(d)

n = {"a": 1, "b": 2, "c": 1}
res = {}
for key, value in n.items():
    if value not in res.values():
        res[key] = value
print(res)

d1={"a":1,"b":2}
d2={"b":3,"c":4}
res=[]
for key in d1:
  if key in d2:
    res.append(key)
print(res)

n={"x":1,"y":2}
res={v:k for k,v in n.items()}
print(res)

n = {"a": 1, "b": 2, "c": 1}
res = {}
for key, value in n.items():
    if value != 1:
        res[key] = value
print(res)