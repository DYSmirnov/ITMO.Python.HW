"""string1 = "This is a string."
string2 = " This is another string."
string3 = "This is a string.  "
print(string1 + string2)
print("Len string1: ", len(string1))
print(string1.title())
print(string1.lower())
print(string2.upper())
print("strip - ", string2.strip())
print("strip (This)- ", string2.strip('This '))
print("rtrip - ", string3.rstrip())
print("ltrip - ", string2.lstrip())


d = "qwerty"
ch = d[2]
print (ch)
chm = d[1:3]
print (chm)
print(d[1:])
print(d[:3])
print(d[:])
print(d[1:5:2])
print(d[1::2])


a = 9
b = 5
print(a/b)
print(a//b)
print(a%b)
param = "string" + str(15)
print(param)

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " + " + n2 + " = ", n3)


a = 1/3
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a,b))
print("{:10.3f} {:10.3f}".format(a,b))


list1 = [5, 89, 65, 2, 77,3]
print(dir(list1))
list1.append(10)
list1.insert(0,33)
print(list1)
list1.pop(0)
print(list1)
del list1[-1]
print(list1)
list1.sort()
print(list1)
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(list2)
print(lis)



seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(listseq)
print(listseq[3])
print(len(listseq))



D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] +=10
print(D['quantity'])
dp ={}
print("Enter your name")
dp['name'] = input()
print("Enter your age")
dp['age'] = int(input())
for k, v in dp.items():
    print(k, v)
"""

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 25}
print(rec['name']['firstname'])
rec['job'].append('janitor')
for k, v in rec.items():
    print(k, v)