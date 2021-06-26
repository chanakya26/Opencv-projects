import cv2 as cv
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def ROI(img,vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

def draw_lines(img,lines):
    img = np.copy(img)
    line_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(line_image,(x1,y1),(x2,y2),(0,255,0),thickness=4)
    img = cv.addWeighted(img, 0.8, line_image,1,0.0)
    return img

try:
    image = mpimg.imread("lane4.jpg")
except FileNotFoundError as error:
    print("Error opening the file")

height = image.shape[0]
width = image.shape[1]
ROI_vertices = [(0, height), (width / 3, height / 3), (width / 1.3, height / 3), (width, height)]


gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
canny_image = cv.Canny(gray,100,200)
cropped_image = ROI(canny_image, np.array([ROI_vertices], np.int32))

lines = cv.HoughLinesP(cropped_image,
                      rho = 5,
                      theta=np.pi/100,
                      threshold=160,
                      lines=np.array([]),
                      minLineLength=60,
                      maxLineGap=17)

output_image = draw_lines(image,lines)
plt.imshow(output_image)
plt.show()

