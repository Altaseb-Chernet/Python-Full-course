import math
def quadratic_function(a,b,c):
    discriminant=b**2 - 4*a*c
    if discriminant > 0:
        d=math.sqrt(discriminant)
        print('the solution set is two ')
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)

        print("solution x1: ",x1)
        print("solution x2: ",x2)

    elif discriminant==0:

        print('the solution is exactly only so')
        x1=-b/2*a
        print('the solution is x : ',x1)

    elif discriminant < 0:

        print('the solution is in a complex form so, ')
        real=-b/2*a
        imaginary = math.sqrt(-discriminant) / (2 * a)

        print('the real part is : ',real)
        print('the imaginary part is : ',imaginary)

number1=float(input('please enter the leading cofficent for a : '))
number2=float(input('please enter the leading cofficent for b : '))
number3=float(input('please enter the leading cofficent for c : '))
print()
quadratic_function(number1,number2,number3)
