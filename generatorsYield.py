#for example we have to print numbers from 1 to 200,normally
# a generator is a function that behaves like an iterator , it produces oonly 1 value at a time when we call it not all value at once.
# it uses yield keyword instead of return
'''
yield is used to pause a func and return some value , but it remembers its state starts from where it stop last
'''
def creater():
    list=[]
    i=1
    while i<=200:
        list.append(i)
        i+=1
    return list
print(creater())
# also if we use a range function
numbers=list(range(1,201))
print(numbers)
# now we need to find the size of list in first code so
import sys
def creater():
    list=[]
    i=1
    while i<=200:
        list.append(i)
        i+=1
    return list
print(creater())
z=sys.getsizeof(list)
print(z)# it takes 432 bytes in memory
# if we have to add 10 in this list in each nu,then
print([num+10 for num in creater()])
    #istrah zada memory use ho rhi h kue k phely 200 nums generate huwy
#h phir us ma addition huwi h isa acha h k hum sath sath generate kery aik num or us ma add kery phir take mem zada use na ho

#use generator yield function
def creater1():
    i=1
    while i<=200:
        yield i
        i+=1
print(creater1())
x=creater1()
print(next(x))
# aik sath nhi balkey bari bari generate kery ga nums ko sirf jab hum call kery ga.
# jesy jab 1 print huwa to ya stop hojye ga phir hum call kery ga to next num hoga.
print(next(x))
print(next(x))
#for full show
print(list(x))

#EXAMPLES
#1
def get_numbers():
    for i in range(1,6):
        yield i
print(get_numbers())
x=get_numbers()
print(next(x))
print(next(x))
print(list(x))
#2
def square():
    for i in range(1,4):
        yield i*i
print(square())
x=square()
print(next(x))
#3
def even():
    for i in range(1,11):
        if i%2==0:
            yield i
print(even())
x=even()
print(next(x))
#4 infinite iterator
def infinite():
    i=1
    while True:
        yield i
        i+=1
print(infinite())
x=infinite()
print(next(x))