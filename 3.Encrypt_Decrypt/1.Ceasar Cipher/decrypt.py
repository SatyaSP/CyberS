def decrypt(cipher,s):
    result = ""
 
    # traverse text
    for i in range(len(cipher)):
        char = cipher[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result
 
#check the above function
cipher = input("Enter cipher (alphabets only) : ")
s = int(input("Enter shift (1-26) : "))
print ("Cipher  : " + cipher)
print ("Shift : " + str(s))
print ("Original Text: " + decrypt(cipher,s))