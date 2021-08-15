import os
for a in range(10):
    os.makedirs("D:/Test/"+str(a))
    for b in range(10):
        os.makedirs("D:/Test/"+str(a)+"/"+str(b))
        for c in range(10):
            os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c))
            for d in range(10):
                os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d))
                for e in range(10):
                    os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d)+"/"+str(e))
                    for f in range(10):
                        os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d)+"/"+str(e)+"/"+str(f))
                        for g in range(10):
                            os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d)+"/"+str(e)+"/"+str(f)+"/"+str(g))
                            for h in range(10):
                                os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d)+"/"+str(e)+"/"+str(f)+"/"+str(g)+"/"+str(h))
                                for i in range(10):
                                    os.makedirs("D:/Test/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d)+"/"+str(e)+"/"+str(f)+"/"+str(g)+"/"+str(h)+"/"+str(i))
