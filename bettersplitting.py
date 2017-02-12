# 1 Gold Star
# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.
def split_string(source,splitlist):
    n=len(source)
    input_list=[]
    separators=[]
    for e in source:
        input_list.append(e)
    #print input_list   
    
    for e in splitlist:
        separators.append(e)
    #print separators  
    
    last_separator=0
    words=[]
    i=0
    while i<n:
        if (input_list[i] in separators): 
            words.append(source[last_separator:i])#0 to 3
            if i<n-1:
                i+=1#i=5
                while input_list[i] in separators:
                    if i<n:
                        i+=1
                    else:
                        break
            else:
                break
            last_separator=i#i=5
        i+=1#i=6
        if (i==n-1) and (input_list[i] not in separators):
            words.append(source[last_separator:])
    return words        
    
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
