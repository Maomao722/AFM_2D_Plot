
#%%
#==============================================================================
# Imports
#==============================================================================
from math import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns
import sys
import os
from PyQt5.QtGui import *

#Set plot parameters
sns.set(font_scale=2.0)
sns.set_style("ticks")
sns.set_palette(palette='deep')
sns.set_color_codes(palette='deep')
mpl.rcParams.update({'font.family': 'serif', 'font.serif':'DejaVu Serif'})

#Or enter the filename manually
filename ='NFC20230328_P01_S02_test02.SIG_TOPO_BKW.flt'
fileextension = '.txt'
file = 'D:/AFM_Data/Data/' + filename + fileextension

# 從檔案中讀取數據
with open(file, 'r') as file:
    ascii_data = file.readlines()

# 排除第一行的數據
ascii_data = ascii_data[1:]

# 將數據轉換為浮點數數組
Data = np.array(ascii_data, dtype=np.float32)

# 將數據重新形狀為256*256的2D數組
Data = Data.reshape(256, 256)

# 設定景深的範圍
vmin_value = np.min(Data)
vmax_value = np.max(Data)

# 繪製2D圖像
fig = plt.figure(figsize=(8, 8))  # 調整圖像尺寸
ax = fig.add_subplot(111)

# im = ax.imshow(Data, cmap='afmhot', vmin=np.min(Data), vmax=np.max(Data), extent=[0, Width, 0, Height])
im = ax.imshow(Data, cmap='afmhot', vmin=vmin_value, vmax=vmax_value, extent=[0, 5, 0, 5], origin='lower')  # X, Y座標為5um

ax.set_xlabel('Position (μm)')
ax.set_ylabel('Position (μm)')

# Add color bar (same height as figure)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.3)  # Change 'pad' to adjust separation of plot and colorbar
colorbar = fig.colorbar(im, cax=cax)
colorbar.set_label('Depth (nm)')

plt.tight_layout()

# 儲存圖像
plt.savefig('D:/AFM_Data/Plot/' + filename + '.png') #Save file with desired file extension (e.g. pdf, svg, png, tif, etc.)
plt.show()
