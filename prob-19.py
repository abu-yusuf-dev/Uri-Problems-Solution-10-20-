x=int(input())
y=int(x/3600)
z=int(x%3600/60)
p=int(x%60)
print('%i:%i:%i'%(y,z,p))

