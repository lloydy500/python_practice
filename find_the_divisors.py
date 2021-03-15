def divisors(integer):
  #a is an empty array
  #iterate through all the numbers from 2..integer
  #for each num, check if the remainder of integer/num == 0
  #if true, append num to a
  #elif a is empty then print "integer is prime"

  a = []
  x = range(2, integer)
  for num in x:
    if integer % num == 0:
      a.append(num)

  if not a:
    return "{} is prime".format(integer)
  else:
    return a
    
print(divisors(15))
print(divisors(29))