list1 = ['magical unicorns ',19,'hello ',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']


def identify_list_type(lst):
    newString = ''
    total = 0 
    for o in lst:
        if isinstance(o,int) or isinstance(o,float):
            total += o
        elif isinstance(o,str):
            newString += o
    if newString and total:
        print " The array you entered is a mixed number"
        print "strings:", newString
        print "total:", total
    elif newString:
        print "the array you entered is os string type"
        print "String:",newString
    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total
        
print identify_list_type(list1)
print identify_list_type(list2)
print identify_list_type(list3)

