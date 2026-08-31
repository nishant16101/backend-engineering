class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show()

#In this problem python uses method resolution order
# main.D-> main.B->main.C-> main.A -> class object