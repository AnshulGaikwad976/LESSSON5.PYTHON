num = int(input("Enter a number ; "))

if num > 1:
    for i in range(2 , num):
        if num % i == 0:
            print(num , "is not a Prime number")
            break
    else:
        print(num , "is a primenumber.")
else:
    print(num, "is NOT a prime number")