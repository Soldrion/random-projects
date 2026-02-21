import math

sa = float(input("Speed A?"))
ra = float(input("Radius A?"))
ma = float(input("Mass A?"))

sb = float(input("Speed B?"))
rb = float(input("Radius B?"))
mb = float(input("Mass B?"))

aa = (sa*sa)/ra

ab = (sb*sb)/rb


cfa = aa*ma

cfb = ab*mb


print("ratio:",cfa/cfb)



