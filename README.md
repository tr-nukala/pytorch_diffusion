# 🧨 PyTorch Diffusion Model Demo | Denoising Diffusion Probabilistic Models (DDPM) Tutorial

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.13+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-MPS%20Optimized-green.svg)](https://pytorch.org/docs/stable/notes/mps.html)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](notebooks/Diffusion_Demo_Clean.ipynb)

A **minimal implementation of denoising diffusion probabilistic models (DDPM)** using PyTorch and U-Net architecture. This educational repository demonstrates how generative AI diffusion models work by training a simple neural network to reverse noise corruption on MNIST handwritten digits.

**Perfect for learning**: Understand diffusion models, generative AI, and PyTorch through a complete working example with interactive Jupyter notebooks.

**Optimized for Apple Silicon** with automatic device detection (MPS → CUDA → CPU) and cross-platform compatibility.

## 🎯 **Keywords**: Deep Learning, Generative AI, Computer Vision, Machine Learning Tutorial, PyTorch Tutorial, Diffusion Models, U-Net, MNIST, Apple Silicon, MPS Acceleration

![Denoising Progression](src/outputs/denoised_progression_padded.png)

## 🧠 What This Is

This repository provides a **complete educational journey into diffusion models** and generative AI:

### 📚 **Learn Diffusion Models From Scratch**
- **Simplified DDPM Implementation**: U-Net architecture that predicts clean images (`x₀`) directly from noisy inputs (`xₜ`)
- **Mathematical Foundation**: Linear noise schedule over T timesteps with clear mathematical explanations
- **Code Walkthrough**: Under 150 lines of well-commented PyTorch code showing core diffusion concepts
- **Interactive Learning**: Jupyter notebooks with step-by-step explanations and visualizations

### 🎓 **Perfect for Students & Researchers**
- **Computer Vision**: Understand how generative models work in image processing
- **Deep Learning**: See U-Net architecture applied to generative tasks
- **PyTorch Tutorial**: Learn modern PyTorch patterns with MPS/CUDA optimization
- **Machine Learning Research**: Use as foundation for your own diffusion experiments

Unlike complex DDPM implementations, this version predicts clean images directly rather than noise, making the mathematical concepts more intuitive and easier to visualize.

## 🚀 Features

- **Simple & Educational**: Clean PyTorch implementation focused on learning
- **Direct x₀ Prediction**: Predicts clean images instead of noise for easier interpretation  
- **Interactive Notebook**: Step-by-step Jupyter notebook with explanations
- **Cross-Platform**: Optimized for Apple Silicon (MPS), with CUDA and CPU fallbacks
- **Visualization**: Shows denoising progression at different noise levels
- **Fast Training**: Trains quickly on MNIST (~2-3 mins on Apple Silicon)

## 📋 Requirements

- Python 3.8 or higher
- PyTorch 1.13+ (supports Apple Silicon MPS, CUDA, or CPU)
- 4GB+ RAM recommended (8GB+ for Apple Silicon recommended)
- Jupyter Notebook for interactive demo

## 🛠 Installation & Setup

### Option 1: Quick Setup (Recommended)

```bash
git clone https://github.com/tr-nukala/pytorch_diffusion.git
cd pytorch_diffusion
./setup.sh
```

The setup script will create a virtual environment, install dependencies, and verify everything works.

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tr-nukala/pytorch_diffusion.git
   cd pytorch_diffusion
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Demo

**Option 1: Use Pre-trained Model (Quick Start)**

Choose your preferred download method:

**A) Automated Script (macOS/Linux)**
```bash
./download_model.sh
```

**B) Python Script (Cross-platform)**
```bash
python download_model.py
```

**C) Manual Download**
1. Go to [Releases](https://github.com/tr-nukala/pytorch_diffusion/releases/latest)
2. Download `unet_denoiser.pth` 
3. Place it in `src/models/unet_denoiser.pth`

**E) Command Line (curl)**
```bash
curl -L -o src/models/unet_denoiser.pth \
  https://github.com/tr-nukala/pytorch_diffusion/releases/latest/download/unet_denoiser.pth
```

**F) Command Line (wget)**
```bash
wget -O src/models/unet_denoiser.pth \
  https://github.com/tr-nukala/pytorch_diffusion/releases/latest/download/unet_denoiser.pth
```

**G) Python One-liner (cross-platform)**
```python
import urllib.request
import os

os.makedirs("src/models", exist_ok=True)
url = "https://github.com/tr-nukala/pytorch_diffusion/releases/latest/download/unet_denoiser.pth"
urllib.request.urlretrieve(url, "src/models/unet_denoiser.pth")
print("✅ Model downloaded!")
```

Then launch Jupyter:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
jupyter lab
```

**Option 2: Train Your Own Model**
```bash
# Skip the download, train from scratch in the notebook
source venv/bin/activate  # On Windows: venv\Scripts\activate  
jupyter lab
```

Open `notebooks/Diffusion_Demo_Clean.ipynb` and run the cells step-by-step.

## 🗂️  Project Structure

```
pytorch_diffusion/
├── README.md                              # This file  
├── LICENSE                                # MIT license
├── requirements.txt                       # Python dependencies
├── setup.sh                               # Quick setup script
├── download_model.sh                      # Download pre-trained model (bash)
├── download_model.py                      # Download pre-trained model (python)
├── .gitignore                             # Git ignore rules
├── notebooks/
│   └── Diffusion_Demo_Clean.ipynb         # Main interactive demo
└── src/
    ├── diffusion.py                       # Core diffusion functions
    ├── model.py                           # U-Net architecture  
    ├── outputs/                           # Generated sample images
    └── models/                            # Model files (download from Releases)
        └── README.md                      # Model documentation
```

## 🖼 Example Output

The trained model can reconstruct MNIST digits from various noise levels:

| Noise Level | Quality | Description |
|-------------|---------|-------------|
| t=10 | ✅ Excellent | Very clean reconstruction |
| t=30 | ✅ Good | Minor artifacts |  
| t=50 | 🤔 Fair | More noise, still recognizable |

## 🎓 Educational Notes

This implementation makes several simplifications for learning purposes:

- **Linear noise schedule** instead of cosine
- **Direct x₀ prediction** instead of ε-prediction  
- **Simple U-Net** without attention mechanisms
- **Fixed timestep sampling** for demonstration

For production use, consider more advanced techniques like DDIM, classifier-free guidance, or modern architectures.

## 🚀 Quick Start (Alternative)

If you just want to see it work:

```bash
# Install PyTorch first
pip install torch torchvision matplotlib numpy jupyter

# Clone and run
git clone https://github.com/tr-nukala/pytorch_diffusion.git
cd pytorch_diffusion

# Download model (choose one method)
python download_model.py              # Cross-platform
# OR: ./download_model.sh             # macOS/Linux only  
# OR: Manual download from Releases

# Launch notebook
jupyter lab notebooks/Diffusion_Demo_Clean.ipynb
```

## 🐛 Troubleshooting

**Common Issues:**

- **ImportError**: Make sure you're in the activated virtual environment
- **Device errors**: The code automatically detects MPS (Apple Silicon) → CUDA → CPU
- **Memory issues**: Reduce batch size in the notebook if needed  
- **Slow training**: 
  - **Apple Silicon**: ~2-3 minutes with MPS acceleration
  - **CUDA GPU**: ~1-2 minutes  
  - **CPU only**: ~5-10 minutes (still very doable!)

## 🤝 Contributing

This is an educational demo, but improvements are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable  
5. Submit a pull request

## 📚 References & Credits

- **DDPM Paper**: [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
- **Educational Resources**: Hugging Face diffusion course, Phil Wang's implementations
- **U-Net Architecture**: Based on the original U-Net for biomedical image segmentation

## 🏷️ Topics & Keywords

**Primary**: `pytorch` `diffusion-models` `machine-learning` `deep-learning` `generative-ai` `unet` `mnist` `denoising` `computer-vision` `tutorial`

**Technical**: `apple-silicon` `mps-acceleration` `jupyter-notebook` `educational` `ddpm` `generative-models` `pytorch-tutorial` `ai-demo`

**Research**: `denoising-diffusion` `probabilistic-models` `generative-artificial-intelligence` `neural-networks` `image-generation`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star This Repository!

If you found this PyTorch diffusion tutorial helpful for learning generative AI and diffusion models, please ⭐ star this repository to help others discover it!

## 📢 Share & Contribute

- **Share**: Help others learn diffusion models by sharing this repository
- **Issues**: Report bugs or request features via GitHub Issues
- **Contributions**: Pull requests welcome for improvements and educational enhancements
- **Discussions**: Use GitHub Discussions for questions about diffusion models and PyTorch

---

**Built with ❤️ for the PyTorch & AI community by [Tarun Reddy Nukala](https://github.com/tr-nukala)**  
*Educational Diffusion Models Tutorial | PyTorch ATX Meetup 2025*

### Related Repositories & Tutorials
**Generative AI** • **PyTorch Tutorials** • **Computer Vision** • **Machine Learning Education** • **Diffusion Models** • **Apple Silicon Optimization**