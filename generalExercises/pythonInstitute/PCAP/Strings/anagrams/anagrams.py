
def areAnagrams(text_1, text_2):

    if len(text_1) == 0 and len(text_2) == 0:
        return "Not anagrams"

    filteredText_1 = ""
    for i in text_1.lower().split():
        filteredText_1 += i

    filteredText_2 = ""
    for i in text_2.lower().split():
        filteredText_2 += i

    if len(filteredText_1) == len(filteredText_2):
        ordered_1 = sorted(filteredText_1)
        ordered_2 = sorted(filteredText_2)

        for i in range(0, len(ordered_1)):
            if ordered_1[i] != ordered_2[i]:
                return "Not anagrams"
            if i == len(ordered_1)-1:
                return "Anagrams"
    else:
        return "Not anagrams"


text_1 = ["Listen", "modern", "sur"]
text_2 = ["Silent", "norman", "usr"]

expected_Text = ["Anagrams", "Not anagrams", "Anagrams"]

for i in range(0, len(text_1) ):
    if areAnagrams(text_1[i], text_2[i]) == expected_Text[i]:
        print("TC", i+1, " PASSED")
    else:
        print("TC", i + 1, " FAILED")
