# Smallest amount 3 numbers
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
  print("a,b,c is smallest")
elif a<=b and a<=c:
  print("a is smallest")
elif b<=a and b<=c :
  print("b is smallest")
else:
   print("c is smallest")
