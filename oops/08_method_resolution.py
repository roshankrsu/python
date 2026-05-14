class A:
    label = "A: Base Class"

class B(A): 
    label = "B: Masala blend" 

class C(A):
    label = "C: Herbal Blend"

class D(B, C):
    pass


cup = D()
print(cup.label) # will call B cause D has no label
print(D.__mro__)