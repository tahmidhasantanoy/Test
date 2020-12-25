n = int(input("Enter the car cover distance in a day: "))
m = int(input("Enter total distance: "))

p = m // n
q = m % n
#x = q / q
if(q == 0):
    print(p)
else:
    print(p+1)

#print(p+x)