import cv2
import serial
import time
import os

SERIAL_PORT = 'COM3'   
BAUD_RATE = 115200
CAMERA_INDEX = 0       
SAVE_FOLDER = 'timelapse_photos'

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

ser = None
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.01)
except Exception:
    pass

cap = cv2.VideoCapture(CAMERA_INDEX)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

if not cap.isOpened():
    exit(1)

photo_count = 0

while True:
    try:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.1)
            continue
            
        cv2.imshow("Camera", frame)
        
        key = cv2.waitKey(1) & 0xFF
        take_photo = False
        
        if key == ord('q'):
            break
        elif key == ord('m'):
            take_photo = True
            
        if ser and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line == "TRIGGER":
                take_photo = True
                
        if take_photo:
            filename = os.path.join(SAVE_FOLDER, f"frame_{photo_count:05d}.jpg")
            cv2.imwrite(filename, frame)
            
            flash = frame.copy()
            flash[:] = (255, 255, 255)
            cv2.imshow("Camera", flash)
            cv2.waitKey(50)
            
            print(f"Captured {filename}")
            photo_count += 1
            
    except KeyboardInterrupt:
        break
    except Exception as e:
        time.sleep(1)

cap.release()
cv2.destroyAllWindows()
if ser is not None:
    ser.close()
