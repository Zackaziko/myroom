#print("input your text please")
#str=input()
#str=str[::-1]
#print(str)
#b=str.encode('utf-8')

#hex=b.hex()
#str.hex()
#print(hex)
print("enter you hex bitch")
hex=input()
b2=bytes.fromhex(hex)
asci=b2.decode("ASCII")
print(asci)
asci=asci[::-1]
print(asci)
