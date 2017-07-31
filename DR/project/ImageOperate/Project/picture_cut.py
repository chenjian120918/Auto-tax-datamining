from PIL import Image
import numpy as np
import os
j=np.arange(1,325)
FindPath=r"F:/Desktop/train7"
filenames=os.listdir(FindPath)
imlist=[]
for name in filenames:
    filePath=os.path.join(FindPath,name)
    imlist.append(filePath)
for i in j:
    outfile7 = r"F:/Desktop/train1/" +str(i+324)+'.jpg'
    im1 = Image.open(imlist[i - 1])
    im2=im1.convert('L')
    im3=im2.resize((512,512))
    im3.save(outfile7)