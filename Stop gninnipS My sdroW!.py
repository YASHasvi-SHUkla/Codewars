def spin_words(sentence):
    # Your code goes here
    
    s = ""
    
    for x in list(sentence.split(" ")): # spliting the string at spaces and storing into list
        if len(x) >= 5:
            s = s + x[::-1]
        else:
            s = s + x
            
        s = s + " "
        
    return s[:-1]
    
