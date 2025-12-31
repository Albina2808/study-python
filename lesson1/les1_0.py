n1=20
n2=3
n3 = n1+n2
print(n3)

n4=n1-n2
print(n4)

n5=n1*n2
print(n5)

n6=n1/n2
print(n6)

n7=n1//n2
print(n7)

n8=n1%n2
print(n8)

n9=n1**n2
print(n9)

n10=n1==n2
print(n10)

n11=n1>n2
print(n11)

n12=n1<n2
print(n12)

n13=n1>=n2
print(n13)

n14=n1<=n2
print(n14)

n15=n1!=n2
print(n15)

result1 = n3 >18 or n15 == True
print("Result1:" + str(result1))

result2 = n3 >25 and n15 == True
print("Result2:" + str(result2))

result3 = not n3 >25 and n15 == True
print("Result3:" + str(result3))

result4 = not n3 >25 and not n15 == True
print("Result4:" + str(result4))

result5 = n3 >18 or n15 == False
print("Result5:" + str(result5))

name = "Albina"
message = "Alina has found a new job."
print (not name in message)

name = "Albina"
message = "Albina has found a new job."
print (name in message)

print(type(n1))
print(type(n6))
print(type(result1))
print(type(name))

l1 = (1,2,2,3,4)
print(type(l1))

l2 = {5,2,3,5}
print(type(l2))

l3 = {'name': "Albina", 'age': 18}
print(type(l3))

l4 = [1,2,2,3,4]
print(type(l4))

print(type(None))

class Person:
    pass
a = Person()
print(type(a))