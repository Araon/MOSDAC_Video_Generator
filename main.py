import requests 
import shutil 
from helper import timelist, lastMonth
import datetime
from os.path import isfile, join
import cv2
import os
import sys
# Set up the image URL and filename
# "https://mosdac.gov.in/look/3D_IMG/gallery/2021/25MAY/3DIMG_25MAY2021_0830_L1C_ASIA_MER_BIMG.jpg"
# "https://mosdac.gov.in/look/3D_IMG/gallery/%s/%s/3DIMG_%s_%s_L1B_STD_IR1.jpg"
# "https://mosdac.gov.in/look/3D_IMG/gallery/%s/%s/3DIMG_%s_%s_L1C_ASIA_MER_BIMG.jpg"

def download_images(sat_id,month):
    
    print("Downloading Image")
    template_link1 = "https://mosdac.gov.in/look/3D_IMG/gallery/%s/%s/3DIMG_%s_%s_L1B_STD_IR1.jpg"
    template_link2 = "https://mosdac.gov.in/look/3D_IMG/gallery/%s/%s/3DIMG_%s_%s_L1C_ASIA_MER_BIMG.jpg"
    if sat_id == 1:
        template_link = template_link1
    else:
        template_link = template_link2
    x = datetime.datetime.now()
    year = str(x.strftime("%Y"))
    
    for din in range(1,32):
        isthereImage = False
        day = str(din)
        timelistt = timelist()
        for i in timelistt:
            link = template_link % (year,day+month, day+month+year,i)
            try:
                r = requests.get(link, stream = True)
            except:
                print("Error fetching Image from {}".format(link))
            filename = "images/%s-%s-%s-%s.jpg" % (year,month,day,i)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image found on:%s-%s-%s-%s' % (year,month,day,i))
                isthereImage = True

        if isthereImage:
            pass
        else:
            print("No Image on %s-%s-%s" % (year,month,day))

def generate_video(pathIn,pathOut,fps):

    frame_array = []
    print("Generating Video")
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    for i in range(len(files)):
        filename=pathIn + files[i]     
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)           
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    print("Video generated: ",pathOut)

def usage():
    
    print("No values provided"+"\n"+ "Defaulting Month: {}\nSattelite: L1B_STD_IR1".format(lastMonth())+ "\n" +"Sample Command: Python main.py <month> <sat ID>" + "\n" +"sat_ID: 1(L1B_STD_IR1)" + "\n" +"sat_ID: 2(L1C_ASIA_MER_BIMG)")


def main():
    
    print("Creating Images folder")
    newpathimg = './images' 
    if not os.path.exists(newpathimg):
        os.makedirs(newpathimg)
    else:
        shutil.rmtree("./images")
    newpathvideo = './output' 
    if not os.path.exists(newpathvideo):
        os.makedirs(newpathvideo)
    try:
        month = sys.argv[1].upper()
        sat_id = sys.argv[2]
    except:
        usage()
        month = lastMonth().upper()
        sat_id = 1

    if sat_id == 1:
        fname = 'L1B_STD_IR1'+' '+month
    else:
        fname = 'L1C_ASIA_MER_BIMG'+' '+month

    print("Setting Parameter\nMonth: {}\nSattelite: {}".format(month,fname))

    download_images(sat_id,month)
    pathin = "images/"
    out = 'output/{}.avi'.format(fname)
    framepersec = 25
    if len(os.listdir('./images')) == 0:
        print("Data from {} has been archived by ISRO".format(month))
    else:    
        generate_video(pathIn=pathin,pathOut=out,fps=framepersec)
        shutil.rmtree("./images")

if __name__ == '__main__':
    main()
