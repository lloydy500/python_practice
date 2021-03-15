
def find_missing_letter(chars):
  #make an array containing all capitals A-Z
  #iterate through alphabet and get the index position of the 
  #first letter in chars call it position or p.
  #then for each letter in chars check if letter == alphabet[p]
  #if True
  #p += 1 
  #else
  #return letter 

  alphabet_in_capitals = []
  for i in range(65, 91):
    alphabet_in_capitals.append(chr(i))
  
  p = alphabet_in_capitals.index((chars[0]).upper())

  for l in chars:
    if l.upper() == alphabet_in_capitals[p]:
      p+=1
    else:
      if l == l.upper():
        return alphabet_in_capitals[p].upper()
      else:
        return alphabet_in_capitals[p].lower()

print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))