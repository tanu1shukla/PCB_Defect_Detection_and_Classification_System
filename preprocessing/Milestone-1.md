## Milestone 1: Dataset Preparation and Image Processing

### Module 1: Dataset Setup and Image Subtraction 
Tasks: 
- Set up and inspect DeepPCB dataset. 
- Align and preprocess image pairs (template and test). 
- Apply image subtraction to obtain defect difference maps. 
- Use thresholding (Otsu’s method) and filters to highlight defect regions. 

Deliverables: 
- Cleaned and aligned dataset 
- Subtraction and thresholding script 
- Sample defect-highlighted images 

Evaluation: 
- Accurate defect mask generation 
- Proper image alignment and subtraction clarity 

### Module 2: Contour Detection and ROI Extraction 
Tasks: 
- Use OpenCV to detect contours of defects. 
- Extract bounding boxes and crop individual defect regions. 
- Label defect ROIs for model training. 

Deliverables: 
- ROI extraction pipeline 
- Cropped and labeled defect samples 
- Visualization of defect contours 

Evaluation: 
- Precision of ROI detection and bounding box accuracy