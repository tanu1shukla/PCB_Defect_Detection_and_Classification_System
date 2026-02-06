import cv2
import numpy as np
import glob
import os

def rotate_bound_white_bg(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    
    return cv2.warpAffine(image, M, (nW, nH), borderValue=(143,148,151))

rot_dir = r"preprocessing\single image\ds\rotated"
angle_file = r"preprocessing\single image\ds\rotated\angle.txt"
out_dir = r"preprocessing\single image\ds\unrotated"

# Create output directory
os.makedirs(out_dir, exist_ok=True)

# Read angles dict
angles = {}
try:
    with open(angle_file, "r") as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                name, ang = parts
                angles[name] = float(ang)
    print(f"Loaded {len(angles)} angles: {list(angles.keys())}")
except FileNotFoundError:
    print(f"angle.txt not found: {angle_file}")
    exit()

# Find rotated images (DIRECTORY, not single file)
paths = glob.glob(os.path.join(rot_dir, "*.jpg"))
print(f"Found {len(paths)} rotated images")

if not paths:
    print("No .jpg files in rotation directory!")
    exit()

# Unrotate each image
success_count = 0
for path in paths:
    file_name = os.path.splitext(os.path.basename(path))[0]  # Clean filename extraction
    
    if file_name in angles:
        angle = angles[file_name]
        reverse_angle = -angle
        
        img_rot = cv2.imread(path)
        if img_rot is None:
            print(f"Failed to load: {path}")
            continue
            
        img_unrot = rotate_bound_white_bg(img_rot, reverse_angle)
        
        out_path = os.path.join(out_dir, file_name + ".jpg")
        cv2.imwrite(out_path, img_unrot)
        print(f"Unrotated {file_name} by {reverse_angle:.1f}° → {out_path}")
        success_count += 1
        
        # Show first image for verification
        if success_count == 1:
            cv2.imshow("Rotated", img_rot)
            cv2.imshow("Unrotated", img_unrot)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print(f"No angle for {file_name}")

print(f"\nCompleted: {success_count}/{len(paths)} images unrotated")
