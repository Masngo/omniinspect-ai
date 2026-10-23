# OmniInspect-Enterprise 🚀
**Autonomous Industrial Inspection Platform Powered by OpenCV 5, AWS Graviton (COOL), and Agentic Vision Loops**

---

## 📋 Overview
**OmniInspect-Enterprise** is an advanced, production-grade automated optical inspection (AOI) system designed for high-throughput manufacturing environments. Built for the **OpenCV AI Competition 2026**, the system bridges low-latency computer vision with an autonomous agentic decision-making loop. 

Traditional inspection platforms rely on static pixel thresholds that result in high false-positive rates when handling edge cases or minor lighting variations. OmniInspect-Enterprise solves this by combining **OpenCV 5** high-throughput image processing pipelines, **AWS Graviton / COOL** cloud acceleration, and a multi-step **Model Context Protocol (MCP)** perception-decision-action loop that dynamically adjusts handling for ambiguous items.

---

## 🏗️ System Architecture

```text
  ┌────────────────────────────────────────────────────────┐
  │                    Streamlit Dashboard                  │
  └───────────────────────────┬────────────────────────────┘
                              │ Live Telemetry & Control Feed
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │         Agentic Perception-Decision-Action Loop        │
  │              (Model Context Protocol / MCP)            │
  └──────────────┬──────────────────────────▲──────────────┘
                 │ Dynamic Tool Invocation  │ Feedback / Metrics
                 ▼                          │
  ┌────────────────────────────────────────────────────────┐
  │       OpenCV 5 (COOL) High-Throughput Engine           │
  │        - Graviton ARM Neon SIMD Acceleration           │
  │        - Advanced Registration & Defect Detection      │
  └───────────────────────────┬────────────────────────────┘
                              │ Benchmarks & Logging
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │              AWS Graviton Cloud Endpoint               │
  └────────────────────────────────────────────────────────┘


🔑 Key FeaturesOpenCV 5 Substantive Vision Pipeline:Advanced image registration, structural similarity indexing, thresholding, and contour feature extraction using OpenCV 5 modules.Robust fallback mechanisms ensuring uninterrupted telemetry even in containerized runtime environments.AWS Graviton & COOL Optimization:Optimized for ARM-based AWS Graviton instances utilizing the Cloud-Optimized OpenCV Library (COOL) for high-speed SIMD vector execution.Reduced latency, higher frame throughput, and lower cost-per-inference compared to traditional x86 baseline architectures.Agentic Vision & MCP Integration:Implements a true multi-step perception-decision-action loop.When primary OpenCV analysis detects a borderline anomaly ($80.0\text{ px} < \text{defect\_area} < 450.0\text{ px}$), the system dynamically triggers secondary tool calls (e.g., adaptive sub-region cropping and contrast enhancement) to update the decision route (PASS, REVIEW_REQUIRED, or REJECT) without manual operator intervention.🛠️ Project Structure
