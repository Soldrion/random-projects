import math

sa = float(input("Speed A?"))
ra = float(input("Radius A?"))


sb = float(input("Speed B?"))
rb = float(input("Radius B?"))


aa = (sa*sa)/ra

ab = (sb*sb)/rb

print("acceleration 1:",aa,"acceleration 2:",ab)
print("ratio:",aa/ab)
