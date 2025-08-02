# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:18:06 2023

@author: Alihan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
calibration equation script :
    
1) save data  for ecah axis same time in .csv format(header have to be 'X,Y,Z')
2)save script and csv file same directory .. Run script
3) copy the string in calibration init. function  calibrating_init(&dev,1012,-1538,1383,-1133,1342,-1037);

qmcl.giveCalibrationEq()
"""


class Calibrate_Mag():
    def __init__(self,FileName):
        self.FileName = str(FileName)
        
      
    def read_file(self):
        
        self.df = pd.read_csv(self.FileName)
        return self.df
        
      
    def take_data(self):
        df = self.read_file()
        values =[]
        values.append( df.X.max())
        values.append( df.Y.max())
        values.append( df.Z.max())
        values.append( df.X.min())
        values.append( df.Y.min())
        values.append( df.Z.min())
        
        return_string = "(&dev" + ","+ str(int(df.X.max()))+ ","+ str(int(df.X.min()))+","+ str(int(df.Y.max()))+","+ str(int(df.Y.min()))+","+ str(int(df.Z.max()))+","+ str(int(df.Z.min()))+")"
       
        return return_string
       
    def giveCalibrationEq(self):
        val = self.take_data()
          
        return val
    
    def c_plot(self):
        
        df = self.read_file()
        Xx=np.arange(0,len(df.X))
        Yx=np.arange(0,len(df.Y))
        Zx=np.arange(0,len(df.Z))
        
        fig, ax = plt.subplots(ncols=1, nrows=1,dpi=105)
        ax.plot(Xx,df.X)
        ax.plot(Yx,df.Y)
        ax.plot(Zx,df.Z)
        ax.set_xlabel("Index")
        ax.set_ylabel("Raw Axis")
        plt.title("Raw Datas")
        plt.grid()
       
          
        

        

file_name = input("please give csv file name : ")
qmcl = Calibrate_Mag(file_name)
print(qmcl.take_data())
qmcl.c_plot()

        