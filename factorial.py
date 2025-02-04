def fact(n):
    if n >=0 :
           if n >= 1 or n==0:
                  return 1
           factorial=n*fact(n-1)
           return factorial
    else:
         return"value is negative"
                  
print(fact(0))