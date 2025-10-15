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

- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Webcam** (built-in or external)
- **Internet connection** (for initial model download)

### 🌐 Live Demo

**Deployed on Vercel:** [https://hf-vision-demo.vercel.app](https://hf-vision-demo.vercel.app)

No installation required! Just visit the link and start using AI models directly in your browser.

### Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/juan-LARRAYA/huggin-face.git
   cd huggin-face/hf-vision-demo
   ```

2. **Start a local server**:

   ```bash
   # Using Python
   python -m http.server 8080

   # Or using Node.js
   npx serve .

   # Or using any other static server
   ```

3. **Access the application**:
   - Open your browser and go to `http://localhost:8080`
   - Allow camera access when prompted
   - Wait for models to load (first time may take a few minutes)
   - Click any model button to see real-time AI inference!

### First Run

⚠️ **Important**: The first execution will download the models (~500MB total) directly to your browser. This may take a few minutes depending on your internet connection. Models are cached locally for subsequent visits.

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
┌─────────────────────────────────────────────────────────────┐
│                    Client-Side Browser                      │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │   Frontend      │    │ Transformers.js │                │
│  │   (HTML/JS)     │◄──►│   AI Models     │                │
│  │                 │    │                 │                │
│  │ • Camera feed   │    │ • CLIP          │                │
│  │ • UI controls   │    │ • ViT           │                │
│  │ • Visualization │    │ • DETR          │                │
│  └─────────────────┘    └─────────────────┘                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Technical Details

- **Client-side AI**: All models run directly in your browser using Transformers.js
- **Model loading**: Automatic download on first run (~500MB total)
- **WebAssembly**: Optimized inference using WASM and WebGL acceleration
- **Memory usage**: 2-4GB RAM depending on models loaded
- **Performance**: ~2-5 seconds per inference depending on device
- **Supported formats**: JPEG, PNG images from webcam
- **Privacy**: All processing happens locally - no data sent to servers

## 🐛 Troubleshooting

### Common Issues

| Problem                   | Solution                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------- |
| 🎥 **Camera not working** | • Check browser permissions<br>• Try a different browser<br>• Ensure camera isn't used by other apps |
| 🐌 **Slow inference**     | • First run downloads models (normal)<br>• Close other browser tabs<br>• Use a modern device         |
| 💾 **Out of memory**      | • Close other browser tabs<br>• Use a device with more RAM<br>• Refresh the page                     |
| 🌐 **Models won't load**  | • Check internet connection<br>• Clear browser cache<br>• Try a different browser                    |
| 📦 **CORS errors**        | • Use HTTPS or localhost<br>• Don't open HTML file directly<br>• Use a local server                  |

### Performance Tips

- **Browser Choice**: Chrome and Firefox typically perform best with WebAssembly
- **Memory Management**: Close unnecessary browser tabs before running
- **Device**: Modern devices with more RAM will perform better
- **Network**: Stable internet connection required for first-time model downloads
- **HTTPS**: Use HTTPS for better performance and security features

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

### Client-Side Architecture

This application runs entirely in the browser using:

- **Transformers.js** - Client-side AI inference
- **WebAssembly** - High-performance computation
- **WebGL** - GPU acceleration when available
- **Web Workers** - Non-blocking model execution

### Project Structure

```
hf-vision-demo/
├── index.html           # Main application (client-side)
├── vercel.json         # Vercel deployment configuration
├── package.json        # Project metadata
├── backend/            # Legacy server-side code (deprecated)
├── frontend/           # Legacy frontend (deprecated)
└── README.md           # This file
```

### 🚀 Deployment

#### Deploy to Vercel

1. **Fork this repository**
2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Import your forked repository
   - Deploy automatically!

#### Deploy to Netlify

1. **Fork this repository**
2. **Connect to Netlify**:
   - Go to [netlify.com](https://netlify.com)
   - Drag and drop the `hf-vision-demo` folder
   - Deploy instantly!

#### Deploy to GitHub Pages

1. **Enable GitHub Pages** in repository settings
2. **Select source**: Deploy from main branch
3. **Access**: `https://yourusername.github.io/huggin-face/hf-vision-demo/`

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
- [Transformers.js](https://huggingface.co/docs/transformers.js) for enabling client-side AI inference
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
