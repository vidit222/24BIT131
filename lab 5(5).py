lst=["manav","bhuva","jenil","vidit","ujash"]
upper=[]
for i in lst:
    upperstring=""
    for char in i:
        if "a"<=char<="z":
            upperstring+=chr(ord(char)-32)
        else:
            upperstring+=char
    upper.append(upperstring)
            
print(upper)
