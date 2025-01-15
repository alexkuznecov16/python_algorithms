# 10. Write a program to convert a string to title case (capitalize the first letter of each word).

def convert_case(string: str) -> str:
  array = [i.capitalize() for i in string.split()] # iterating each word capitalize it and then add to list
  return ' '.join(array)

print(convert_case('Hello to everyone!')) # Hello To Everyone!