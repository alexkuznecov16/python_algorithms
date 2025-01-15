# 4. Write a program to reverse a given string.

def string_reverse(string: str) -> str:
  # get each char from end to beginning
  return string[::-1]

print(string_reverse('Hello')) # olleH
print(string_reverse('There')) # erehT