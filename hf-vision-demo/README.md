# 🤖 HF Vision Demo - Top 3 Computer Vision Models

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![Transformers](https://img.shields.io/badge/🤗%20Transformers-4.44+-yellow.svg)](https://huggingface.co/transformers)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

An interactive real-time demo showcasing the **3 most popular computer vision models** from Hugging Face, running directly in your browser using your webcam.

## ✨ Features

- 🎥 **Real-time webcam processing**
- 🚀 **3 state-of-the-art AI models** in one application
- 🎨 **Modern, responsive web interface**
- 🔧 **Easy setup and deployment**
- 📱 **Cross-platform compatibility**
- 🎯 **Zero-shot classification** with custom prompts

## 🎯 Included Models

### 1. **CLIP** (openai/clip-vit-base-patch32)

![CLIP](https://img.shields.io/badge/Downloads-10M+-brightgreen)

- **What it does**: Zero-shot classification using text and images
- **Capabilities**: Classifies images using natural language descriptions
- **Use cases**: Content moderation, image search, flexible categorization
- **Example**: "a photo of a cat", "a person running", "Italian food"

### 2. **ViT** (google/vit-base-patch16-224)

![ViT](https://img.shields.io/badge/Downloads-5M+-brightgreen)

- **What it does**: Image classification using Vision Transformer
- **Capabilities**: Classifies images into 1000 ImageNet categories
- **Use cases**: Object recognition, product categorization, automated tagging
- **Example**: Identifies specific objects like "Golden Retriever", "laptop", "pizza"

### 3. **DETR** (facebook/detr-resnet-50)

![DETR](https://img.shields.io/badge/Downloads-2M+-brightgreen)

- **What it does**: Object detection using Detection Transformer
- **Capabilities**: Detects and localizes multiple objects with bounding boxes
- **Use cases**: Autonomous vehicles, security systems, quality control
- **Example**: Finds people, cars, animals and draws boxes around them

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** (3.10+ recommended)
- **Webcam** (built-in or external)
- **4GB+ RAM** (8GB+ recommended for optimal performance)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/juan-LARRAYA/huggin-face.git
   cd huggin-face/hf-vision-demo
   ```

2. **Create virtual environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server**:

   ```bash
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Open the frontend**:
   - Open `frontend/index.html` in your browser
   - Or serve with a local server: `python -m http.server 3000`

### First Run

⚠️ **Important**: The first execution will download the models (~2GB total). This may take several minutes depending on your internet connection.

## 🎮 How to Use

1. **Allow camera access** when prompted by your browser
2. **Try each model**:

   - 🔍 **ViT Classifier**: Classifies what the camera sees
   - 🎯 **CLIP Zero-Shot**: Classifies using predefined categories
   - 📦 **DETR Object Detection**: Detects and marks objects with boxes
   - 🎨 **CLIP Custom**: Use your own text prompts

3. **For CLIP Custom**: Write comma-separated prompts like:
   ```
   a happy person, an animal, technology, delicious food
   ```

## 📊 Interface Features

- 🎨 **Modern UI** with gradients and visual effects
- ⚡ **Real-time processing** using your webcam
- 🎯 **Interactive visualization** of detections with colored boxes
- 📈 **Results sorted by confidence**
- 📱 **Responsive design** that adapts to different screens
- 🔄 **Live updates** as you move objects in front of the camera

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   FastAPI       │    │  Hugging Face   │
│   (HTML/JS)     │◄──►│   Backend       │◄──►│    Models       │
│                 │    │                 │    │                 │
│ • Camera feed   │    │ • Image proc.   │    │ • CLIP          │
│ • UI controls   │    │ • Model calls   │    │ • ViT           │
│ • Visualization │    │ • API endpoints │    │ • DETR          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔧 Technical Details

- **Model loading**: Automatic download on first run (~2GB total)
- **GPU support**: Automatically detected if available (CUDA/MPS)
- **Memory usage**: 4-8GB RAM depending on models loaded
- **Performance**: ~1-3 seconds per inference depending on hardware
- **Supported formats**: JPEG, PNG images from webcam

## 🐛 Troubleshooting

### Common Issues

| Problem                    | Solution                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 🎥 **Camera not working**  | • Check browser permissions<br>• Try a different browser<br>• Ensure camera isn't used by other apps         |
| 🐌 **Slow inference**      | • First run downloads models (normal)<br>• Close other applications<br>• Use GPU if available                |
| 💾 **Out of memory**       | • Close other applications<br>• Use a machine with more RAM<br>• Restart the backend                         |
| 🌐 **Connection error**    | • Ensure backend is running on port 8000<br>• Check browser console for errors<br>• Verify firewall settings |
| 📦 **Model loading fails** | • Check internet connection<br>• Clear Hugging Face cache<br>• Restart with `--reload`                       |

### Performance Tips

- **GPU Acceleration**: Install CUDA (NVIDIA) or use Apple Silicon for better performance
- **Memory Management**: Close unnecessary applications before running
- **Browser Choice**: Chrome and Firefox typically perform best
- **Network**: Stable internet connection required for first-time model downloads

## 🎯 Example Use Cases

### 🏥 Healthcare

```
# CLIP prompts for medical imaging
"normal chest X-ray, pneumonia, fracture, medical equipment"
```

### 🛒 E-commerce

```
# Product categorization with ViT
Automatically classify product images into categories
```

### 🚗 Autonomous Vehicles

```
# DETR for object detection
Detect pedestrians, vehicles, traffic signs, road obstacles
```

### 📱 Social Media

```
# Content moderation with CLIP
"appropriate content, inappropriate content, violence, safe for work"
```

### 🏭 Quality Control

```
# Manufacturing defect detection
"defective product, normal product, damaged packaging"
```

## 📊 Model Comparison

| Model    | Size   | Speed  | Accuracy  | Best For                           |
| -------- | ------ | ------ | --------- | ---------------------------------- |
| **CLIP** | ~600MB | Medium | High      | Flexible classification, zero-shot |
| **ViT**  | ~350MB | Fast   | Very High | Precise object recognition         |
| **DETR** | ~170MB | Medium | High      | Object detection, localization     |

## 🛠️ Development

### API Endpoints

- `GET /` - API information and available models
- `POST /classify` - ViT image classification
- `POST /clip` - CLIP zero-shot classification
- `POST /detect` - DETR object detection
- `POST /clip-custom` - CLIP with custom prompts

### Project Structure

```
hf-vision-demo/
├── backend/
│   └── main.py          # FastAPI backend server
├── frontend/
│   └── index.html       # Web interface
├── requirements.txt     # Python dependencies
├── demo_script.py      # Demo and testing script
└── README.md           # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the amazing models and transformers library
- [OpenAI](https://openai.com/) for CLIP
- [Google](https://github.com/google-research/vision_transformer) for Vision Transformer
- [Facebook Research](https://github.com/facebookresearch/detr) for DETR

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting)
2. Look at existing [GitHub issues](https://github.com/juan-LARRAYA/huggin-face/issues)
3. Create a new issue with detailed information

---

**Made with ❤️ using the top 3 computer vision models from Hugging Face** 🤗
