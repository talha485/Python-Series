def is_palindrome(word):
    reversed_word = word[::-1]

    if word == reversed_word:
        print("Palindrome")
    else:
        print("Not Palindrome")


word = input("Enter word: ")
is_palindrome(word)