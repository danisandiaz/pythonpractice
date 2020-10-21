def namelist(names):
    
    namestr = ""
    if (len(names)) < 1:
        namestr = ""
    
    elif (len(names)) > 1:
        i=0                
        while i < (len(names)-1):              
            if (len(namestr) > 0):
                namestr += ", "
            namestr += str(names[i]['name'])  
            i = i + 1
        namestr += " & "
        namestr += str(names[-1]['name']) 
        
    else:
        namestr = str(names[0]['name'])
        
    return namestr   
    
