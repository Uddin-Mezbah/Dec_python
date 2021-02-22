#def function1():
#    print("subscribe now")

#func2 = function1()
#del function1
#func2

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = funcret(1)
print(a)

def dec1(func1):
    def nowexec():
        print("Excuting now")
    return nowexec()
@dec1
def who_is_harry():
    print("davide is a good boy")

who_is_harry()