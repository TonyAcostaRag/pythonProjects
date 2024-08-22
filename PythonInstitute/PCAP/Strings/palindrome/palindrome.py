
def isPalindrome(text):
    palindrome = False
    if len(text) == 0:
        return palindrome

    text_no_spaces = ""
    for i in text.lower().split():
        text_no_spaces += i

    for ch in range(0, len(text_no_spaces)):
        if not text_no_spaces[ch] == text_no_spaces[-1-ch]:
            return palindrome
        else:
            if ch == len(text_no_spaces) - 1:
                palindrome = True
            continue

    return palindrome

#text = input("Enter the text to determine if is a palindrome: ")
text_1 = "Ten animals I slam in a net"
text_2 = "Eleven animals I slam in a net"
text_3 = "Anita lava la tina"

if isPalindrome(text_1):
    print(text_1, "It's a palindrome", sep="\t\t->\t")
else:
    print(text_1, "It's not a palindrome", sep="\t->\t")

if isPalindrome(text_2):
    print(text_2, "It's a palindrome", sep="\t->\t")
else:
    print(text_2, "It's not a palindrome", sep="\t->\t")

if isPalindrome(text_3):
    print(text_3, "It's a palindrome", sep="\t->\t")
else:
    print(text_3, "It's not a palindrome", sep="\t->\t")


