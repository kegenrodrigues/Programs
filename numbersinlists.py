def smaller_than_specified_element(i,new_list):
    j=i
    while j!=0:
        if (new_list[i]<=new_list[i-j]):
            return True 
        else:
            j-=1
    return False
def numbers_in_lists(string):
    n=len(string)
    number=int(string)
    the_list=[]
    new_list=[]
    i=0
    while i<n:
        the_list.append(number%10)
        number=number/10
        i+=1
    i=0
    while i<n:
        new_list.append(the_list.pop())
        i+=1
    print new_list
    
    sublist=[]
    result=[] 
    i=0       
    while i<=(n-1):                                         
        if i==0:                                                            
            result.append(new_list[i])
            i+=1
        else:                                                                               
            if not smaller_than_specified_element(i,new_list):  #                                                    
                result.append(new_list[i])                                                              
                i+=1
            else:                                                                                                            
                sublist=[]                                                  
                while smaller_than_specified_element(i,new_list):
                    sublist.append(new_list[i])
                    i+=1
                    if not i<=(n-1):
                        break
                result.append(sublist)
    return result

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result

string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result

string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result

string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result
