from math import sqrt
xA = int(input())
yA = int(input())
xB = int(input())
yB = int(input())
xC = int(input())
yC = int(input())
distAB = sqrt(((xA-xB)**2)+((yA-yB)**2))
distBC = sqrt(((xC-xB)**2)+((yC-yB)**2))
distCA = sqrt(((xA-xC)**2)+((yA-yC)**2))
print("""A-B: {:.2f}
B-C: {:.2f}
C-A: {:.2f}""".format(distAB, distBC, distCA))