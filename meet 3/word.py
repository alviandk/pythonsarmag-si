kata=raw_input('input sebuah kata: ')
loop=1
batasan=input("loop kata sebanyak: ")
while loop<=batasan:
    print "{0} ke {1}".format(kata,loop)
    loop=loop+1
print ''
print "variable loop terakhir={0}".format(loop)

