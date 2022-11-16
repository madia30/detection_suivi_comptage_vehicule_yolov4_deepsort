# import subprocess
# subprocess.run(["python C:\\Users\\faateemah\\Desktop\\yolov4\\object_tracker.py --video C:\\Users\\faateemah\\Desktop\\yolov4\\data\\video\\video5.mp4 --output C:\\Users\\faateemah\\Desktop\\yolov4\\outputs\\final3.mp4 --model yolov4 --dont_show --info"])

import subprocess
p = subprocess.Popen("python object_tracker.py --video .\\data\\video\\video1.mp4 --output .\\outputs\\video1.mp4 --model yolov4 --dont_show --info",stdin=subprocess.PIPE, shell=True )