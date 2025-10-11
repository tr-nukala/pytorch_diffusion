# Model Files

This directory contains trained PyTorch model files.

## unet_denoiser.pth

- **Size**: ~7.5MB
- **Description**: Pre-trained U-Net model for MNIST denoising
- **Status**: Excluded from git (see .gitignore)

## Training Your Own Model

The model file is excluded from version control due to its size. To train your own model:

1. Run the notebook: `notebooks/Diffusion_Demo_Clean.ipynb`
2. The training section will create a new `unet_denoiser.pth` file
3. Training takes approximately 5-10 minutes on a modern CPU

## Model Architecture

- U-Net with encoder-decoder structure
- Input: 28x28 grayscale images (MNIST)
- Output: Denoised 28x28 grayscale images
- Parameters: ~470K parameters

## Alternative: Download Pre-trained Model

If you prefer to use the pre-trained model without training:

```bash
# This would be a download script if the model were hosted externally
# wget https://example.com/models/unet_denoiser.pth
```

*Note: Currently, you'll need to train the model yourself using the notebook.*