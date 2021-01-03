#Attempt at fibonnaci function
#Fibonacci adds previous two terms to get next term
n = int(input("How many terms of the fibonacci sequence do you want?"))

def fibonacci(n):
  counter = 1
  print("Fibonacci sequence")
  #n = int(input("How many terms of the fibonacci sequence would you like to print?"))
  #Use previous line if you want user input
  a = 0
  b = 1
  l = []
  if n > 0:
    l.append(1)
    while counter<n:
      a = a + b
      l.append(a)
      counter += 1
      if counter<n:
        b = a + b
        l.append(b)
        counter += 1
    print(l)

fibonacci(n)