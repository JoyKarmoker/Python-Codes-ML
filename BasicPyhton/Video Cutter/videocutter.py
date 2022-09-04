# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("video.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)
	
# # getting only first 5 seconds
# clip = clip.subclip(0, 10)

# # cutting out some part from the clip
# clip = clip.cutout(3, 7)

# showing clip
#clip.ipython_display(width = 360)
clip.write_videofile("notcroped.mp4",fps=25)

clip = clip.crop(x1=145,y1=110,x2=400,y2=810)

clip.write_videofile("croped.mp4")



