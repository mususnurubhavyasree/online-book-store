'''PATH=r"newfile.txt"
file=open(PATH,"w")
d={"key1":"val1",
   "key2":"val2",
   "key3":"val3"}
s= ""

for i in d.keys():
    file.write(i + " " +d[i] + "\n")'''

'''PATH=r"newfile.txt"
file=open(PATH,"r")

lines=file.readlines()

d={ }
for line in lines:
    s=line.strip().split()
    d[s[0]]=s[1]
    
    
print(d)
file.close()'''
#file handling
'''import os
file=r"file"
os.rmdir(file)'''

'''n=int(input("enter number"))

if n>=0:
    print("Yes!!! A non Negative Number")
else:
    raise Exception("No Negative number Allowed")'''

'''n=int(input("enter number"))

if   n<0:
    print("non negative")
else:
    print(" no negative")'''

#exception handling

'''s=[1,2,3]

try:
    s.append(4)
    print(s)
except AttributeError:
    print("tuple cant be append")
except:
    print("some error come")
else:
    print("no error has come")
finally:
    print("code has been run!!!")'''
#string formatting 
var=12345
s="we have{a}apple".format(a=var)
print(s)











































  

 
 














