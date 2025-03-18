import random

numbers=[random.randint(1,30) for i in range(50)] #randint() is use for random number generate not using unique number 
print(numbers)
b=[]
b.append(set(numbers))
print(b)