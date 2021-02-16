a = float(input('Enter first side:'))  
b = float(input('Enter second side:'))  
c = float(input('Enter third side:'))  

#to calculate the area of a trainle we have to calculate the semi perimeter

semi_perimeter= (a+b+c)/2


#formula is20


area=((semi_perimeter*(semi_perimeter-a)*(semi_perimeter-b)*(semi_perimeter-c))) **0.5
print(area)