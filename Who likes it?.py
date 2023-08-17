def likes(names):
    
    # it was a simple code 
    # used only conditional statements if, elif and else
    
    draken = ""
    
    if len(names) == 0:
        draken = "no one likes this"
        
    elif len(names) == 1:
        draken = names[0] + " likes this"
        
    elif len(names) == 2:
        draken = names[0] + " and " + names[1] + " like this"
        
    elif len(names) == 3:
        draken = names[0] + ", " + names[1] + " and " + names[2] + " like this"
        
    else:
        draken = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
        
    return draken
