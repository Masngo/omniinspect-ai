import cv2
import numpy as np

def analyze_part_defect(image_bytes: bytes, crop_box=None, exposure_boost=1.0):
    """
    Simulates OpenCV 5 high-speed image processing optimized for AWS Graviton (COOL).
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if frame is None:
        raise ValueError("Invalid image buffer provided.")
    
    if exposure_boost != 1.0:
        frame = cv2.convertScaleAbs(frame, alpha=exposure_boost, beta=0)
        
    if crop_box:
        x, y, w, h = crop_box
        frame = frame[y:y+h, x:x+w]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    defect_score = float(sum(cv2.contourArea(c) for c in contours))
    ambiguous = 50.0 < defect_score < 300.0
    
    status = "FLAGGED" if defect_score >= 300 else ("UNCERTAIN" if ambiguous else "CLEAR")
    
    return {
        "defect_score": defect_score,
        "contour_count": len(contours),
        "ambiguous": ambiguous,
        "status": status
    }
