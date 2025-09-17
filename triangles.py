def equilateral(sides):
    a,b,c= sides
    total= (a==b and b==c and c==a) and (a+b>c and b+c>a and c+a>b)
    return total
def isosceles(sides):
    a,b,c= sides 
    total=((a==b and a!=c and b!=c) or (b==c and c!=a and b!=a) or (c==a and a!=b and c!=b) or ( a==b and b==c and c==a))and(a+b>c and b+c>a and c+a>b)
    return total
def scalene(sides):
    a,b,c= sides
    total= (a!=b and b!=c and c!= a)and(a+b>c and b+c>a and c+a>b)
    return total
