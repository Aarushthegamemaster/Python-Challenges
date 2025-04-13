int1 = int(input("Please enter a number here:"))
int2 = int(input("Please enter another number here"))
int3 = int(input("Please enter another number here"))

avg = (int1+int2+int3)/3
print("The average is",avg)

if avg>int1 and avg>int2 and avg>int3:
    print("%d is higher than %d, %d, %d" %(avg, int1, int2, int3))
elif avg>int1 and avg>int2:
    print("%d is higher than %d and %d" %(avg, int1, int2))
elif avg>int1 and avg>int3:
    print("%d is higher than %d and %d" %(avg, int1, int3))
elif avg>int2 and avg>int3:
    print("%d is higher than %d and %d" %(avg, int2, int3))
else:
    print("Invalid Input!")


