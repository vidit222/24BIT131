import random
numbers=[random.randint(-50,50) for i in range(30)]
print(numbers)

positive=[]
negative=[]
zero=[]
for i in range(len(numbers)):
    if numbers[i]>0:
        positive.append(numbers[i])
    elif numbers[i]<0:
        negative.append(numbers[i])
    else:
        zero.append(numbers[i])
print("positive",":",positive) 
print("negative",":",negative)   
print("zero",":",zero)