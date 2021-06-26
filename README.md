# Opencv-projects
This repository consists of  mini projects related to Opencv and Machine learning..



In project1 :  Lane Detection :
                    I used a frame of a video to analyse the path in which a vehicle is moving. Thius helps in extracting an image from a video 
                    which later on is used for real time lane detection which is used in most of the autonomous vehicles.The very first thing we 
                    must do before we can process an image is… read an image! The following snippet can be used to load an image from a file into 
                    an array of image data which can be manipulated in python:
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# reading in an image
image = mpimg.imread('lane3.jpg')
#printing the image
plt.imshow(image)
plt.show()
                    Now that we have our image loaded we define a region of interest i.e to the region which we need to detect in the image..This can be achieved through
 
height = image.shape[0]
width = image.shape[1]
ROI_vertices = [(0, height), (width / 3, height / 3), (width / 1.3, height / 3), (width, height)] 
                         
                         Here we name the dimensions i.e Height and Width of the image inthe first two lines and create a list which holds the vertices in the image..
                         In ROI_VERTICES the parameters passed will create a polygon which is close to trapezium , in which most of the lane is covered..
                         Now that we have a cropped image of the original image we can convert this cropped iumage into a gray scale image(This is needed inorder to filter out the 
                         colours that are present in the image) Since we need to find the white lines presesnt on the road we need to convert the image from BGR format to GRAY 
                         Now we detect the edges present in the image using canny function in opencv..Canny edge detection function detect the areas where there is a massive 
                         change in intensity value. These represent the edges in our image.
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
canny_image = cv.Canny(gray,100,200)
cropped_image = ROI(canny_image, np.array([ROI_vertices], np.int32)) 
                         
                         Now we pass this canny image to our ROI function where a duplicate of this image is generated i.e a masked image highlighting the pixels on lines in 
                         the image.This result is stored in a variable (in our case Cropped_image) where it is again sent to function Houghlinesp()..
lines = cv.HoughLinesP(cropped_image,
                      rho = 5,
                      theta=np.pi/100,
                      threshold=160,
                      lines=np.array([]),
                      minLineLength=60,
                      maxLineGap=17)
                      
                        Here parameters like
                        RHO -  The distance from the origin to the line along a vector perpendicular to the line(which is detected in the image)
                        THETA - The angle in degrees between the x-axis and the line in the image.
                        THRESHOLD - The minimum number of intersections to detect a line.
                        MinLineLength: The minimum number of points that can form a line. Lines with less than this number of points are disregarded.
                        MaxLineGap: The maximum gap between two points to be considered in the same line.
                            
                        At last we match these lines and the image together using DRAW_LINES() in opencv. This will produce our desired result..
                        
                        
                        
                         
                         
                         
