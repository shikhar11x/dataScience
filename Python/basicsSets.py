s1={1,5,4,6,15,12,15}
print(s1)
s2=set() #empty set

item={"apple", "banana","orange"}
item.add("grapes")
print(item)
item.update(["mango",'peach'])
print(item)
item.remove("banana")
print(item)
item.discard("lemon")
print(item)
a=item.pop()
print(a)
print(item)


# >>>> Set Operations <<<<
a={1,2,3,4}
b={4,5,6}
print(a.union(b))
print(a.intersection(b))