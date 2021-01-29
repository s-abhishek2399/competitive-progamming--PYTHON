# Enter your code here. Read input from STDIN. Print output to STDOUTimport math
import math
ab=float(input())
bc=float(input())
x=int(round(math.degrees(math.atan2(ab, bc))))
y=str(str(x)+'°')
print(y)
      
