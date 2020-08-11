# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:32:26 2018

@author: lovedoglion
"""
#'TTATGTTTTGAGGATGGGGCTGGLGCTTGATTTTATGTTTTGAGGATGGGGBCGTTGATTATGTTTGA'
# 判斷基因碼為3的倍數
def threeGene(x):
    nogene = ''
    #判斷3個一組的基因碼
    if len(x) >= 3: # 輸入字串的長度要大於等於3個 
        leng = len(x)  # 分隔後的字串長度
        p = leng % 3  # 除以3後的餘數
        if p == 0:  
            return x  # 印出字串
        elif p == 1: 
            return x[:leng-1] # 去掉最後1個多餘的字
        elif p == 2: 
            return x[:leng-2]  # 去掉最後2個多餘的字
        else:
            return nogene # 其他情況
    else:
        return nogene # 輸入字串長度小於3個

# 主程式開始
inputStr = input("Enter a Chromosome string: ")
atgList = inputStr.split('ATG')[1:] # 得出以ATG切分的字串陣列，[1:]是取出字串陣列的第0以後的全部
atglen = len(atgList) # 得出字串陣列個數
taa = inputStr.count('TAA')  # 找出TAA個數
tag = inputStr.count('TAG')  # 找出TAG個數
tga = inputStr.count('TGA')  # 找出TGA個數
threeEnd = taa+tag+tga
if atglen > 0 and threeEnd > 0:
    for i in range(atglen): # 逐一查看字串陣列裡的字串結尾
        if atgList[i].count('TAA') > 0: # 若出現TAA字串
            TAAList = atgList[i].split('TAA')[0] # 以TAA為分割符號，取出第0個字串
            print(threeGene(TAAList))
        if atgList[i].count('TAG') > 0:  # 若出現TAG字串
            TAGList = atgList[i].split('TAG')[0] # 以TAG為分割符號，取出第0個字串
            print(threeGene(TAGList))
        if atgList[i].count('TGA') > 0:  # 若出現TAA字串
            TGAList = atgList[i].split('TGA')[0]  # 以TGA為分割符號，取出第0個字串
            print(threeGene(TGAList))
else:
    print('no gene fund')
