class A:
    def __init__(self):
        print('In A')
        super().__init__()

class B:
    def __init__(self):
        print('In B')
        super().__init__()

class C(A):
    def __init__(self):
        print('In C')
        super().__init__()

class D(A):
    def __init__(self):
        print('In D')
        super().__init__()

class F(B):
    def __init__(self):
        print('In F')
        super().__init__()

class G(B):
    def __init__(self):
        print('In G')
        super().__init__()

class E(C, D):
    def __init__(self):
        print('In E')
        super().__init__()

class H(F, G):
    def __init__(self):
        print('In H')
        super().__init__()

class I(E, H):
    def __init__(self):
        print('In I')
        super().__init__()

