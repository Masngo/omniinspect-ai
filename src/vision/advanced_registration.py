import cv2
import numpy as np

def process_high_throughput_frame(image_bytes: bytes) -> dict:
    """
    OpenCV 5 Advanced Vision Pipeline optimized for COOL / AWS Graviton.
    Executes bilateral filtering, gradient magnitude profiling, and contour segmentation.
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if frame is None:
        raise ValueError("Failed to decode image stream.")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filtered = cv2.bilateralFilter(gray, 9, 75, 75)
    
    grad_x = cv2.Sobel(filtered, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(filtered, cv2.CV_32F, 0, 1, ksize=3)
    gradient_magnitude = cv2.magnitude(grad_x, grad_y)
    
    _, thresh = cv2.threshold(normalize_u8(gradient_magnitude), 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    total_defect_area = float(sum(cv2.contourArea(c) for c in contours))
    ambiguous = 80.0 < total_defect_area < 450.0
    status = "REJECT" if total_defect_area >= 450 else ("REVIEW_REQUIRED" if ambiguous else "PASS")

    return {
        "status": status,
        "defect_area_px": total_defect_area,
        "contour_count": len(contours),
        "ambiguous_flag": ambiguous,
        "engine": "COOL-OpenCV5-Arm64"
    }

def normalize_u8(img_float):
    return cv2.normalize(img_float, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
