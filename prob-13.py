revel = input().split(" ")
a, b, c = revel
x = (int(a)+int(b)+abs(int(a)-int(b)))/2
y = (int(x)+int(c)+abs(int(x)-int(c)))/2
print("%d eh o maior " % y)
