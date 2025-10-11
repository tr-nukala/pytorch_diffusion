#!/usr/bin/env python3
"""
Download pre-trained model from GitHub Releases
Cross-platform alternative to download_model.sh
"""

import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

def download_model():
    """Download the pre-trained U-Net model from GitHub Releases."""
    
    MODEL_FILE = Path("src/models/unet_denoiser.pth")
    RELEASE_URL = "https://github.com/tr-nukala/pytorch_diffusion/releases/latest/download/unet_denoiser.pth"
    
    print("🤖 Downloading pre-trained U-Net model...")
    
    # Check if model already exists
    if MODEL_FILE.exists():
        print(f"⚠️  Model file already exists at {MODEL_FILE}")
        response = input("Do you want to overwrite it? (y/N): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Download cancelled.")
            return False
    
    # Create models directory if it doesn't exist
    MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        print("📥 Downloading...")
        
        def progress_hook(block_num, block_size, total_size):
            """Show download progress."""
            if total_size > 0:
                percent = min(100, (block_num * block_size * 100) // total_size)
                print(f"\rProgress: {percent:3d}% ({block_num * block_size:,} / {total_size:,} bytes)", end='')
        
        urllib.request.urlretrieve(RELEASE_URL, MODEL_FILE, progress_hook)
        print()  # New line after progress
        
        # Verify download
        if MODEL_FILE.exists():
            file_size = MODEL_FILE.stat().st_size
            print("✅ Model downloaded successfully!")
            print(f"   File: {MODEL_FILE}")
            print(f"   Size: {file_size:,} bytes (~7.5MB expected)")
            print("")
            print("🚀 You can now run the notebook and use the pre-trained model!")
            return True
        else:
            print("❌ Download failed. File not found after download.")
            return False
            
    except urllib.error.URLError as e:
        print(f"\n❌ Download failed: {e}")
        print("\nAlternatives:")
        print(f"1. Manual download from: {RELEASE_URL}")
        print("2. Train your own model using the notebook")
        return False
    except KeyboardInterrupt:
        print("\n⏹️  Download cancelled by user.")
        if MODEL_FILE.exists():
            MODEL_FILE.unlink()  # Remove partial file
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False

def main():
    """Main function."""
    print("PyTorch Diffusion Demo - Model Downloader")
    print("=" * 45)
    
    success = download_model()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()