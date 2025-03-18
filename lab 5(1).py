odd=[1,3,57,77,73]
even=[4,2,6,8,10]

odd[2]=even
print(odd)

flatenlst=[1,3,*even,77,73]
print(flatenlst)


flatenlst.sort()
print(flatenlst)