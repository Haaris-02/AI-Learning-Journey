#funtion with return value and without return value
def print_values():
    a = 10
    b = 20
    c = a + b
    return c

a=print_values()
print(a)

def print_values2() :
    a = 10
    b = 20
    c = a * b
    print(c)

print_values2()

#list
lis=[]
for i in range(1,11):
    lis.append(i)
print(lis)

#dictionary
dict1={}    
for i in range(1,11):
    dict1[i]=i*i
print(dict1)

#get(),items(),keys(),values()
print("get()",dict1.get(5))
print("items()",dict1.items())
print("keys()",dict1.keys())
print("values()",dict1.values())

#OOPS basics class,object,init, self
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

p1=Person("Alice",30)
p1.display()