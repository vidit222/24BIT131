f=[450,425,400,150,32]
celcius=[]

for i in range(len(f)):
    c=(f[i]-32)*9/5
    celcius.append(c)
    
print(celcius)