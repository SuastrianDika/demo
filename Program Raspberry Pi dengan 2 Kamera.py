import cv2
import threading

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()

        if rval :
             cv2.imshow("GeeksForGeeks", frame)
  
             # saving image in local storage
             cv2.imwrite("D:\capture.png", frame)
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

# Create two threads as follows
x = int(input('tekan 1 untuk mencapture kamera 1/ tekan 2 untuk mencapture kamera 2 : '))

if x == 1:
    thread1 = camThread("Camera 1", 1)
    thread1.start()
if x == 2:
    thread2 = camThread("Camera 2", 2)
    thread2.start()


