from moviepy.editor import *


# loading video gfg
clip = VideoFileClip("edited.mp4")

# getting frame rate of the clip
rate = clip.fps
  
# printing the fps
print("FPS : " + str(rate))