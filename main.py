import requests 
import shutil 
from helper import timelist
import datetime
## Set up the image URL and filename
template_link = "https://mosdac.gov.in/look/3D_IMG/gallery/%s/%s/3DIMG_%s_%s_L1C_ASIA_MER_BIMG.jpg"

# "https://mosdac.gov.in/look/3D_IMG/gallery/2021/25MAY/3DIMG_25MAY2021_0830_L1C_ASIA_MER_BIMG.jpg"


def main():
    x = datetime.datetime.now()
    year = str(x.strftime("%Y"))
    month = "MAY"

    for din in range(1,32):
        day = str(din)
        print('====================[New day]=======================')
        print(day)
        timelistt = timelist()
        for i in timelistt:
            link = template_link % (year,day+month, day+month+year,i)
            r = requests.get(link, stream = True)
            filename = "images/%s-%s-%s.jpg" % (year,day,i)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Downloaded: ',filename)
            else:
                print('Image Couldn\'t be retreived',i)
main()

# x = datetime.datetime.now()

# year = x.strftime("%Y")
# print(year)
# month = x.strftime("%B")
# day = x.strftime("%d")

# print(day+month.upper())

