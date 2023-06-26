
def encoded_text(message):
    encoded_message = ""
    #the for loop is defined from the message entered 
    for char in message:
        #"isalpha" is used to check if all the characters in the string are letters
        if char.isalpha():
            #Character is converted to ASCII value
            ascii_value = ord(char)
            #the base offset is determined by the case of the letter 
            if char.islower():
                base_offset = ord("a")
            else:
                base_offset = ord("A")
            #the new ascii value is calculated using the cyclical offset
            n_ascii_value = base_offset + ((ascii_value - base_offset + 15)% 26)
            #the n_ascii_value is converted back to a character 
            encodd_charac = chr(n_ascii_value)
        else:
            #This preserves the non-alphabetic characters
            encodd_charac = char
        encoded_message += encodd_charac
    return encoded_message
#User inputs message to be encrypted
message = input("What is your message?: ")
encoded_message = encoded_text(message)
#the encrypted message is printed 
print("Your encoded message is:", encoded_message)
    
    