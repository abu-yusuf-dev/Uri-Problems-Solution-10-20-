x=int(input())
y=int(x/365)
z=int(x%365/30)
p=int(x%365%30)
print('%i ano(s)\n%i mes(es)\n%i dia(s)'%(y,z,p))

