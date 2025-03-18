import random

numbers=[random.randint(1,100) for i in range(20)]
print(numbers)


a=int(input("enter a number here:"))
for i in range(len(numbers)):
    if a==numbers[i]:
        print("number is found and index is",":",i)
        break
else:
    print("not found")