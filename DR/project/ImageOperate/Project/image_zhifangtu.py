# coding: utf-8
"""
图像直方图化
"""
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pylab import *
j=np.arange(1,325)
FindPath="python/project/ImageOperate/prue_images/"
filenames=os.listdir(FindPath)
imlist=[]
for name in filenames:
    filePath=os.path.join(FindPath,name)
    imlist.append(filePath)
for i in j:
    outfile7 = r"python/project/ImageOperate/images/" +str(i+2268)+'.jpg'
    im3=Image.open(imlist[i - 1])
    im4=im3.resize((512,512))
    imhist, bins = histogram(np.array(im4.convert('L')).flatten(), 512, normed=True)
    cdf = imhist.cumsum()
    cdf = cdf * 255 / cdf[-1]
    im5 = interp(np.array(im4).flatten(), bins[:512], cdf)
    im6 = im5.reshape(np.array(im4).shape)
    fig = plt.figure()
    plt.axis("off")
    plt.imshow(im6)


