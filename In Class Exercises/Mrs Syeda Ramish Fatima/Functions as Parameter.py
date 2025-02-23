
def funcObject():
    print('I am function object')

def func_a(x):
    print(x)
    x()

#func_a(funcObject)
s = funcObject
func_a(s)