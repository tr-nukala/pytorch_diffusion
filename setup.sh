#!/bin/bash
# Setup script for PyTorch Diffusion Demo

set -e  # Exit on any error

echo "🚀 Setting up PyTorch Diffusion Demo..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+' | head -1)
echo "✅ Python version: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "📦 Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Check if Jupyter is accessible
echo "🧪 Testing Jupyter installation..."
jupyter --version

echo ""
echo "✅ Setup complete!"
echo ""
echo "To get started:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Launch Jupyter: jupyter lab"
echo "3. Open: notebooks/Diffusion_Demo_Clean.ipynb"
echo ""
echo "🎉 Happy diffusing!"