n = int(input().strip())
# if n is odd print "Weird"
# n is even and n >= 2 and n<=5 print "Not Weird"
# n is even and n >=6 and n <=20 print "Weird"
# if n is even and n>20 print "Not Weird"
print(n % 2)
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
