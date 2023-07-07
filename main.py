import cv2

# configurable parameters
source = "4.jpg"
destination = " newImage.png"
scale_percent = 50

scr = cv2.imread(source,cv2.IMREAD_UNCHANGED)

# PERCENT BY WHICH THE IMAGE IS RESIZED

# Calculating the 50 percent of original dimensions
new_width = int(scr.shape[1]* scale_percent/100)
new_height = int(scr.shape[0]* scale_percent/100)

# resize image
output = cv2.resize(scr, (new_width,new_height))

cv2.imwrite(destination, output)