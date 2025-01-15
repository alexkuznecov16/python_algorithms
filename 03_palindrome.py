# 3. Write a function to check if a given string is a palindrome (reads the same forwards and backwards).

def is_palindrome(string: str) -> bool:
  string_array = [i for i in string.lower()][::-1] # iterate each string char and reverse list
  res = ''.join(string_array) # convert list to string
  return res == string.lower()

print(is_palindrome('Mom')) # True
print(is_palindrome('Hello')) # False
print(is_palindrome('Level')) # True