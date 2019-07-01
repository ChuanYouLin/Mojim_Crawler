
# coding: utf-8

# In[11]:


import pandas as pd
import os
import sys

mypath = os.getcwd()


Folder_Path = os.path.join(mypath,sys.argv[1])          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path =  os.path.join(mypath,sys.argv[2])       #拼接后要保存的文件路径
print("合併此分類下所有.csv，路徑:{}".format(Folder_Path))
print("合併結果路徑:{}".format(SaveFile_Path))
#修改当前工作目录
os.chdir(Folder_Path)
#将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()
 
#读取第一个CSV文件并包含表头
f = open(Folder_Path +'/'+ file_list[0])
df = pd.read_csv(f,encoding="utf_8_sig")   #编码默认UTF-8，若乱码自行更改
 
#将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path,encoding="utf_8_sig",index=False)
 
#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '/'+ file_list[i])
    df.to_csv(SaveFile_Path,encoding="utf_8_sig",index=False, header=False, mode='a+')

