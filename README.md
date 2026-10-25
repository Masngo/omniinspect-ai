# OmniInspect Enterprise

Autonomous Multi-Modal Visual Inspection & Quality Control System  
*Submitted to the OpenCV AI Competition 2026*

<p align="left">
  <a href="https://omniinspect-ai-ialbbmzohmxvknbos5vjpy.streamlit.app">
    <img src="https://img.shields.io/badge/Open_in-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Live App">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License MIT">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/OpenCV-5.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV 5">
  </a>
</p>

---

## 🔗 Quick Links & Live Demos

* 🌐 **Live Streamlit App:** [https://omniinspect-ai-ialbbmzohmxvknbos5vjpy.streamlit.app](https://omniinspect-ai-ialbbmzohmxvknbos5vjpy.streamlit.app)
* 📁 **GitHub Repository:** [https://github.com/Masngo/omniinspect-ai](https://github.com/Masngo/omniinspect-ai)[cite: 2]
* 🎥 **3-Minute Demo Video:** [YouTube / Vimeo Demo Link] *(See Devpost Submission)*
* 🏛️ **System Architecture Spec:** Documented below in this README

---

## 1. System Architecture Overview

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          1. INPUT & INGESTION PIPELINE                          │
│                                                                                 │
│   [ Live Camera Stream ]               [ Interactive Upload ]                   │
│   (RTSP / Video Feed)                  (Images, Videos, Archives)               │
│            │                                       │                            │
│            └───────────────────┬───────────────────┘                            │
│                                │                                                │
│                                ▼                                                │
│                   ┌─────────────────────────┐                                   │
│                   │ Streamlit Ingestion UI  │                                   │
│                   └────────────┬────────────┘                                   │
│                                │ Validation & Buffer                            │
│                                ▼                                                │
│                   ┌─────────────────────────┐                                   │
│                   │ Secure RAM / In-Memory  │                                   │
│                   └────────────┬────────────┘                                   │
└────────────────────────────────┼────────────────────────────────────────────────┘
                                 │ Decoded Frame Streams
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          2. CORE PROCESSING ENGINE                              │
│                                                                                 │
│                   ┌─────────────────────────┐                                   │
│                   │    OpenCV 5 Engine      │                                   │
│                   │ (Pre-filter, Threshold, │                                   │
│                   │  Edge & ROI Detection)  │                                   │
│                   └────────────┬────────────┘                                   │
│                                │ Extracted Features & Frame Tensors             │
│                                ▼                                                │
│                   ┌─────────────────────────┐                                   │
│                   │  Agentic Vision Core    │                                   │
│                   │ (Multi-Agent Reasoning, │                                   │
│                   │  Defect Classification) │                                   │
│                   └────────────┬────────────┘                                   │
│                                │ Structured Payload                             │
│                                ▼                                                │
│                   ┌─────────────────────────┐                                   │
│                   │  Pydantic Validation    │                                   │
│                   │ (Schema Enforcement &   │                                   │
│                   │   Tolerance Checks)     │                                   │
│                   └────────────┬────────────┘                                   │
└────────────────────────────────┼────────────────────────────────────────────────┘
                                 │ Validated Detection Data
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         3. OPERATIONAL DASHBOARD                                │
│                                                                                 │
│                   ┌─────────────────────────┐                                   │
│                   │  Streamlit Dashboard    │                                   │
│                   │  • Bounding Box Overlay │                                   │
│                   │  • Pass/Fail Analytics  │                                   │
│                   │  • Real-Time Alerts     │                                   │
│                   └─────────────────────────┘                                   │
└─────────────────────────────────────────────────────────────────────────────────┘
2. End-to-End Processing Workflow
Step 1: Input Ingestion & In-Memory Preprocessing
Multi-Modal Input Support: Ingests live video streams (RTSP/IP cameras) or manual inspection media via the Streamlit web interface.

Validation & Security: Verifies uploaded files against supported format specifications (e.g., JPEG, PNG, MP4, AVI) to prevent corrupt payloads from entering the stream.

Zero-Disk In-Memory Buffer: Uploaded binaries and live stream frames are buffered directly in RAM as raw NumPy array representations, bypassing disk write overhead and minimizing processing latency.

Step 2: Computer Vision Feature Extraction (OpenCV 5 Engine)
Image Normalization: Applies contrast adjustment, color space conversion, and noise reduction filters (e.g., Gaussian, Bilateral filtering).

Region of Interest (ROI) Cropping: Isolates key target regions across assembly lines or product components.

Edge & Anomaly Pre-filtering: Executes high-speed Canny edge detection, thresholding, and contour extraction to isolate potential surface fractures, misalignments, or structural defects prior to deep analysis.

Step 3: Multi-Agent Reasoning (Agentic Vision Core)
Defect Classification: Feeds extracted ROIs and visual feature maps into multi-agent vision models to classify anomaly types (e.g., surface scratches, dimensional out-of-tolerance, missing components, or packaging flaws).

Severity Analysis & Autonomous Remediation: Calculates anomaly confidence scores and severity indexes to automatically trigger component rejection flags or signal operational alarms.

Step 4: Data Validation & Schema Enforcement (Pydantic)
Strict Schema Typing: Encapsulates visual inspection metrics into strictly defined Pydantic data models.

Boundary & Quality Constraints: Enforces strict validation on bounding-box coordinates, detection timestamps, defect classes, and tolerance thresholds prior to UI rendering or database logging.

Step 5: Interactive Operational Dashboard (Streamlit UI)
Real-Time Visual Overlay: Renders interactive image/video overlays featuring bounding boxes, segmentation masks, and color-coded severity tags.

Telemetry & Analytics: Summarizes pass/fail ratios, throughput metrics, defect density distribution, and audit trail records in real time.
