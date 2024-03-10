import cv2
import numpy as np

# Function to process video frames and draw lines
def process_video(cap, a_thresh ):
    a1 = 0
    b1 = 0
    p1 = 0
    p2 = 0
    count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        img = cv2.cvtColor(fgmask, cv2.COLOR_BGR2RGB)
        edge = cv2.Canny(img, 200, 200)
        lines = cv2.HoughLines(edge, 1, np.pi / 180, a_thresh)

        if lines is not None:
            for line in lines:
                rho, theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)

                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                if x1 < 500 or x2 < 500 or x1 > 1350 or x2 > 1350:
                    continue
                a1 = a1 + a
                b1 = b1 + b
                p1 = p1 + x0
                p2 = p2 + y0
                count = count + 1

                #cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        
        if count != 0:
            afinal = a1 / count
            bfinal = b1 / count
            p1final = p1 / count
            p2final = p2 / count
            x1_final = int(p1final + 1000 * (-bfinal))
            y1_final = int(p2final + 1000 * (afinal))
            x2_final = int(p1final - 1000 * (-bfinal))
            y2_final = int(p2final - 1000 * (afinal))
            cv2.line(frame, (x1_final, y1_final), (x2_final, y2_final), (0,0, 255), 2)

        cv2.imshow('frame', frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap1 = cv2.VideoCapture('t1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap1, a_thresh=100)


cap2 = cv2.VideoCapture('t2.1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap2, a_thresh=200)
cap3 = cv2.VideoCapture('t2.2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap3, a_thresh=150)

cap4 = cv2.VideoCapture('t3.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap4, a_thresh=195)

cap5 = cv2.VideoCapture('t4.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap5, a_thresh=105)

cap6 = cv2.VideoCapture('t5.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap6, a_thresh=100)

cap7 = cv2.VideoCapture('t6.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap7, a_thresh=100)

cap8 = cv2.VideoCapture('t7.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap8, a_thresh=200)

cap9 = cv2.VideoCapture('t8.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap9, a_thresh=135)

cap10 = cv2.VideoCapture('t9.1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
process_video(cap10, a_thresh=135)

cap11 = cv2.VideoCapture('t9.2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap11, a_thresh=185)

cap12 = cv2.VideoCapture('t10.1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap12, a_thresh=185)

cap13 = cv2.VideoCapture('t10.2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap13, a_thresh=165)

cap14 = cv2.VideoCapture('t11.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap14, a_thresh=178)

cap15 = cv2.VideoCapture('t12.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap15, a_thresh=178)

cap16 = cv2.VideoCapture('t13.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap16, a_thresh=178)

cap17 = cv2.VideoCapture('t14.1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap17, a_thresh=100)

cap18 = cv2.VideoCapture('t14.2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap18, a_thresh=200)

cap19 = cv2.VideoCapture('t15.1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))

process_video(cap19, a_thresh=135)

cap20 = cv2.VideoCapture('t15.2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
 

process_video(cap20, a_thresh=105)


cap1.release()
cap2.release()
cap3.release()
cap4.release()
cap5.release()
cap6.release()
cap7.release()
cap8.release()
cap9.release()
cap10.release()
cap11.release()
cap12.release()
cap13.release()
cap14.release()
cap15.release()
cap16.release()
cap17.release()
cap18.release()
cap19.release()
cap20.release()

cv2.destroyAllWindows()
