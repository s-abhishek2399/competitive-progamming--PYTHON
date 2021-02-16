import cmath  
a = float(input('Enter a:'))  
b = float(input('Enter b:'))  
c = float(input('Enter c:'))  

#to solve the quadratic equations the formula is 

#  (-b square root of ((b**2)-4ac))/2a
#the solution may be of either minus or plus


first_solution= (-b-cmath.sqrt((b**2)-4*a*c))/(2*a)  
second_solution = (-b+cmath.sqrt((b**2)-4*a*c))/(2*a) 
print(first_solution,second_solution)