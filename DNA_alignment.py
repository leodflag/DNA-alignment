# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:32:26 2018

@author: lovedoglion
"""
#'TTATGTTTTGAGGATGGGGCTGGLGCTTGATTTTATGTTTTGAGGATGGGGBCGTTGATTATGTTTGA'

def threeGene(x):
    nogene=''
    #判斷3個一組的基因碼
    if len(x)>=3:
        leng=len(x)  #分隔後的字串長度
        p=leng%3    #分隔後的字串長度%3
        if p==0:     #字串長度%3=0
            return x    #印出字串
            #genelist.append(x)
        elif p==1:   #字串長度%3=0
            return x[:leng-1]
            #genelist.append(x[:leng-1])
        elif p==2:   #字串長度%3=0
            return x[:leng-2]#ATG分隔後的字串
           # genelist.append(x[:leng-2])
        else:
            #genelist.append('') 
            return nogene
    else:
        return nogene
    #return genelist        
        

inputStr = input("Enter a Chromosome string: ")
atgList=inputStr.split('ATG')[1:]
#print(atgList)
atglen=len(atgList)
#tga=inputStr.find('TGA')
taa=inputStr.find('TAA')#找出TAA個數
tag=inputStr.find('TAG')#找出TAG個數
tga=inputStr.find('TGA')#找出TGA個數
threeEnd=taa+tag+tga
if atglen>0 and threeEnd>0:
    for i in range(atglen):
        if atgList[i].find('TAA')>0:
            TAAList=atgList[i].split('TAA')[0]
            print(threeGene(TAAList))
        if atgList[i].find('TAG')>0:
            TAGList=atgList[i].split('TAG')[0]
            print(threeGene(TAGList))
        if atgList[i].find('TGA')>0:
            TGAList=atgList[i].split('TGA')[0]
            print(threeGene(TGAList))    
else:
    print('no gene fund')               
