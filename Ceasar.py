def encode(string, k):
    encoded_str = ""
    for each in string:
        if (65 <= ord(each) <= 90):
            encoded_char = ord(each) + k
            if encoded_char > 90:
                encoded_char = 65 + (encoded_char - 90 -1)
            encoded_str += chr(encoded_char)
        if (97 <= ord(each) <= 122):
            encoded_char = ord(each) + k
            if encoded_char > 122:
                encoded_char = 97 + (encoded_char - 122 -1)
            encoded_str += chr(encoded_char)
    return encoded_str

#main function
s = input()
encoded_str = encode(s, 1)
print(encoded_str)
