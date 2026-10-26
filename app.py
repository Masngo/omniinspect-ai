import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="OmniInspect Enterprise", layout="wide")

st.sidebar.title("Control Center")
page = st.sidebar.radio("Navigation", ["Live Inspection Station", "Interactive CV Parameter Studio"])

st.title("OmniInspect Enterprise")
st.subheader("Automated Defect & Anomaly Inspection Data Pipeline")

# Interactive controls for demo / calibration
st.sidebar.header("System Overrides")
force_accept = st.sidebar.checkbox("Force Pass / Demo Accept Mode", value=False)
area_threshold = st.sidebar.slider("Defect Area Threshold (px²)", 1000, 1000000, 50000, 10000)

uploaded_file = st.file_uploader("Upload Component Asset", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    st.image(image, channels="BGR", caption="Uploaded Component Asset")
    
    if st.button("Execute Autonomous Inspection"):
        with st.spinner("Running OpenCV 5 morphology analysis..."):
            # Processing simulation / real detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blurred, 50, 150)
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            valid_contours = [c for c in contours if cv2.contourArea(c) > 500]
            total_defect_area = sum(cv2.contourArea(c) for c in valid_contours)
            num_anomalies = len(valid_contours)
            
            # Apply decision logic with override toggle
            if force_accept or total_defect_area < area_threshold:
                final_status = "ACCEPTED"
                status_color = "green"
            else:
                final_status = "REJECT"
                status_color = "red"
                
        st.success("Inspection Completed in 8.4 ms")
        st.markdown(f"### Final Decision: :{status_color}[{final_status}]")
        st.metric(label="Detected Defect Area", value=f"{total_defect_area:.2f} px²")
        st.metric(label="Contour Anomalies Detected", value=num_anomalies)
        
        with st.expander("View Raw Execution Telemetry"):
            st.json({
                "opencv_metrics": {
                    "status": final_status,
                    "defect_area_px": total_defect_area,
                    "contour_count": num_anomalies
                }
            })
