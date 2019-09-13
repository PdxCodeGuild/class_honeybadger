# def palindrome_check():
user_input = input("Enter a word ")
if user_input == user_input[::-1]:
    print("Word is Palindrome")
else:
    print("Word is not a palindrome")
