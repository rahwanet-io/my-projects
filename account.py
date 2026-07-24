def fizzbizz(m):
 for n  in range(1, m + 1):
    if n % 3 == 0 and n % 5 == 0:
        print ("fizzbuzz")
    elif n % 3 == 0:
        print ("fizz")
    elif n % 5 == 0:
        print ("bizz")
    else:
        print (n)
print(fizzbizz(15)) 