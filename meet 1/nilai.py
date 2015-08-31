score=input("enter your score : ")
if score <=100 and score >=80:
    print "A"
elif score <80 and score >=60:
    print "B"
elif score <60 and score >=40:
    print "C"
elif score <40 and score >=20:
    print "D"
elif score <20 and score >=0:
    print "E"
else:
    print "out of range"
