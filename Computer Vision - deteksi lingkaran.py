import cv2
import numpy as np

# Ambil video
cap = cv2.VideoCapture(0)

while True:
    # baca video
    ret, frame = cap.read()

    output = frame.copy()
    # konversikan ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gunakan blurring untuk mengurangi noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.medianBlur(gray, 5)

    # konversi kebiner
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 3.5)

    # erosi
    kernel = np.ones((3, 3), np.uint8)
    gray = cv2.erode(gray, kernel, iterations=1)

    # dilatasi
    gray = cv2.dilate(gray, kernel, iterations=1)

    circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200,
                              param1=30, param2=45, minRadius=0, maxRadius=0)

    if circle is not None:
        # konversi x,y koordinat dan radius ke integer 16 bit tak bertanda
        circle = np.uint16(np.around(circle))

        for (x, y, r) in circle[0,:]:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output,(x-5, y-5), (x+5, y+5), (0, 128, 255),-1)

            print('radius :', r)

    cv2.imshow('gray', gray)
    cv2.imshow('frame', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
