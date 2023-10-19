# -*- coding: utf-8 -*-
"""
AERO4200 A3 

Shina Chen 

"""

import pandas as pd
import numpy as np 
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


"""
Q1 Strategy: Convert pqr into euler rates 

Steps: 
    1. Initial conditions
        a) Attitudes = np.array ([0], [0], [0]))
        b) 
    2. pqr vector x  conversion matrix  = euler rates 
    3. attitudes = euler rates x dt 
    4. 
    

"""

# def body_to_NED (IMU_file): 
    
#     # Step 1: Load text file and extract into vector form 
#     try:
        
#         dataframe = pd.read_csv(IMU_file)

#         # Converts columns to NumPy arrays
#         time  = dataframe['TIME'].to_numpy()
#         wbe_1 = dataframe['WBE_1'].to_numpy()
#         wbe_2 = dataframe['WBE_2'].to_numpy()
#         wbe_3 = dataframe['WBE_3'].to_numpy()
#         fsp_x = dataframe['FSP_X'].to_numpy()
#         fsp_y = dataframe['FSP_Y'].to_numpy()
#         fsp_z = dataframe['FSP_Z'].to_numpy()

#         return time, wbe_1, wbe_2, wbe_3, fsp_x, fsp_y, fsp_z
    
#     except FileNotFoundError:
#         print(f"File '{IMU_file}' is not found.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
        

def body_to_NED (IMU_file): 
    
    # Step 1: Load text file and extract into vector form 
    try:
        
        dataframe = pd.read_csv(IMU_file)

        # Converts columns to NumPy arrays
        time  = dataframe['TIME'].to_numpy()
        wbe_1 = dataframe['WBE_1'].to_numpy()
        wbe_2 = dataframe['WBE_2'].to_numpy()
        wbe_3 = dataframe['WBE_3'].to_numpy()
        fsp_x = dataframe['FSP_X'].to_numpy()
        fsp_y = dataframe['FSP_Y'].to_numpy()
        fsp_z = dataframe['FSP_Z'].to_numpy()

        return time, wbe_1, wbe_2, wbe_3, fsp_x, fsp_y, fsp_z
    
    except FileNotFoundError:
        print(f"File '{IMU_file}' is not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    #Step 2 
    
    


# time, wbe_1, wbe_2, wbe_3, fsp_x, fsp_y, fsp_z = load_text_file(file_name)

time,wbe_1,wbe_2,wbe_3, fsp_x,fsp_y,fsp_z= body_to_NED('IMU_M1H.txt')
