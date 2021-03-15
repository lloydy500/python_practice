def array_diff(a, b):
  #iterate through list a
  #for each letter, check if that letter is in b
  #if true, remove letter from the list
  #return a
  new = []
  for l in a:
    if l not in b:
      new.append(l)
  return new
