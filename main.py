import math
class Kalkulacka:
    def sucetfunc(self, a, b):
        sucet = a+b
        return sucet

    def sucinfunc(self, a, b):
        sucin = a*b
        return sucin


    def deleniefunc(self, a, b):
        delenie = a/b
        return delenie

    def preponafunc(self, a, b):
        prepona = math.sqrt(a**2 + b**2)
        return prepona


    def quadratic_roots(self, a, b, c):
    # Calculate the discriminant
        discriminant = b ** 2 - 4 * a * c
        return discriminant

    # Check if a is zero to avoid division by zero
        if a == 0:
            return "The coefficient 'a' cannot be zero in a quadratic equation."

    # Case 1: Two distinct real roots
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return (root1, root2)

kalkulacka = Kalkulacka()

# Printing the results
print(f"Sucet: {kalkulacka.sucetfunc(5,3)}")
print(f"Sucin: {kalkulacka.sucinfunc(5,3)}")
print(f"Delenie: {kalkulacka.deleniefunc(10,2)}")
print(f"Prepona: {kalkulacka.preponafunc(3,4)}")
print(f"Quadratic: {kalkulacka.quadratic_roots(1,-3,2)}")