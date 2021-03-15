def tower_builder(n_floors):
  #for each floor, f, in range 0..n
  #print "*" f + (f-1) times
  #add f - (f-1) spaces to each side
  #append it to the tower array
  #return the tower array
  a = []
  for f in range(1, n_floors + 1):
    a.append((((" ") * (n_floors - f)) + (("*" * f) + ("*" * (f-1)))) + ((" ") * (n_floors - f)))
  return a

print(tower_builder(7))