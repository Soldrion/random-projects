import math

pi = math.pi

pa = float(input("Period A?"))
ra = float(input("Radius A?"))


pb = float(input("Period B?"))
rb = float(input("Radius B?"))


va = ((2*pi)*ra)/pa

vb = ((2*pi)*rb)/pb

print("speed 1:",va,"speed 2:",vb)
print("ratio:",va/vb)
