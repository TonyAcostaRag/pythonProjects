def validation(value):
    if value.isdigit():
        if int(value) < 1 or int(value) > 25:
            print(value + " is not within the valid range")
            valid_shift_value = False
        else:
            valid_shift_value = True
    else:
        print(value + " is not a digit")
        valid_shift_value = False
    while (not valid_shift_value):

        value = input("Enter the valid shift value within the valid range of 1 and 25: ")

        if not value.isdigit():
            print(value + " is not a digit")
            continue

        if int(value) < 1 or int(value) > 25:
            print(value + " is not within the valid range")
            continue

        valid_shift_value = True
    return int(value)

def encrypt(text, shift_value):
    encoded_text = ""

    for ch in text:
        # Checking symbols.
        if not ch.isalpha():
            encoded_text += ch
            continue

        # Checking for low case
        if ch.islower():
            # Checking greater than z
            if ord(ch) + shift_value > ord('z'):
                encoded_text += chr( ord('a') + ( ord(ch) + shift_value - ord('z') - 1 ))
            else:
                encoded_text += chr(ord(ch) + shift_value)
        else:
            # Checking greater than Z
            if ord(ch) + shift_value > ord('Z'):
                encoded_text += chr(  ord('A') + (ord(ch) + shift_value - ord('Z') - 1 ))
            else:
                encoded_text += chr(ord(ch) + shift_value)

    return encoded_text

expected_encoded_text_1 = "cdezabCDEzab 123"
expected_encoded_text_2 = "Sgd chd hr bzrs"
#text_1 = input("Enter the text to encrypt: ")
text_1 = "abcxyzABCxyz 123"
#shift_value_1 = validation(input("Enter the valid shift value within the valid range of 1 and 25: "))
shift_value_1 = validation("2")
text_2 = "The die is cast"
shift_value_2 = validation("25")

print("Test case 1:")
print("shift value: ", shift_value_1)
print("text:  \t\t\t" + text_1)
print("encoded text: \t" + encrypt(text_1, shift_value_1))
print("Match with expected value: ", expected_encoded_text_1 == encrypt(text_1, shift_value_1))
print()
print("Test case 2:")
print("shift value: ", shift_value_2)
print("text:  \t\t\t" + text_2)
print("encoded text: \t" + encrypt(text_2, shift_value_2))
print("Match with expected value: ", expected_encoded_text_2 == encrypt(text_2, shift_value_2))
