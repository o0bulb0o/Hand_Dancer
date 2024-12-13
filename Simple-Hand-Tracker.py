import mediapipe
import cv2
import time

class HandTracker:
    
    def __init__(self):
        self.drawingModule = mediapipe.solutions.drawing_utils
        self.handsModule = mediapipe.solutions.hands
        self.w = 640
        self.h = 480
        self.cap = cv2.VideoCapture(0)
        self.finger_names = {
            4: "Thumb",
            8: "Index Finger",
            12: "Middle Finger",
            16: "Ring Finger",
            20: "Pinky Finger"
        }
        self.hand_mark = []
      
    
    def return_gesture(self):
        # recognize the gesture here!!
        if (self.hand_mark [4].x * 640 < self.hand_mark [5].x * 640 and
            self.hand_mark [8].y > self.hand_mark [5].y and
            self.hand_mark [12].y > self.hand_mark [9].y and
            self.hand_mark [16].y > self.hand_mark [13].y):
            print("Fist gesture detected")
            return "Fist"
        
        # OK gesture
        if (abs(self.hand_mark [4].x - self.hand_mark [8].x) < 0.05 and
            abs(self.hand_mark [4].y - self.hand_mark [8].y) < 0.05 and
            self.hand_mark [12].y < self.hand_mark [9].y and
            self.hand_mark [16].y < self.hand_mark [13].y):
            print("OK gesture detected")
            return "OK"
        
        # Palm gesture
        if (self.hand_mark [4].x > self.hand_mark [2].x and
            self.hand_mark [8].y < self.hand_mark [7].y and
            self.hand_mark [12].y < self.hand_mark [11].y and
            self.hand_mark [16].y < self.hand_mark [15].y):
            print("Palm gesture detected")
            return "Palm"
        
        # Pointing gesture
        if (self.hand_mark [8].y < self.hand_mark [7].y and
            self.hand_mark [12].y > self.hand_mark [9].y and
            self.hand_mark [16].y > self.hand_mark [13].y):
            print("Pointing gesture detected")
            return "Pointing"
      

    def update_hand_mark(self):
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

                        drawingModule.draw_hand_marks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                        list = []
                        for id, pt in enumerate(handLandmarks.hand_mark ):
                            x = int(pt.x * w)
                            y = int(pt.y * h)
                            list.append([id, x, y])
                        for val in list:
                            if val[0] < 6:
                                print(val)
                        for point in handsModule.HandHand_mark :
                            normalizedHand_mark  = handLandmarks.hand_mark [point]
                            pixelCoordinatesHand_mark  = drawingModule._normalized_to_pixel_coordinates(normalizedHand_mark .x, normalizedHand_mark .y, 640, 480)
                            if point in finger_names:
                                print(f"{finger_names[point]}: {pixelCoordinatesHand_mark }")
                        self.hand_mark = list

                cv2.imshow("Frame", frame1)
                key = cv2.waitKey(1) & 0xFF
                end = time.time()
                print(f"FPS: {(end - start)}")

    def close(self):    
        self.cap.release()
        cv2.destroyAllWindows()

