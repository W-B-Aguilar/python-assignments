words = "It's thanksgiving day. It's my birthday,day!"
print words
print words.find('day')
words = words.replace('day', 'month',1)
words.replace('day', 'month')
print words
x = [2,54,-2,7,12,98]
print"minvalue elemnt: ",min(x)
print"max value element:",max(x)
x = ["hello",2,54,-2,7,12,98,"world"]
new_list=[]
print x[0],x[-1]
new_list= x[0]+x[-1]
print new_list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
y=[]
x.sort()
print x
print len(x)
y=x[:len(x)/2]
z=x[len(x)/2 -1:]
z[0]=y
print z
