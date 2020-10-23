#Raymundo Sanchez
#CSS 225
#Oct 23,2020
#Lab


#This code returns some mad libs text based on the user input
#Is the code always returnin the correct input?
#What do you think I did to write this code that I shouldn't have done?

def change_name(adjective):
    if adjective == 'red':
        return "The quick brown fox jumps over the red dog"
    elif adjective == 'lazy':
        return "The quick brown fox jumps over the lazy dog"
    elif adjective == 'energetic':
        return "The quick brown fox jumps over the energetic dog"
    elif adjective == 'happy':
        return "The quick brown fox jumps over the happy dog"
    elif adjective == 'sad':
        return "The quick brown fox jumps over the sad dog"
    else:
        return "No case for that adjective found!"
#I included a input so that it can ask the user the adjectives since it was missing that.
#the second problme that I fixed was the sentence that was repeating at the top.
user_input = input ("What is the Adjective: ")
print(change_name(user_input))
