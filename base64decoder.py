#Character set for the base64 language
char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

#Message which we have to decode
msg = 'R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ'

#Point to be noted: the 2 ='s at the end of the encoded message are manually removed and to mitigate it's padding effect on the program, we subtract 4 from the length of the final_bit variable (at line 20)

final_bit = ''  #Creating final bit variable which will store the string of bits

#Loop to convert each character in the encoded message to it's corresponding bit representation
for c in msg:
    bit = ''
    ind = char_set.index(c)
    for _ in range(6):  #loop run till 6 because of the character size of base64 characters
        bit += str(ind % 2)
        ind = ind // 2
    final_bit += bit[::-1]

final_bit = final_bit[:len(final_bit) - 4]  #Subtracting 4 to mitigate the padding effect of the '='s

i = 8   #Since, ASCII character size = 8 bits
while i <= len(final_bit):
    sub = final_bit[i-8:i]
    sub = sub[::-1]

    s = 0
    for j in range(8):
        k = int(j)
        s += (2**k)*int(sub[k])

    i += 8
    print(chr(s), end='')