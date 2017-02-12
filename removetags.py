def remove_tags(code):
    n=len(code)
    print n
    
    result=[]
    word=''
    i=0
    while (i<n):
        if code[i]=='<':
            while code[i]!='>':
                i+=1
            i+=1    
        else:
            while i<n :
                if code[i]==" " and word!='' :
                    result.append(word)
                    word=''
                    i+=1
                elif code[i]=='<':
                    if word=='':
                        print "broke in if of elif"
                        break
                    result.append(word)
                    word=''
                    print "broke in elif"
                    break
                else:
                    if code[i]!=' ':
                        word=word+code[i]
                        i+=1
                    else:
                        i+=1
                    #if not i<n:
                    #    print "broke in last if"
                    #    print i
                    #    break
            if i==n and word!='':
                result.append(word)    
    return result        
print remove_tags('''A <img src='here.img' alt='nothing'>picture,</a> a cat and a mouse! ''')
#>>> ['A', 'picture,', 'a', 'cat', 'and', 'a', 'mouse!']

print remove_tags('''This <i>line</i> has <em>lots</em> of <b>tags</b>.''')
#>>> ['This', 'line', 'has', 'lots', 'of', 'tags', '.']
print remove_tags('''<h1>Title</h1><p>This is a <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print remove_tags('This sentence has no tags.')

