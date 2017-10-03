
def say_hello(name):
    if name:
        print 'hello,'+name+'from inside the function'
    else:
            print'no name'
print 'outside the function'

print "this is a simple string"
name = '1'
print 'my name is',name
print 'my name is '+name
first_name='zen'
middle_name='holy'
last_name='coder'
print 'my name is {} {} {}' .format(first_name, middle_name,last_name)
x='hello world'
print x.upper()
drawer = ['documents','envelopes','pens']
drawer2=['meow']
print drawer[0]
print drawer[2]
print drawer[1]
drawer.append('paper')
print drawer
drawer.pop(1)
print drawer
drawer.extend(drawer2)
print drawer
age=15
if age>=18:
    print'legal age'
else:
    print 'you are young!'