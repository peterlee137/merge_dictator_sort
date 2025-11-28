#import random

def mysort(a):
    arrys=[a]
    issorted=False
    while issorted==False:
        temp1=[]
        temp2=[]
        current=arrys[-1]
        temp3=float('-inf')
        for i in current:
            if i>=temp3:
                temp1.append(i)
                temp3=i
            else:
                temp2.append(i)
        arrys[-1]=temp1
        if temp2==[]:
            issorted=True
        else:
            arrys.append(temp2)
    #print(arrys)
    for i in range(len(arrys)-1,0,-1):
        L=arrys[i-1]
        l=0
        R=arrys[i]
        r=0
        temp1=[0]*(len(L)+len(R))
        while l<len(L) and r<len(R):
            if L[l]<=R[r]:
                temp1[l+r]=L[l]
                l+=1
            else:
                temp1[l+r]= R[r]
                r+=1
        if r<len(R):
            temp1[l+r:]=R[r:]
        elif l<len(L):
            temp1[l+r:]=L[l:]
        arrys[i-1]=temp1
    return arrys[0]

    

'''for i in range(100):
    arry=[random.randint(1,10) for _ in range(10)]
    print(sorted(arry)==mysort(arry))'''
