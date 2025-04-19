def fun():
    print("Function fun()")

def disp():
    print("Function disp()")

def msg():
    print("Function msg()")

functions = [fun, disp, msg]

for i in functions:
    i()