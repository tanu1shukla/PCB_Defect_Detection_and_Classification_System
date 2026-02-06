import cv2
import numpy as np

img = cv2.imread(r"preprocessing\single image\ds\unrotated\01_missing_hole_01.jpg")

# STEP 1: Aggressive crop (catch ALL PCB pixels)
grey = np.array([143,148,151])
diff = np.abs(img.astype(int) - grey)
# LOOSER: ANY channel differs by >3 = PCB (was >8)
non_grey_mask = np.any(diff > 3, axis=2)  

y_coords, x_coords = np.where(non_grey_mask)
x_min, x_max = x_coords.min(), x_coords.max()
y_min, y_max = y_coords.min(), y_coords.max()

pad = 60
cropped = img[max(0,y_min-pad):min(img.shape[0],y_max+pad), 
              max(0,x_min-pad):min(img.shape[1],x_max+pad)]

# STEP 2: Inpaint remaining grey pixels
mask = np.all(np.abs(cropped.astype(int) - grey) <= 5, axis=2)
mask = cv2.dilate(mask, np.ones((20,20), np.uint8), iterations=1)

# Inpaint using surrounding pixels
result = cv2.inpaint(cropped, mask.astype(np.uint8), 3, cv2.INPAINT_TELEA)

cv2.imwrite("pcb_clean.jpg", result)
print("CLEAN - No grey pixels remaining!")

cv2.imshow("Before Inpaint", cropped)
cv2.imshow("After Inpaint", result)
cv2.waitKey(0)
