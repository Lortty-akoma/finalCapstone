# **CAPSTONE PROJECT II**
# This project aims at encoding a message entered using the cyclical approach ( the 15th letter after the letter used).
# **TABLE OF CONTENTS**
  CODE
  USAGE
# **CODE**
  This code is first of all defined by calling the encoded_text function in message. 'isalpha' is used to check if all the characters in the string are letters and then converted to ASCII value. 
  The base offset commonly called indexing is determined by the case of the letter. the new ASCII value is calculated; base_offset + ((ascii_value - base_offset + 15)% 26) where 15 is the encoding approach and 26 being the number of alphabets there is.
  The new ASCII value is then converted back to a string, thus the encoded message.
# **USAGE**
  You will be asked to enter your message to be encoded. Once the message has been entered, your message is encoded and the result is printed with punctuations and spaces not changing.

  [Screenshot (20)](https://github.com/Lortty-akoma/finalCapstone/assets/128003931/37cfc315-385f-4472-9d55-699c04b6b4f2)
  ![Screenshot (21)](https://github.com/Lortty-akoma/finalCapstone/assets/128003931/c840da66-5d61-4d14-ac62-9c52e0e5a7e9)
  
  # This code was created by Loretta Adjei
