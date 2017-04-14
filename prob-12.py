revel = input().split(" ")
A,B,C=revel
pi=3.14159
rec=(float(A)*float(C))/2
circ=pi*(float(C)*float(C))
trapz=float(C)*(float(A)+float(B))/2
sq=float(B)*float(B)
rect=float(A)*float(B)
print(' TRIANGULO: %.3lf' %rec)
print(' CIRCULO: %.3lf' %circ)
print(' TRAPEZIO: %.3lf' %trapz)
print(' QUADRADO: %.3lf' %sq)
print(' RETANGULO: %.3lf' %rect)

