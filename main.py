import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        count = 0
        for handData in results.multi_hand_landmarks:

            # for id, lm in enumerate(handData.landmark):
            #     h, w, c = img.shape
            #     cx, cy = int(lm.x*w), int(lm.y*h)
            for i in range(4):
                if handData.landmark[8+(i*4)].y < handData.landmark[6+(i*4)].y:
                    count += 1
            if abs(handData.landmark[9].x - handData.landmark[17].x) < abs(handData.landmark[9].x - handData.landmark[4].x):
                count += 1
            # mpDraw.draw_landmarks(img, handData, mpHands.HAND_CONNECTIONS)
        cv2.putText(img, str(count), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 5)







    cv2.imshow("image", img)


    cv2.waitKey(1)
