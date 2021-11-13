from glob import glob
import pandas as pd
import numpy as np
import ntpath
import os

trainCSV=pd.read_csv("train.csv")
train_path = 'train_images/train/'
valid_path = 'train_images/valid/'
test_path = 'train_images/test/'
###先建造train valid test的資料夾，再依序建造0-5的資料夾
if not os.path.isdir(train_path):
    os.mkdir(train_path)
if not os.path.isdir(valid_path):
    os.mkdir(valid_path)
if not os.path.isdir(test_path):
    os.mkdir(test_path)
for i in range(0,6):
    if not os.path.isdir(train_path+str(i)):
        os.mkdir(train_path+str(i))
    if not os.path.isdir(valid_path+str(i)):
        os.mkdir(valid_path+str(i))
    if not os.path.isdir(test_path+str(i)):
        os.mkdir(test_path+str(i))


all_files = glob("train_images/*.png")
print(len(all_files))
###打散
shuffles = np.random.permutation(all_files)
###8:1:1分配進三個資料夾，再根據Label分類進0-5
if len(all_files) > 0:
    test_amount= int((len(all_files)*0.1))
    valid_amount = int((len(all_files)*0.2))
    for i in range(0,test_amount):
        file=ntpath.basename(shuffles[i])
        label=trainCSV.loc[trainCSV['ID'] == file, 'Label'].iloc[0]
        newpath=shuffles[i].replace('train_images', test_path+str(label))
        os.rename(shuffles[i], newpath)
    for i in range(test_amount, valid_amount):
        file=ntpath.basename(shuffles[i])
        label=trainCSV.loc[trainCSV['ID'] == file, 'Label'].iloc[0]
        newpath=shuffles[i].replace('train_images', valid_path+str(label))
        os.rename(shuffles[i], newpath)
    for i in range(valid_amount,len(all_files)):
        file=ntpath.basename(shuffles[i])
        label=trainCSV.loc[trainCSV['ID'] == file, 'Label'].iloc[0]
        newpath=shuffles[i].replace('train_images', train_path+str(label))
        os.rename(shuffles[i], newpath)