#Import the necessary Packages for this software to run
import mediapipe
import cv2
import time

#Use MediaPipe to draw the hand framework over the top of hands it identifies in Real-Time
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands
w = 640
h = 480

#Use CV2 Functionality to create a Video stream and add some values
cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

#Add confidence values and extra settings to MediaPipe hand tracking. As we are using a live video stream this is not a static
#image mode, confidence values in regards to overall detection and tracking and we will only let two hands be tracked at the same time
#More hands can be tracked at the same time if desired but will slow down the system
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1) as hands:

     finger_names = {
        4: "Thumb",
        8: "Index Finger",
        12: "Middle Finger",
        16: "Ring Finger",
        20: "Pinky Finger"
        }
     
#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
     while True:
           ret, frame = cap.read()
           cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
           start =time.time()
           #Unedit the below line if your live feed is produced upsidedown
           #flipped = cv2.flip(frame, flipCode = -1)
           
           #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
           frame1 = cv2.resize(frame, (640, 480))
           
           #produces the hand framework overlay ontop of the hand, you can choose the colour here too)
           results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
           
           #Incase the system sees multiple hands this if statment deals with that and produces another hand overlay
           if results.multi_hand_landmarks != None:
               for handLandmarks in results.multi_hand_landmarks:
                    drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                    list = []
                    for id, pt in enumerate (handLandmarks.landmark):
                        x = int(pt.x * w)
                        y = int(pt.y * h)
                        list.append([id,x,y])
                    for val in list:
                        if (val[0] < 6):
                            #print("test_ponit")
                            print(val)
                  #   Added Code to find Location of Index Finger !!
                    for point in handsModule.HandLandmark:
                      
                      normalizedLandmark = handLandmarks.landmark[point]
                      pixelCoordinatesLandmark= drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, 640, 480)
                      
                      if point == 4:
                        #print(point)
                        #print(pixelCoordinatesLandmark)
                        #print(normalizedLandmark)
                        #print("hello")
                        print(f"{finger_names[point]}:{pixelCoordinatesLandmark}")
                        #Sprint(f"Normalized {finger_names[point]}:{normalizedLandmark}")
                      if point == 8:
                        #print(point)
                        #print(pixelCoordinatesLandmark)
                        #print(normalizedLandmark)
                        #print("hello")
                        print(f"{finger_names[point]}:{pixelCoordinatesLandmark}")
                        #print(f"Normalized {finger_names[point]}:{normalizedLandmark}")
                      if point == 12:
                        #print(point)
                        #print(pixelCoordinatesLandmark)
                        #print(normalizedLandmark)
                        #print("hello")
                        print(f"{finger_names[point]}:{pixelCoordinatesLandmark}")
                        #print(f"Normalized {finger_names[point]}:{normalizedLandmark}")
                      if point == 16:
                        #print(point)
                        #print(pixelCoordinatesLandmark)
                        #print(normalizedLandmark)
                        #print("hello")
                        print(f"{finger_names[point]}:{pixelCoordinatesLandmark}")
                        #print(f"Normalized {finger_names[point]}:{normalizedLandmark}")
                      if point == 20:
                        #print(point)
                        #print(pixelCoordinatesLandmark)
                        #print(normalizedLandmark)
                        #print("hello")
                        print(f"{finger_names[point]}:{pixelCoordinatesLandmark}")
                        #print(f"Normalized {finger_names[point]}:{normalizedLandmark}")

                    
            
           #Below shows the current frame to the desktop 
           cv2.imshow("Frame", frame1);
           key = cv2.waitKey(1) & 0xFF
           
           end = time.time()
#            print (end-start)

