gorcery =["Banana","Water","Mouse","Watch","Keychain",
          "TV","Mobile"]
print(gorcery)
print(gorcery[1])
print(gorcery[1:6])
print(gorcery[1:4:2])
print(gorcery[-3])
print(gorcery[-1:-5])
print(gorcery[::-1])

numbers = [234,565,678,4356,789,65765,9808,56,78,75,89,5,67,89]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort()
numbers.reverse()
print (numbers)

print(type(numbers))
print(len(numbers))
print(max(numbers))
print (min(numbers))

numbers.append(345)
numbers.append(78435943)
numbers.append(454679780)
print(numbers)

numbers.insert(1,000)
numbers.insert(4,1000)
print(numbers)

numbers.remove(0)
numbers.remove(565)
print(numbers)

numbers.pop()
print(numbers)

numbers[1]=342
print(numbers)
numbers[14]=67524
print(numbers)


tuple=(1,4,8,23,64)
print(tuple)
tup=((1))
print(tup)

a= 1
b=8
temp = a
a = b
b = temp
print(a,b)

c = 43
d = 90
c , d = d , c
print(c,d)
