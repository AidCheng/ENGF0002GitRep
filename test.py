# Runze Cheng / 08/Oct/2023
# This test encrypt the sentence using Caesar's Cipher
from random import*


def encrypt_cipher(text):
    temp = ['0']*26
    sentence = ['']*1000
    maxcount = 0
    maxI = 0
    i = randint(0,25)
    count = 0
        
    for c in text:
            
        temp[i] = c
        temp[i] = chr(ord(temp[i])+i)
        if c == ' ':
            sentence[i] = ''.join([sentence[i],c])
        else:
            if ord(temp[i]) > 90:
                temp[i] = chr(ord(temp[i]) - 26)
            if ord(temp[i]) == 69 or  ord(temp[i]) == 84 or ord(temp[i]) == 65 or ord(temp[i]) == 79 or ord(temp[i]) == 73 or ord(temp[i]) == 78:
                count += 1
            sentence[i] = ''.join([sentence[i],temp[i]])
    print (sentence[i])
        
text = str(input())
encrypt_cipher(text)
