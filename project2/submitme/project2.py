import re
import random
import operator
import sys
"""
def qsort(lyst):
    if len(lyst)<2: 
        return lyst
    pivot = random.choice(lyst)
    less = [i for i in lyst if i< pivot]
    equal = [i for i in lyst if i==pivot]
    greater = [i for i in lyst if i> pivot]
    return qsort(less) + equal + qsort(greater)
"""
class Array2D(object):
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
        self.array2d=[[None for x in range(width)] for x in range(height)]
    def __iter__(self):
        iterArray=[]
        row=0
        while row<self.__height:
            col=0
            while col<self.__width:
                iterArray.append(self.array2d[row][col])
                col+=1
            row+=1
        return iter(iterArray)    
    def __str__(self):
        row=0
        retString=""
        while row<self.__height:
            col=0
            while col<self.__width:
                if col!=self.__width-1:
                    retString+=str(self.array2d[row][col])+","
                else:
                    retString+=str(self.array2d[row][col])+" "
                col+=1
            row+=1
            if row !=self.__height: retString+="\n"
        return retString
    def __eq__(self,other):
        return self.array2d == other
    def width(self):
        return self.__width
    def height(self):
        return self.__height
    def get(self,row,col):
        return self.array2d[row][col]
    def set(self,row,col,element):
        self.array2d[row][col]=element
    def row(self,row_no):
        rowlist=[]
        i=0
        while i < self.__width:
            rowlist.append(self.array2d[row_no][i])
            i+=1
        return rowlist
    def rowSwap(self,row_one,row_two,valOne,valTwo):
        #swaps row values in two equal length rows
        i=0
        for n in row_one:
            self.array2d[valOne][i],self.array2d[valTwo][i] = self.array2d[valTwo][i],self.array2d[valOne][i]
            i+=1
            
    def column(self,col_no):
        i=0
        collist=[]
        while i < self.__height:
            collist.append(self.array2d[i][col_no])
            i+=1
        return collist
    def printarray(self):
        row=0
        while row<self.__height:
            col=0
            while col<self.__width:
                #print(str(self.array2d[row][col]),end=" ")
                col+=1
            row+=1
            print("\n")

def main():
    
    fp=open(sys.argv[1],'r')
    text = fp.read()
    fp.close()
    fp=open('test.csv','r')
    keyLine = fp.readline()
    keyLine= re.sub('[^a-z\A-Z\\ \_]+', " ",keyLine)
    keyLine=list(keyLine.split())
    values=[]
    values=fp.readlines()
    
    fp.close()
    
    text= re.sub('[^a-z\A-Z\^0-9\.\ \_]+', " ",text)
    words = list(text.split())
    
    bob = Array2D(len(keyLine),int(len(words)/len(keyLine)))
    
    keyList=bob.row(0)
    
    i=0
    j=0
    k=0
    for n in range(0,int(bob.width()*bob.height())):
        if (i+1)%int(bob.width())==0:#make new lines every time line printed = value of key length
            try:
                bob.set(k,j,words[i])
            except:
                print(str(j)+" "+str(i)+"fail")
            j=0
            k+=1
            i+=1
        else:
            #disregard this.
            try:
                bob.set(k,j,words[i])
                
            except:
                print(str(j)+" "+str(i)+"fail")
            i+=1
            j+=1
    
    allRowValues=[]
    i=1
    for n in range(1,bob.height()):
        try:
            allRowValues.append(bob.row(i))
            i+=1
        except:
            print("couldn't add after value: "+str(i))
    #new=qsort(bob.column(3))
    i=0
    row=0
    new1=allRowValues
    for n in new1:
        col=0
        while col<len(new1[0]):
            bob.set(row+1,col,new1[row][col])
            col+=1
        row+=1
    
    
    fp2 = open(sys.argv[2],'r')
    dataType=[]
    for line in fp2:
        token = line
        token = token.rstrip('\n')
        token = token.split(',')
        dataIndex = keyLine.index(token[0])
        dataType.append([dataIndex,token[1],token[2]])
   
    for n in range(len(dataType)-1,-1,-1): #run check to see what type to compare. This runs in reverse to establish the dominant sorts as last.
        if dataType[n][2]=="string":
            please = dataType[n][0]
            for z in range(0,len(new1),1):
                new1[z][please]=str(new1[z][please])
        
        if dataType[n][2]=="float":
            please = dataType[n][0]
            for z in range(0,len(new1),1):
                new1[z][please]=float(eval(new1[z][please]))
        
        if dataType[n][2]=="int":
            please = dataType[n][0]
            for z in range(0,len(new1),1):
                new1[z][please]=int(new1[z][please])
                
        if dataType[n][1]=="ascend": reversal=False
        else: reversal = True
        new1= sorted(new1, key=operator.itemgetter(dataType[n][0]), reverse = reversal)
        
    row=0
    col=0
    for n in new1:
        
        col=0
        while col<len(new1[0]):
            bob.set(row+1,col,new1[row][col])
            col+=1
        row+=1
       
    
    fp3 = open(sys.argv[3],'w')
    sys.stdout=fp3
    if bob.get(1,3)==0:
        bob.set(1,3,"00000000")
    
    print(bob)
   
main()