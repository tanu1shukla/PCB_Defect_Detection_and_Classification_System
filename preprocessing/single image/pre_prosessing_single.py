import cv2
import numpy as np
import os

# Set your exact paths here (from your PCB project)
template_path = r"preprocessing\single image\ds\pcb-used\01.JPG"  # Good PCB
test_path = r"preprocessing\single image\ds\image\01_missing_hole_01.jpg"             # Defective PCB
output_dir = r"preprocessing\single image\ds\aligned"
os.makedirs(output_dir, exist_ok=True)

# Load grayscale
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
test = cv2.imread(test_path, cv2.IMREAD_GRAYSCALE)

print("Template:", template.shape if template is not None else "FAILED")
print("Test:", test.shape if test is not None else "FAILED")

if template is None or test is None:
    print("Fix paths above!")
else:
    # ORB alignment
    orb = cv2.ORB_create(nfeatures=5000)
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(test, None)
    
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = sorted(matcher.match(des1, des2), key=lambda x: x.distance)[:100]
    
    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)
    
    H, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
    h, w = template.shape
    test_aligned = cv2.warpPerspective(test, H, (w, h))
    
    # Subtraction + Otsu
    diff = cv2.absdiff(template, test_aligned)
    diff_blur = cv2.GaussianBlur(diff, (5,5), 0)
    ret, thresh = cv2.threshold(diff_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # ret = scalar threshold
    
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Save results
    base = "result"
    cv2.imwrite(f"{output_dir}{base}_aligned.png", test_aligned)
    cv2.imwrite(f"{output_dir}{base}_diff.png", diff)
    cv2.imwrite(f"{output_dir}{base}_thresh.png", cleaned)
    
    print(f"Saved to {output_dir}: Otsu threshold = {ret:.1f}")  # FIXED: use ret, not thresh[1]
    
    # Quick preview
    cv2.imshow("Defect Mask", cleaned)
    cv2.waitKey(0)
    cv2.destroyAllWindows()