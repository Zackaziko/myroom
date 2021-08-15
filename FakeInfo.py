import random
with open('info test/names.txt', 'r') as f:
    list = f.readlines()
    rand=random.randrange(0,len(list))
    print("Name: "+list[rand])
with open('info test/email.txt', 'r') as f2:
    list2 = f2.readlines()
    rand2=random.randrange(0,len(list))
    print("E-mail: "+list2[rand])
with open('info test/num.txt', 'r') as f3:
    list3 = f3.readlines()
    rand3=random.randrange(0,len(list))
    print("Phone number: "+list3[rand])
