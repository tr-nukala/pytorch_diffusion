# Model Files

This directory contains trained PyTorch model files.

## unet_denoiser.pth

- **Size**: ~7.5MB
- **Description**: Pre-trained U-Net model for MNIST denoising
- **Status**: Included for demo purposes

## Using the Pre-trained Model

The model is ready to use! You can:

1. **Run inference directly** using the existing model
2. **Train your own model** to see the process

To train a new model:

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