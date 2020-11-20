'''
Name: Yatharth Taneja
Roll Number: 2019346
CSE 112 
Cache Endsemester Project
16 bit machine cache 


 '''

import math
import copy
# helper functions
def Log2(x): 
    if x == 0: 
        return False; 
  
    return (math.log10(x) / 
            math.log10(2)); 
def To_Decimal(n): 
    return int(n,2) 

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == 
            math.floor(Log2(n))); 

def to_binary(s,di):
    x=int(s)
    sum=0
    exp=1
    while(x>0):
        digit=x%2
        x=x//2
        # arr.append(digit)
        sum+=digit*exp
        exp*=10
    sum='0'*(di-len(str(sum)))+str(sum)
    # print("sum  "+ str(digit))
    return sum
# declaring cache memory
cache=[] #level2
cache2=[] 
"""level 1"""
def readDir2(addr,memoryindex,Cindex,Tagindex):
    global cache 
    global cache2
    addr2=addr
    cacheindex=(addr[Tagindex:Cindex+Tagindex])

    cacheindex=To_Decimal(cacheindex)

    tagdata=addr[0:Tagindex]
    # print(tagdata)
    if(cache2[cacheindex][0:Tagindex]==tagdata):
        print("HIT")
    else:
        # print("MISS")
        # print("adding to cache")
        readDir(addr,memoryindex,Cindex+1,memoryindex-Cindex-1)
        writeDir2(addr,memoryindex,Cindex,Tagindex)
def readDir(addr,memoryindex,Cindex,Tagindex):
    global cache 
    addr2=addr
    cacheindex=(addr[Tagindex:Cindex+Tagindex])

    cacheindex=To_Decimal(cacheindex)

    tagdata=addr[0:Tagindex]
    # print(tagdata)
    if(cache[cacheindex][0:Tagindex]==tagdata):
        print("HIT")
    else:
        print("MISS")
        print("adding to cache")
        writeDir(addr,memoryindex,Cindex,Tagindex)
    # print(cache)
    
def writeDir2(addr,memoryindex,Cindex,Tagindex):
    global cache 
    global cache2
    addr2=addr
    flag=0
    cacheindex=(addr[Tagindex:Cindex+Tagindex])
    cacheindex=To_Decimal(cacheindex)
    tagdata=addr[0:Tagindex]
    # print(tagdata)
    if(cache2[cacheindex][0:Tagindex]==tagdata):
        print("ALREADY IN CACHE")
        flag=1
    if flag==0:
        print("Removing "+str(cache2[cacheindex])+" from L1 cache")
        cache2[cacheindex]=addr[0:Cindex+Tagindex]
   
def writeDir(addr,memoryindex,Cindex,Tagindex):
    global cache 
    addr2=addr
    flag=0
    cacheindex=(addr[Tagindex:Cindex+Tagindex])
    cacheindex=To_Decimal(cacheindex)
    tagdata=addr[0:Tagindex]
    # print(tagdata)
    if(cache[cacheindex][0:Tagindex]==tagdata):
        print("ALREADY IN CACHE")
        flag=1
    if flag==0:
        print("Removing "+str(cache[cacheindex])+" from L2 cache")
        cache[cacheindex]=addr[0:Cindex+Tagindex]

def directMapping(n,c,b,cl,nl,Tagindex,Cindex):
    global cache
    global cache2
    memoryindex=int(Log2(nl))
    for i in range(cl):
        cache.append('-')
    for i in range(int(cl/2)):
        cache2.append("-")
    inp=True
    while(inp):
        inp2=input(" ENTER READ/ WRITE or exit \n")
        # if(inp2=="READ ")
        if(inp2=='exit'):
            inp=False
            break
        inp3= inp2.split(" ")
        if(len(inp3[1])!=memoryindex+int(Log2(b)) ):
            print("ERROR adress size wrong must be "+str(memoryindex+int(Log2(b))))
            break
        # cacheindex=inp3[1][Tagindex:Cindex]
        if(inp3[0]=="read"):
            readDir2(inp3[1],memoryindex,Cindex-1,memoryindex+1-Cindex)
        elif(inp3[0]=="write"):
            readDir2(inp3[1],memoryindex,Cindex-1,memoryindex+1-Cindex)
        else:
            print("Syntax Error")
        print("L1 CACHE")
        print(cache2)
        print("L2 CACHE")
        print(cache)     
"""direct mapping ends here """
# directMapping(1,1,8,8,64,2,4)
# associative mapping
def readAss2(addr,memoryindex):
    global cache
    global cache2
    flag=0
    addr2=addr
    addr=addr[0:memoryindex]
    if addr in cache2:
        flag=1
        print("HIT"  )

    if flag==0:
        # print("MISS")
        # print("adding to cache")
        writeAss2(addr)
        readAss(addr2,memoryindex)


def readAss(addr,memoryindex):
    global cache
    flag=0
    addr2=addr
    addr=addr[0:memoryindex]
    if addr in cache:
        flag=1
        print("HIT"  )

    if flag==0:
        print("MISS")
        print("adding to cache")
        writeAss(addr)

def writeAss2(addr):
    global cache
    global cache2
    flag=0
    for i in range(len(cache2)):
        if cache2[i]==addr:
            print("Already in cache")
            flag=2
            break
    if flag==0:
        for i in range(len(cache2)):
            if cache2[i]=="-":

                flag=1
                cache2[i]=addr
                # print loctaion where writting
                break
    if flag==0:
        print("REMOVING " + cache2[0]+" from L1 cache")
        for i in range(1,len(cache2)):
            
            cache2[i-1]=cache2[i]
        cache2[len(cache2)-1]=addr

def writeAss(addr):
    global cache
    flag=0
    for i in range(len(cache)):
        if cache[i]==addr:
            print("Already in cache")
            flag=2
            break
    if flag==0:
        for i in range(len(cache)):
            if cache[i]=="-":

                flag=1
                cache[i]=addr
                # print loctaion where writting
                break
    if flag==0:
        print("REMOVING " + cache[0]+" from L2 cache")
        for i in range(1,len(cache)):
            
            cache[i-1]=cache[i]
        cache[len(cache)-1]=addr
    # return cache 

def AssociativeMaping(n,c,b,cl,nl,Tagindex):
    global cache
    global cache2
    memoryindex=int(Log2(nl))
    for i in range(cl):
        cache.append('-')
    for i in range(int(cl/2)):
        cache2.append("-")
    inp=True
    while(inp):
        inp2=input(" ENTER READ/ WRITE or exit \n")
        # if(inp2=="READ ")
        if(inp2=='exit'):
            inp=False
            break
        inp3= inp2.split(" ")
        if(len(inp3[1])!=memoryindex+int(Log2(b)) ):
            print("ERROR adress size wrong must be "+str(memoryindex+int(Log2(b))))
            break
        # print(inp3[1])
        if(inp3[0]=="read"):
            readAss2(inp3[1],memoryindex)
        elif(inp3[0]=="write"):
            readAss2(inp3[1],memoryindex)
            # probable errorr here
        else:
            print("Syntax Error")
        print("L1 CACHE")
        print(cache2)
        print("L2 CACHE")
        print(cache)   
# AssociativeMaping(1,1,8,8,32,int(Log2(32/8)))
# print(cache)

""" ASSOCIATIVE MAPPING ENDS HERE """
def readNass2(addr,memoryindex,Kindex,Tagindex,k):
    global cache
    global cache2
    addr2=addr
    # print("tagindex")
    # print(Tagindex)
    # print("memory")
    # print(memoryindex)
    cacheindex=(addr[Tagindex:memoryindex])
    # print(cacheindex)
    cacheindex=To_Decimal(cacheindex)
    tagdata=addr[0:Tagindex]
    flag=0
    addr=addr[0:memoryindex]
    if addr in cache2[cacheindex]:
        flag=1
        print("HIT")

    if flag==0:
        # print("MISS ")
        # print("adding to cache")
        writeNass2(addr,memoryindex,Kindex,Tagindex,k)
        readNass(addr2,memoryindex,Kindex+1,Tagindex-1,k)
def readNass(addr,memoryindex,Kindex,Tagindex,k):
    global cache
    addr2=addr
    # print("tagindex 2")
    # print(Tagindex)
    # print("memory 2")
    # print(memoryindex)
    cacheindex=(addr[Tagindex:memoryindex])
    # print(cacheindex)
    cacheindex=To_Decimal(cacheindex)
    tagdata=addr[0:Tagindex]
    flag=0
    addr=addr[0:memoryindex]
    if addr in cache[cacheindex]:
        flag=1
        print("HIT")

    if flag==0:
        print("MISS ")
        print("adding to cache")
        writeNass(addr,memoryindex,Kindex,Tagindex,k)
    
def writeNass2(addr,memoryindex,Kindex,Tagindex,k):
    global cache
    global cache2
    flag=0
    cacheindex=(addr[Tagindex:memoryindex])
    # print(cacheindex)
    cacheindex=To_Decimal(cacheindex)
    tagdata=addr[0:Tagindex]
    for i in range(len(cache2[cacheindex])):
        if cache2[cacheindex][i]==addr[:memoryindex]:
            print("Already in cache")
            flag=2
            break
    if flag==0:
        for i in range(len(cache2[cacheindex])):
            if cache2[cacheindex][i]=="-":

                flag=1
                cache2[cacheindex][i]=addr[0:memoryindex]
                # print loctaion where writting
                break
    if flag==0:
        print("REMOVING " + cache2[cacheindex][0]+" from L1 cache")
        for i in range(1,len(cache2[cacheindex])):
            
            cache2[cacheindex][i-1]=cache2[cacheindex][i]
        cache2[cacheindex][len(cache2[cacheindex])-1]=addr[0:memoryindex]
def writeNass(addr,memoryindex,Kindex,Tagindex,k):
    global cache
    flag=0
    cacheindex=(addr[Tagindex:memoryindex])
    # print(cacheindex)
    cacheindex=To_Decimal(cacheindex)
    tagdata=addr[0:Tagindex]
    for i in range(len(cache[cacheindex])):
        if cache[cacheindex][i]==addr[:memoryindex]:
            print("Already in cache")
            flag=2
            break
    if flag==0:
        for i in range(len(cache[cacheindex])):
            if cache[cacheindex][i]=="-":

                flag=1
                cache[cacheindex][i]=addr[0:memoryindex]
                # print loctaion where writting
                break
    if flag==0:
        print("REMOVING " + cache[cacheindex][0]+" from L2 cache")
        for i in range(1,len(cache[cacheindex])):
            
            cache[cacheindex][i-1]=cache[cacheindex][i]
        cache[cacheindex][len(cache[cacheindex])-1]=addr[0:memoryindex]

def Nassociative(n,c,b,cl,nl,Tagindex,Cindex,k):
    global cache
    global cache2
    temp=[]
    for i in range(k):
        temp.append("-")
    memoryindex=int(Log2(nl))
    for i in range(int(cl/k)):
        temp2=copy.deepcopy(temp)
        cache.append(temp2)
    for i in range(int(cl/(2*k))):
        temp2=copy.deepcopy(temp)
        cache2.append(temp2)
    inp=True
    # cache[0][1]="11100"
    while(inp):
        inp2=input(" ENTER READ/ WRITE or exit \n")
        # if(inp2=="READ ")
        if(inp2=='exit'):
            inp=False
            break
        inp3= inp2.split(" ")
        if(len(inp3[1])!=memoryindex+int(Log2(b)) ):
            print("ERROR adress size wrong must be "+str(memoryindex+int(Log2(b))))
            break
        # cacheindex=inp3[1][Tagindex:Cindex]
        if(inp3[0]=="read"):
            # readNass2(inp3[1],memoryindex,int(cl/(2*k)),memoryindex-int(cl/(2*k)),k)
            readNass2(inp3[1],memoryindex,int(cl/(2*k)),memoryindex-(int(Cindex-1)- int(Log2(k))),k)

        elif(inp3[0]=="write"):
            readNass2(inp3[1],memoryindex,int(cl/(2*k)),memoryindex-(int(Cindex-1)- int(Log2(k))),k)
            # readNass2(inp3[1],memoryindex,int(cl/(2*k)),memoryindex-int(cl/(2*k)),k)
            # writeNass(inp3[1],memoryindex,int(cl/k),Tagindex,k)
        else:
            print("Syntax Error")
        # print(cache)'
        print("L1 CACHE")
        print(cache2)
        print("L2 CACHE")
        print(cache)   
 

def main():
    # N= int (input(" input Size of main memory (Should be power of 2): " ))
    # if(not isPowerOfTwo(N)):
    #     print("ERROR: Input "+ str(N) + " is not in power of 2")
    #     exit
    N=2**16  #16 bit machine
    C= int (input(" input Size of Cache memory (Should be power of 2): " ))
    if(C>N):
        print("ERROR Main memory cannot be smaller than Cache memory")
        exit()
    if(not isPowerOfTwo(C)):
        print("ERROR: Input "+ str(C) + " is not in power of 2")
        exit()
    
    B= int (input(" input Size Block Size (Should be power of 2): " ))
    if(not isPowerOfTwo(B)):
        print("ERROR: Input "+ str(B) + " is not in power of 2")
        exit()
    Cl=int(C/B)
    Nl=int(N/B)
    Cindex=int(Log2(Cl))
    Mindex=int(Log2(Nl))
    Tagindex=Mindex-Cindex
    # print(Log2(Cl))
    if(Cl<=1):
        print("ERROR : Block size too big or small Cache memory")
        exit()
    if(Cl>Nl or C>N):
        print("ERROR Main memory cannot be smaller than Cache memory")
        exit()
    
    # handle error if block is bigger or if cahce is bigger than mainn memory
    choice=int(input(" WHAT type of cache memory you want \n press 1 for direct mapping \n press 2 for Associative \n press 3 for n-set Associative \n choice: "))
    print("address should be " +str(Mindex+int(Log2(B))))
    if(choice==1):
        directMapping(N,C,B,Cl,Nl,Tagindex,Cindex)
    elif(choice==2):
        AssociativeMaping(N,C,B,Cl,Nl,Tagindex)
    elif(choice==3):
        k=int(input("input N : "))
        if(not isPowerOfTwo(k)):
            print("ERROR: Input "+ str(B) + " is not in power of 2")
            exit()
        Nassociative(N,C,B,Cl,Nl,Tagindex,Cindex,k)
    else:
        print("Invalid input ")
        exit()


if __name__ == "__main__":
    main()