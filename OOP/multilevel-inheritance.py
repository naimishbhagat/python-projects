class A:
    def method_a(self):
        print('Method of class A')

class B(A):
    def method_b(self):
        print('Method of class B')

class C(B):
    def method_c(self):
        print('Method of class C')

c = C()
c.method_a()
c.method_b()
c.method_c()