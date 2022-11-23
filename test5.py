from PoseModule import PoseDetector
import cv2
import pafy

url='https://www.youtube.com/watch?v=-Lw8Ri6BGzA'
videoPafy = pafy.new(url)
best = videoPafy.getbest()
cap = cv2.VideoCapture(best.url)

# cap = cv2.VideoCapture(0)
detector = PoseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        # print(lmList)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()