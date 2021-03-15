def sort_array(source_array):
    #iterate through the list
    #make a sorted_array,  of all the odd numbers sorted 
    #iterate through source_array again
    #check if each number is odd
    #if true, set the num equal to the first num in sorted array
    #pop the first number from the sorted array
    #return source array

  sorted_array = sorted([num for num in source_array if num % 2 != 0])
  for i, value in enumerate(source_array):
    if value % 2 != 0:
      source_array[i] = sorted_array[0]
      sorted_array.pop(0)
  return source_array
      
print(sort_array([5, 8, 6, 3, 4]))
