# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(0)

#camera 2
vid2 = cv2.VideoCapture(1)


while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	ret, frame2 = vid2.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)

	cv2.imshow('frame2', frame2)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()

vid2.release()
# Destroy all the windows
cv2.destroyAllWindows()
