import mediapipe
import cv2
import time

def run_hand_tracker():
    drawingModule = mediapipe.solutions.drawing_utils
    handsModule = mediapipe.solutions.hands
    w = 640
    h = 480

    cap = cv2.VideoCapture(0)

    with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1) as hands:
        finger_names = {
            4: "Thumb",
            8: "Index Finger",
            12: "Middle Finger",
            16: "Ring Finger",
            20: "Pinky Finger"
        }

        while True:
            ret, frame = cap.read()
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            start = time.time()
            frame1 = cv2.resize(frame, (640, 480))
            results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))

            if results.multi_hand_landmarks:
                for handLandmarks in results.multi_hand_landmarks:
                    drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                    list = []
                    for id, pt in enumerate(handLandmarks.landmark):
                        x = int(pt.x * w)
                        y = int(pt.y * h)
                        list.append([id, x, y])
                    for val in list:
                        if val[0] < 6:
                            print(val)
                    for point in handsModule.HandLandmark:
                        normalizedLandmark = handLandmarks.landmark[point]
                        pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, 640, 480)
                        if point in finger_names:
                            print(f"{finger_names[point]}: {pixelCoordinatesLandmark}")

            cv2.imshow("Frame", frame1)
            key = cv2.waitKey(1) & 0xFF
            end = time.time()
            if key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

