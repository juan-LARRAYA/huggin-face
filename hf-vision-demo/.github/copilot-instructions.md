# Copilot Instructions for HF Vision Demo

## Project Overview
- **Purpose:** Real-time demo of the 3 most popular Hugging Face vision models (CLIP, ViT, DETR) using a webcam and interactive frontend.
- **Architecture:**
  - `backend/` (Python/FastAPI): Serves model inference endpoints for image classification, zero-shot, and object detection.
  - `frontend/` (HTML/JS): Captures webcam, sends frames to backend, visualizes results (labels, bounding boxes).

## Key Components
- **Backend:**
  - Loads all models at startup for fast inference.
  - Endpoints:
    - `/classify` (ViT): Image classification
    - `/clip` (CLIP): Zero-shot with fixed prompts
    - `/clip-custom` (CLIP): Zero-shot with user prompts (comma-separated)
    - `/detect` (DETR): Object detection
  - Uses `transformers`, `torch`, and `PIL` for model and image handling.
  - CORS enabled for all origins (frontend runs separately).
- **Frontend:**
  - `index.html` is the main UI. Uses webcam, overlays results, and calls backend endpoints.
  - Model selection via buttons; custom prompts supported for CLIP.
  - Bounding boxes drawn for DETR results.

## Developer Workflows
- **Setup:**
  - Create a Python 3.9+ virtual environment and install from `requirements.txt`.
- **Run backend:**
  - `uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000`
- **Run frontend:**
  - Open `frontend/index.html` directly or serve with `python -m http.server 3000`.
- **Model downloads:**
  - Models are downloaded on first run (~1-2GB total).

## Project Conventions
- All model inference is synchronous and handled in memory (no async GPU batching).
- Prompts for CLIP are comma-separated strings (see `/clip-custom`).
- All API responses are JSON with `model` and `results` keys.
- Frontend expects results as `{label, score}` for classifiers, `{label, score, box}` for DETR.
- No authentication or user management; CORS is open for demo simplicity.

## Integration & Extensibility
- To add new models, follow the pattern in `backend/main.py` (load at startup, add endpoint).
- Frontend expects endpoints at `localhost:8000` by default.
- For production, secure CORS and consider model warmup/health checks.

## References
- See `README.md` for user-facing instructions and troubleshooting.
- Example API usage and data formats are in `backend/main.py` and `frontend/index.html`.
