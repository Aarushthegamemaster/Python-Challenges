print("Please put a number(numerator here)")
a = int(input())
print("Please put another number(numerator here)")
b = int(input())

if a%b==0:
    print(str(a),"is divisible by", str(b))
else:
    print(str(a),"is not divisible by", str(b))