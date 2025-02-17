import cv2
import mediapipe as mp
import time
import threading

# Initialize video capture with lower resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize mediapipe for hand detection with reduced complexity
mpHand = mp.solutions.hands
hands = mpHand.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# Initialize variables for FPS calculation
pTime = 0
cTime = 0

def process_frame(img):
    global results
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

while True:
    success, img = cap.read()
    if not success:
        break

    # Start a new thread to process the frame
    thread = threading.Thread(target=process_frame, args=(img,))
    thread.start()
    thread.join()

    if results.multi_hand_landmarks:
        for handLmarks in results.multi_hand_landmarks:
            for id, lmark in enumerate(handLmarks.landmark):
                height, width, _ = img.shape
                centre_x, centre_y = int(lmark.x * width), int(lmark.y * height)

                if id == 20 or id == 8:
                    cv2.circle(img, (centre_x, centre_y), 10, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLmarks, mpHand.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
