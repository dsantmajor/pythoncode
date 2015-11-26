#looping over collections
names = ['raymond','rachel','matthew']
colors = ['red','green','blue','yellow']
for i in range(len(colors)):
    print colors[i]

# better way of writing this code in python is as below,its simple ,better and faster
for color in colors:
    print color
print "--------"


#pythons for is not the same as it is in other programing languages ,it should be named foreach,it loops over collections ,it uses the iterator protocol
for i in (0,1,2,3,4,5):
    print i**2
print "---------"

# Better way of writing it in python is ,range function ,the output of it is the list above,if you do a big range eg range(1 million) that range will be big and consume 32GB of memory, there was some thing new introduced called xrange
for i in range(6):
    print i**2
print "-------"

#looping backwards
for i in range(len(colors)-1,-1,-1):
    print colors[i]
print "-------------"

#better way of doing this is

for color in reversed(colors):
    print color
print "---better way---"

#Looping over a colloection and indices
for i in range(len(colors)):
    print i, '--->', colors[i]
print "--------"


#Better was of looping over a collection and indices is ising enumerate
for i, color in enumerate (colors):
    print i, '--->' , colors[i]
print "better way of looping over collections and indicides"
