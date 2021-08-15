print("enter your text")
text=str(input())
val=float(((len(text)+1)/2)-1)
chk=val.is_integer()
if chk is True:
    mid=int(((len(text)+1)/2)-1)
    print(text[mid])
else: 
    mid=int(((len(text)+1)/2)-1)
    print(text[mid:mid+2])