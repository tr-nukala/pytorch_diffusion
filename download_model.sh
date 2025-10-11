#!/bin/bash
# Download pre-trained model from GitHub Releases

set -e  # Exit on any error

MODEL_FILE="src/models/unet_denoiser.pth"
RELEASE_URL="https://github.com/tr-nukala/pytorch_diffusion/releases/latest/download/unet_denoiser.pth"

echo "🤖 Downloading pre-trained U-Net model..."

# Check if model already exists
if [ -f "$MODEL_FILE" ]; then
    echo "⚠️  Model file already exists at $MODEL_FILE"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Download cancelled."
        exit 0
    fi
fi

# Create models directory if it doesn't exist
mkdir -p "$(dirname "$MODEL_FILE")"

# Download the model
if command -v curl >/dev/null 2>&1; then
    echo "📥 Downloading with curl..."
    curl -L -o "$MODEL_FILE" "$RELEASE_URL"
elif command -v wget >/dev/null 2>&1; then
    echo "📥 Downloading with wget..."
    wget -O "$MODEL_FILE" "$RELEASE_URL"
else
    echo "❌ Error: Neither curl nor wget found."
    echo "Please install curl or wget, or download manually from:"
    echo "   $RELEASE_URL"
    exit 1
fi

# Verify download
if [ -f "$MODEL_FILE" ]; then
    file_size=$(wc -c < "$MODEL_FILE" | tr -d ' ')
    echo "✅ Model downloaded successfully!"
    echo "   File: $MODEL_FILE"
    echo "   Size: $file_size bytes (~7.5MB expected)"
    echo ""
    echo "🚀 You can now run the notebook and use the pre-trained model!"
else
    echo "❌ Download failed. Please try again or download manually."
    exit 1
fi