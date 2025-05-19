def sponge_case(sentence):
    # Write your solution here!
    result = ""
    
    for index, character in enumerate(sentence):
        if index % 2 == 1:
            upper_char = character.upper()
            result += upper_char
        else:
            lower_char = character.lower()
            result += lower_char
    return result
        
# print(sponge_case("aigerim"))
# print(sponge_case("Who are YOU calling A Pinhead"))
print(sponge_case("WHAT is UP my dude"))

# # Test cases
# assert sponge_case("spongebob") == "sPoNgEbOb"
# assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
# assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
# assert sponge_case("E") == "e"
# assert sponge_case("e") == "e"

# print("All tests passed!")
# print("Discuss time and space complexity if there's time remaining")