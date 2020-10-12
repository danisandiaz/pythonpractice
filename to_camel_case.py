def to_camel_case(text):
    
    lenT= len(text)
    newText=''
    i= 1
    
    while i< lenT:
        if (text[i]== '-' or text[i]=='_' ):
            text[i]= ''
            text[i+1]=text[i+1].capitalize() 
        newText += text[i]
        return newText 
