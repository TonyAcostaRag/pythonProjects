
def pos(word, text):

    container = ""
    anchor_index = 0
    for i in word:

        anchor_index = text.find(i, anchor_index)
        if anchor_index == -1:
            break
        else:
            container += i

    if container == word:
        return "Yes"
    else:
        return "No"


word = ["donor", "donut", "baticu"]
text = ["Nabucodonosor", "Nabucodonosor", "redfbefrfrfaeomftdedeidedecu"]

expectedResult = ["Yes", "No", "Yes"]

for i in range(0, len(word)):
    if pos(word[i], text[i]) == expectedResult[i]:
        print("TC", i+1, " PASSED")
    else:
        print("TC", i+1, " FAILED")
