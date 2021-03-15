def cakes(recipe, available):
  #set a counter at 0
  #calculating = True
  #while calculating is True execute this loop:
  #iterate through the recipe
    #for each (ingredient, amount) in the recipe
      #look in dictionary "available" for ingredient
      #if the ingredient's value is less than the amount needed
      #calculating = False
      #else
      #take amount from the corresponding available[ingredient]
      #add one to the counter
  #return counter    
  counter = 0
  calculating = True
  while calculating is True:
    for k, v in recipe.items():
      if k not in available:
        calculating = False
      elif available[k] < v:
        calculating = False
      elif available[k] >= v:
        new_amount = available[k] - v
        available[k] = new_amount
        continue
    counter += 1
  return counter - 1
      
        
    



recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))