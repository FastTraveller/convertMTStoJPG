#example:python runScript.py /home/gq/Videos/output
#Author:guoqinzju@gmail.com 2013/12/21
import sys,os,re,unittest
from convertMTStoJPG import *
#convertMTStoJPG('/home/gq/Videos/BroF.MTS','/home/gq/Videos/aa/')
print sys.argv[0], sys.argv[1]
#path='/media/2Tdata/20131220'
path=sys.argv[1]
files=os.listdir(path)
for e in files:
    camPath=path+'/'+e
    #print camPath
    videofiles=os.listdir(camPath)
    for v in videofiles:
        videoPath=camPath+'/'+v
        picPath,fileExtension = os.path.splitext(videoPath)
        if(fileExtension=='.MTS'):

            if not os.path.exists(picPath):
                os.makedirs(picPath)
            convertMTStoJPG(camPath+'/'+v,picPath+'/')
