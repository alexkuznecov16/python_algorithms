# 8. Write a program to find the largest element in a nested array.

def find_max(array: list) -> float:
  res = array[0][0] # initial result
  
  for i in array:
    for x in i:
      if x > res:
        res = x
        
  return res

print(find_max([[1,2,3], [7,8,9], [4,5,6]]))