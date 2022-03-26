from time import sleep
from cv2 import *
cam_port = 0
cam = VideoCapture(cam_port)
scode="0190576914082" #variable that will contain the scan code




if scode == scode :
    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

            # showing result, it take frame name and image
            # output
            imshow("GeeksForGeeks", image)

            # saving image in local storage
            imwrite("/home/pi/angga.png", image)

            # If keyboard interrupt occurs, destroy image
            # window
            waitKey(0)
            destroyWindow("GeeksForGeeks")

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")