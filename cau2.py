import math
x1=int(input("nhap x1: "))
y1=int(input("nhap y1: "))
x2=int(input("nhap x2: "))
y2=int(input("nhap y2: "))
d1=(x2-x1)*(x2-x1)
d2=(y2-y1)*(y2-y1)
res=math.sqrt(d1+d2)
print("kcach giua 2 diem la: ",res)

