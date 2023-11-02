# Runze Cheng / 08/Oct/2023
# Breaking Caesar's Cipher
# Comment: This program applied the stats in English that 'E,T,A,D,I,N' is the most comment letters. 
# Therefore, it's more likely to give the correct answer when more words is given in a single input


def break_cipher(text):
    temp = ['0']*26
    sentence = ['']*10000000
    maxcount = 0
    maxI = 0
    for i in range(0,26):
        count = 0
        
        for c in text:
            
            temp[i] = c
            temp[i] = chr(ord(temp[i])+i)
            
            if c == ' ':                                    # if a sentence contains spaces (Although not been asked in the question)
                sentence[i] = ''.join([sentence[i],c])
            
            else:
                if ord(temp[i]) > 90:
                    temp[i] = chr(ord(temp[i]) - 26)
                
                if ord(temp[i]) == 69 or  ord(temp[i]) == 84 or ord(temp[i]) == 65 or ord(temp[i]) == 79 or ord(temp[i]) == 73 or ord(temp[i]) == 78: # the ASCII of 'E,T,A,D,I,N'
                    count += 1
                
                sentence[i] = ''.join([sentence[i],temp[i]])
                       
        if count > maxcount:
            maxcount = count
            maxI = i       
        
    print(sentence[maxI],end="")
        
text = str(input())
break_cipher(text)

# Use the letter frequency in English language and use score += score to score each txts.