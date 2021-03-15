input_list = range(100)

def div_by_five(num):
  if num % 5 == 0:
    return True
  else:
    return False

#generator, converted to list.
xyz = list(i for i in input_list if div_by_five(i))

input_list = range(100)

def div_by_five(num):
  if num % 5 == 0:
    return True
  else:
    return False

# generator:

xyz = [i for i in input_list if dib_by_five(i)]

