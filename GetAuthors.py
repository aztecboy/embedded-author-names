import sys 
debug=False
if len(sys.argv)>=2:
    File=sys.argv[1]
    if len(sys.argv)==3:
        if sys.argv[2]=="-d":
            debug=True
else:
    print(sys.argv)
    print("Invalid Arguments")
    quit()

with open(File,"rb") as f:
    Data=list(f.read())

identifier=[0x41,0x52,0x4c]
i2=0

for i,obj in enumerate(Data):
    if debug:
        print(hex(obj))
    if obj==identifier[i2]:
        i2+=1
        if i2==len(identifier):
            startread=i+1
            break
    else:
        i2=0
i2=0
AuthorBytes=[]
Authors=[]
startread=i
for i in range(startread,len(Data)):
    if debug:
        print(hex(Data[i]))
    if i2==8:
        if debug:
            print("Author Found")
        for i2,dat in enumerate(AuthorBytes):
            AuthorBytes[i2]=chr(dat)
        Authors.append("".join(AuthorBytes))
        AuthorBytes=[]
        i2=0
        if Data[i]==0:
            break
        else:
            AuthorBytes.append(Data[i])
            i2+=1
    else:
        if Data[i]==0:
            
            break
        AuthorBytes.append(Data[i])
        i2+=1 


print("Authors")
if Authors==[]:
    print("No Authors found")
else:
    for i,obj in enumerate(Authors):
        print("-"+obj)

