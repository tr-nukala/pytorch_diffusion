# Model Files

This directory contains trained PyTorch model files.

## unet_denoiser.pth

- **Size**: ~7.5MB  
- **Description**: Pre-trained U-Net model for MNIST denoising
- **Status**: Available as GitHub Release asset (see Releases section)

## Getting the Pre-trained Model

**Option 1: Download from Releases (Recommended)**
1. Go to [Releases](https://github.com/tr-nukala/pytorch_diffusion/releases)
2. Download `unet_denoiser.pth` from the latest release
3. Place it in this `src/models/` directory

**Option 2: Train Your Own**
Run the notebook to train a fresh model:

1. Run the notebook: `notebooks/Diffusion_Demo_Clean.ipynb`
2. The training section will create a new `unet_denoiser.pth` file
3. Training time varies by device:
   - **Apple Silicon (MPS)**: ~2-3 minutes  
   - **NVIDIA GPU (CUDA)**: ~1-2 minutes
   - **CPU**: ~5-10 minutes

## Model Architecture

- U-Net with encoder-decoder structure
- Input: 28x28 grayscale images (MNIST)
- Output: Denoised 28x28 grayscale images
- Parameters: ~470K parameters

## Model Performance

This pre-trained model demonstrates:
- Fast denoising of MNIST digits
- Good reconstruction quality at low noise levels (t=10, t=30)
- Educational insight into diffusion model capabilities

*Note: This is a demonstration model optimized for learning, not production use.*