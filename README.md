# PyTorch Diffusion Demo

Toy diffusion model demo for PyTorch ATX meetup.
# PyTorch Diffusion Demo

A toy implementation of a denoising diffusion model using PyTorch, presented at the PyTorch ATX Meetup.

## 🧠 What This Is

This demo trains a small U-Net model to reverse the diffusion process on MNIST digits. It learns to reconstruct clean images (`x₀`) from noisy ones (`xₜ`) using a simplified forward and reverse process.

![Denoising Progression](outputs/denoised_progression_padded.png)

## 🚀 Features

- Simple PyTorch implementation (under 150 lines)
- Predicts `x₀` directly instead of noise
- Uses log-distributed timestep sampling
- Visualizes denoising at various noise levels (t=10, 30, 50)

## 🛠 How to Run

```bash
git clone https://github.com/yourusername/pytorch_diffusion_demo.git
cd pytorch_diffusion_demo
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
jupyter lab
```

Open `notebooks/Diffusion_Demo.ipynb` and run the cells step-by-step.

## 🖼 Output Example

The model reconstructs clean digits from various levels of noise:

| Original | t=10 | t=30 | t=50 |
|----------|------|------|------|
| ✅ | ✅ | 🤔 | 😬 |

## 🧪 Credits

Inspired by DDPMs and the educational implementations of denoising diffusion by Hugging Face and annotated notebooks by Phil Wang and Lilian Weng.

---

Demo built with ❤️ by Tarun Reddy Nukala · [@ntreddy](https://github.com/ntreddy)