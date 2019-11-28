# INSPECTOR LEKAS
# 2ND DEGREE EQUATION
print("The equation has the form aX^2+bX+c=0")
var1=float(input("give the a="))
var2=float(input("give the b="))
var3=float(input("give the c="))
if var1==0 :
    X=-var3/var2
    print(f"the solution is X={X}")
D=var2**2-4*var1*var3
if D==0 :
    X=-var2/(2*var1)
    print(X)
if D>0 :
    x1=(-var2+(D**0.5))/(2*var1)
    x2=(-var2-(D**0.5))/(2*var1)
    print(x1)
    print(x2)
if D<0 :
    print("D<0")    




