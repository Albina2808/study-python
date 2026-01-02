list1 = [1,2,8,6]
dict1 = {'name':'Albina', 'age': 8}
name= 'Albina'
tupl1= ('n','a','g')
result1 = dict1['age'] in list1 and dict1['name'] in tupl1
print(result1)

n1='1'
n1=int(n1)
print(type(n1))

string1="Albina"
print(len(string1))
print(string1.upper())
print(string1.lower())
print(string1.capitalize())
print(string1.replace("a","o"))
print(string1.split('i'))

string2 = 'hello world'
print(string2.split())
print(''.join(string2))
print(string2.count('o'))

base_list = [1,2,3]
print(len(base_list))
base_list.append(4)
print(base_list)
base_list.extend([5,6,7])
print(base_list)
print(base_list.index(4))

base_dict={'name':'Tom', 'age': 8, 'high':163}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())
print(base_dict['name'])
print(base_dict.get('name'))
print(base_dict.get('is animal', 'Not an animal'))