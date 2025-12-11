
"""def extendList(val, list=[]):
    if not list:
        list=[]
        list.append(val)
    else:
        list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,['23','we'])
list3 = extendList('a')



print ("list1 = %s" %list1)
print ("list2 = %s" %list2)
print ("list3 = %s" %list3)


matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col])"""

# sorted_by_key = sorted([
# {'name': 'Bina', 'age': 30},
# {'name':'Andy', 'age': 18},
# {'name': 'Zoey', 'age': 55}],
# key=lambda el: (el['name']))
# print(sorted_by_key)

# sorted_by_second = sorted(['hi', 'afgh' ,'yau','man', 'dghj'], key=lambda el: el[2])
# print(sorted_by_second)

# element_sum = [sum(pair) for pair in zip([1,2,3,4],[4,5,6,5],[7,8,9,10])]
# print(element_sum)

# msg = ''
# while msg != 'quit':
#     msg = input("What should I do?")
#     print(msg)

# for i, el in enumerate('helloo'):
#     print(f'{i}, {el}')

# from collections import OrderedDict
# # Store each person's languages, keeping # track of who responded first.
# programmers = OrderedDict()
# programmers['Tim'] = ['python', 'javascript']
# programmers['Sarah'] = ['C++']
# programmers['Bia'] = ['Ruby', 'Python', 'Go']
# for name, langs in programmers.items():
#     print(name + '-->')
#     for lang in langs:
#         print('\t' + lang)

# def f(x, *args):

# [*[1,2,3], *[4]] # [1, 2, 3, 4]
# {*[1,2,3], *[4]} # {1, 2, 3, 4}
# (*[1,2,3], *[4]) # (1, 2, 3, 4)
# {**{'a': 1, 'b': 2}, **{'c': 3}}# {'a': 1, 'b': 2, 'c': 3}


# from functools import reduce
# n=input("enter n")
# factorial = reduce(lambda x, y: x*y, range(1, n+1))
# print(factorial)

# fib = lambda n : n if n <= 1 else fib(n-1) + fib(n-2)
# print(fib(10))

# from functools import wraps
# def debug(func):
#     @wraps(func)
#     def out(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return out
# @debug
# def add(x, y):
#     return x + y

# print(add(5,6))

# # unzip
# z = [(1, 2), (3, 4), (5, 6), (7, 8)] # Some output of zip() function
# unzip = lambda z: list(zip(*z))
# print(unzip(z))

def sum(*n,**kwargs):
    s = 0
    for i in n:
        s += i
    return s

print(sum(4,5,6,7,8,9))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# intersection of list1 and list2 using list comprehension
intersection_list = [x for x in list1 and list2]
print(intersection_list)

# union of list1 and list2 using list comprehension
union_list = [i for i in list1] + [i for i in list2 if i not in list1]
print(union_list)

#left join list1 and list2
left_join = [i for i in list1 if i not in list2]
print(left_join)
# fib_series = [0,1]+ [fib_series[i-1]+fib_series[i-2] for i in range(0,10)]
# print(fib_series)

# def multiplier_of_19(a):
#     def multiplier():
#         return a*19
# return multiplier

# print(multiplier_of_19(5))

# Number of Fibonacci numbers to generate
n = 10

# Generate Fibonacci numbers using list comprehension
fib_s = [0, 1]
fibonacci_series = [fib_s.append(fib_s[i-1] + fib_s[i-2]) for i in range(2, 20)]
print(fib_s)

prime = [i for i in range(2,20) if (i == 2 or i == 3) or (i % 2 and i % 3)]
print(prime)

def outer_function(outer_variable):
    def inner_function(inner_variable):
        return outer_variable * inner_variable
    return inner_function

multiplier_of_19 = outer_function(19)
result = multiplier_of_19(5) 
print(result)

from functools import wraps
def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out
@debug
def add(x, y):
    return x + y

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def concatenate(self, list):
        self.head = self.head
        current = self.head
        while current.next:
            current = current.next
        current.next = list.head

    def __mul__(self,list):
        current1 = self.head
        current2 = list.head
        count1 = 0
        count2 = 0
        while current1:
            current1 = current1.next
            count1 += 1
        while current2:
            current2 = current2.next
            count2 += 1

        if (count1 == count2):
            current1 = self.head
            current2 = list.head
            current = self.head
            while current:
                current.data = current1.data * current2.data
                current = current.next
                current1 = current1.next
                current2 = current2.next
        else:
            print("Lists mismatch")


list1 = LinkedList()
list2 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(3)
list2.append(4)
list2.append(5)
list2.append(6)
#list1.concatenate(list2)
# list1.display()
# list2.display()
list1.__mul__(list2)
list1.display()