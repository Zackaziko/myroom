try:

    print("1 for encrypt, 2 for decrypt")
    mode = input()
    if mode != "1" and mode != "2":
        print("kosmak")
    if mode == "1":
        print("enter your text")
        text=input()
        print("enter your shift")
        shift=int(input())
        lst=[]
        for i in range(len(text)):
                char = text[i]
                ordin = ord(char)
                ordin = ordin + shift
                ch=chr(ordin)
                lst.append(ch)
        plchldr = "" 
        finl=plchldr.join(lst)
        print(finl)
    if mode =="2":
        print("enter your text")
        text=input()
        print("enter your shift")
        shift=int(input())
        lst=[]
        for i in range(len(text)):
                char = text[i]
                ordin = ord(char)
                ordin = ordin - shift
                ch=chr(ordin)
                lst.append(ch)
        plchldr = "" 
        finl=plchldr.join(lst)
        print(finl)
    
except:
    print('Teezak 7amra')
        