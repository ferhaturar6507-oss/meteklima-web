import cv2
import os

video_path = "Air_conditioner_rotating_in_studio_202608221858.mp4"
output_dir = "images/ac_frames"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)
count = 0

print("Extracting frames...")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save frame as JPG
    frame_path = os.path.join(output_dir, f"frame_{count:04d}.jpg")
    cv2.imwrite(frame_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    count += 1

cap.release()
print(f"Extracted {count} frames.")
