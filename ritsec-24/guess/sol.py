import base64


def whatTheFunction(evilString: str):
    fornameN = base64.b64decode(evilString)
    recursiveCharArray = ""
    undecryptedencryptedString = "SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw=="
    finalrray = [ord(i) for i in undecryptedencryptedString]
    kentucky = 0
    xortrad = len(finalrray) - 1
    while xortrad > kentucky:
        glaf = finalrray[kentucky]
        finalrray[kentucky] = finalrray[xortrad]
        finalrray[xortrad] = glaf

        kentucky += 1
        xortrad -= 1

    for everyOther in range(0, len(fornameN)):
        recursiveCharArray += chr(fornameN[everyOther] - 1)

    for c in finalrray:
        undecryptedencryptedString = base64.b64encode(b"SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==").decode() + chr(c)

    return "SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==" + recursiveCharArray + undecryptedencryptedString

print(whatTheFunction("cmpkdjNjYzE6MzUuU1R8aHY0dHR6YGd2b2R1MnBvfi46MTI0M3M6amcz"))

# RS{gu3ssy_funct1on}
