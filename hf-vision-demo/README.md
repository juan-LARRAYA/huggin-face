# 🤖 HF Vision Demo - Los 3 Modelos Más Populares

Demo interactivo que ejecuta los 3 modelos de visión artificial más descargados de Hugging Face usando tu cámara web en tiempo real.

## 🎯 Modelos Incluidos

### 1. **CLIP** (openai/clip-vit-base-patch32)

- **Qué hace**: Clasificación zero-shot usando texto y imágenes
- **Capacidades**: Puede clasificar imágenes usando descripciones en lenguaje natural
- **Ejemplo**: "una foto de un gato", "una persona corriendo", "comida italiana"

### 2. **ViT** (google/vit-base-patch16-224)

- **Qué hace**: Clasificación de imágenes usando Vision Transformer
- **Capacidades**: Clasifica imágenes en 1000 categorías de ImageNet
- **Ejemplo**: Identifica objetos específicos como "Golden Retriever", "laptop", "pizza"

### 3. **DETR** (facebook/detr-resnet-50)

- **Qué hace**: Detección de objetos usando Detection Transformer
- **Capacidades**: Detecta y localiza múltiples objetos en una imagen con cajas delimitadoras
- **Ejemplo**: Encuentra personas, carros, animales y dibuja cajas alrededor de ellos

## 🚀 Instalación y Uso

### Requisitos

- Python 3.9+
- Cámara web
- 4GB+ RAM (los modelos son grandes)

### Pasos

1. **Crear entorno virtual**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

2. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el backend**:

   ```bash
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Abrir el frontend**:
   - Abre `frontend/index.html` en tu navegador
   - O sirve con un servidor local: `python -m http.server 3000`

## 🎮 Cómo Usar

1. **Permite acceso a la cámara** cuando el navegador lo solicite
2. **Prueba cada modelo**:

   - 🔍 **ViT Classifier**: Clasifica lo que ve la cámara
   - 🎯 **CLIP Zero-Shot**: Clasifica usando categorías predefinidas
   - 📦 **DETR Object Detection**: Detecta y marca objetos con cajas
   - 🎨 **CLIP Custom**: Usa tus propios prompts de texto

3. **Para CLIP Custom**: Escribe prompts separados por comas como:
   ```
   una persona feliz, un animal, tecnología, comida deliciosa
   ```

## 📊 Características

- **Interfaz moderna** con gradientes y efectos visuales
- **Tiempo real** usando tu cámara web
- **Visualización interactiva** de detecciones con cajas de colores
- **Resultados ordenados** por confianza
- **Responsive design** que se adapta a diferentes pantallas

## 🔧 Notas Técnicas

- **Primera ejecución**: Los modelos se descargan automáticamente (puede tomar varios minutos)
- **Tamaño de modelos**: ~1-2GB total de descarga
- **GPU**: Se detecta automáticamente si está disponible
- **Memoria**: Recomendado 8GB+ RAM para mejor rendimiento

## 🐛 Solución de Problemas

- **Error de cámara**: Verifica permisos del navegador
- **Modelos lentos**: Considera usar GPU o reducir resolución
- **Error de memoria**: Cierra otras aplicaciones o usa una máquina con más RAM
