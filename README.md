# 🧨 PyTorch Diffusion Demo

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.13+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal implementation of a denoising diffusion model using PyTorch, presented at the PyTorch ATX Meetup. This educational demo shows how a simple U-Net can learn to reverse the diffusion process on MNIST digits.

**Built on Apple Silicon** with automatic device detection (MPS → CUDA → CPU).

![Denoising Progression](src/outputs/denoised_progression_padded.png)

## 🧠 What This Is

This demo implements a **simplified diffusion model** that:
- Trains a U-Net to predict clean images (`x₀`) directly from noisy inputs (`xₜ`)
- Uses a linear noise schedule over T timesteps
- Demonstrates the core concept of diffusion models in under 150 lines of code

Unlike full DDPM implementations, this version predicts the clean image directly rather than the noise, making it easier to understand and visualize.

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
git clone https://github.com/tr-nukala/pytorch_diffusion_demo.git
cd pytorch_diffusion_demo
./setup.sh
```

The setup script will create a virtual environment, install dependencies, and verify everything works.

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tr-nukala/pytorch_diffusion_demo.git
   cd pytorch_diffusion_demo
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

```bash
# Activate environment (if not already active)
source venv/bin/activate

# Launch Jupyter
jupyter lab
```

Open `notebooks/Diffusion_Demo_Clean.ipynb` and run the cells step-by-step.

## 🗂️  Project Structure

```
pytorch_diffusion_demo/
├── README.md                              # This file
├── LICENSE                                # MIT license
├── requirements.txt                       # Python dependencies
├── setup.sh                               # Quick setup script
├── .gitignore                             # Git ignore rules
├── notebooks/
│   └── Diffusion_Demo_Clean.ipynb         # Main interactive demo
└── src/
    ├── diffusion.py                       # Core diffusion functions
    ├── model.py                           # U-Net architecture
    ├── outputs/                           # Generated sample images
    └── models/                            # Model files (excluded from git)
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
git clone https://github.com/tr-nukala/pytorch_diffusion_demo.git
cd pytorch_diffusion_demo/src
jupyter notebook Diffusion_Demo_Clean.ipynb
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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ 🦾 by [Tarun Reddy Nukala](https://github.com/tr-nukala)**  
*Presented at PyTorch ATX Meetup, 2025*