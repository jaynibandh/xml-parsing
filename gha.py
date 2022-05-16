import re
import string
from itertools import groupby
  
i=0

f=open("C:/Users/Jayanth/Documents/New folder/patent.txt", "r",encoding="utf-8")
separate=list(f.read().split(" "))

f=open("lode.txt","w",encoding="utf-8")
while i<=len(separate)+1:

    i=i+1
    if i==len(separate):
        break

    if separate[i].isupper() and separate[i+1].isupper():
          f.write("{")
          f.write(" ")
          f.write(separate[i])
          print(separate[i])
          f.write(":")
          f.write(str(i))
          f.write("}")
          f.write("'")
    if separate[i].isupper() and separate[i-1].isupper():


          f.write("{")
          f.write(" ")
          f.write(separate[i-1])
          print(separate[i-1])
          f.write(":")
          f.write(str(i-1))
          f.write("}")
          f.write("'")
          f.write("{")
          f.write(" ")
          f.write(separate[i])
          print(separate[i])
          f.write(":")
          f.write(str(i))
          f.write("}")
          f.write("'")
f.close()

f=open("lode.txt","r",encoding="utf-8")
separatoe=list(f.read().split("'"))
res = [i for n, i in enumerate(separatoe) if i not in separatoe[:n]]
re1s=(" ".join(res))
f=open("lode1.txt","w",encoding="utf-8")
f.write(re1s)
f.close()
f.close()
f=open("lode1.txt","r",encoding="utf-8")
separatoe=list(f.read().split(" "))
res = [''.join(j).strip() for sub in separatoe 
        for k, j in groupby(sub, str.isdigit)]
o=len(res)
print(o)
print (res[23])
print(res)
i=4
match = re.findall(r"\b(?![a-z]+\b)[A-Za-z]{2,}\b",str(res) ) 
print(match[5])
f=open("lode2.txt","w",encoding="utf-8")
res.insert(0,"{")
print(res[6])
print(res[9])
k=int(res[3])+1
print(k)
i=4
print("{{{{{{{{{{{{{{{{{{{{{{")

print(match)
while(i!=len(res)):
    print(i)
    print("*******")
    if i>len(res):
        break
    print(str(res[i+3]))
    print(int(res[i+3]))
    if int(res[i-1])+1==int(res[i+3]):
            #f.write(str(res[i-2]))
            print("+++++++")
            print(str(res[i-2]))
            print(res[i-1])
            f.write(" ")
    f.write(str(res[i-2]))
    if int(res[i-1])+1!=int(res[i+3]):
            f.write("\n")
    i=i+4
f.close()
f.close()



