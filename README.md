# MOSDAC Video Generator
### Demo
<p align="center">
  <img src="https://raw.githubusercontent.com/Araon/MOSDAC_Video_Generator/master/demos/INSAT-3D-2.gif">
</p>

Timelapse of the two cyclones that hit the Indian peninsula in the Month of May. Made with data from INSAT-3D taken from MOSDAC.
Also, the reflection of the sun on the ocean moving from right to left is a good way to see if the day ended and keep track of time while watching the video.
This is taken in a span of 30 days with more than 550 individual images


## Usage

Month = Use abbreviation of the months i.e jan, feb
##### Sat_id  
1: L1B_STD_IR1
 
2: L1C_ASIA_MER_BIMG
##### Sameple code
```python
Python main.py <month> <sat_id>
```
The code will try to fetch all the images from that said month and compile it on a folder `./images` and after that it will generate a video from that folder and save it to `./output`

