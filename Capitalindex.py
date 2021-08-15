print("enter your text")
text = str(input())
index=[]
for i in range(len(text)):
    char=text[i]
    case=char.isupper()
    if case is True:
        index.append(i)
print(index)
    