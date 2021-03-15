def is_valid_walk(n):
  #make a counter for north and south
  #where north is +1 and south is -1 per unit
  #make a counter for east and west
  #where east is +1 and west is -1 per unit
  #only if both counters are 0 and length of n == 10 should is_valid_walk return true

  lat_counter = 0
  lon_counter = 0

  for l in n:
    if l == 'n':
      lat_counter += 1
    elif l == 's':
      lat_counter -= 1
    elif l == 'e':
      lon_counter += 1
    elif l == 'w':
      lon_counter -= 1
    print("lat_counter: "+ str(lat_counter))
    print("lon_counter: "+ str(lon_counter))
  if lat_counter == 0 and lon_counter == 0 and len(n) == 10:
    return True
  else:
    return False

print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))