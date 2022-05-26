l=["apple", "banana", "keri", "joker"]
print (l)
n =[2, 36, 54, 65, 9]
print [n]
print (l+n)
n.append(56)
print(n)

#n.sort()
#print (n)
#n.reverse()
#print (n)

print (n[2])
print (l[2])
print (n[1:5])
print (n[1:6:2])
print (n[1:6:3])
n.insert(2, 89)
print (n)
n.pop(3)
print (n)
n.remove(2)
print (n)
n.remove(56)
print (n)

tp=("keri", 56, "car", 14)
print (tp)

a = 2
b = 6

#temp = a
#a= b
#b = temp
#print (a, b)

a, b = b,a
print (a, b)

a= 1
b = 8
a, b = b,a
# temp = a
# a = b
# b = temp
print(a, b)

print (min(n))
print (max(n))
print (type(n))
print (type(tp))
