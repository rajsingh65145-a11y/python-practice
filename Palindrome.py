def is_palindrome(s):
    return s == s[::-1]

s=input("enter a string:")

if is_palindrome(s):
    print("This string is a palindrome")

else:
    print("this string is not a palindrome")    