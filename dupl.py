text= "abcaacc"
lst=[]
for i in range(len(text)):
    char=text[i]
    ordin= ord(char)
    lst.append(ordin)
print(lst)
for i in range(len(lst)):
    if lst[i] == lst[i-1]:
         print(lst[i])
         print(chr(lst[i]))