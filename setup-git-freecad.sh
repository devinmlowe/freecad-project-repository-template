#!/bin/bash
# Setup Git for FreeCAD file version control using zippey

set -e

echo "Setting up Git for FreeCAD files..."

# Create src directory if it doesn't exist
mkdir -p ~/src/bitbucket.org/sippey

# Clone zippey if not already present
if [ ! -d ~/src/bitbucket.org/sippey/zippey ]; then
    echo "Cloning zippey..."
    git clone https://bitbucket.org/sippey/zippey.git ~/src/bitbucket.org/sippey/zippey
else
    echo "zippey already exists, updating..."
    cd ~/src/bitbucket.org/sippey/zippey
    git pull
fi

# Make zippey executable
chmod +x ~/src/bitbucket.org/sippey/zippey/zippey.py

# Configure global git settings
echo "Configuring Git..."

# Add zip diff settings
git config --global diff.zip.textconv "unzip -c -a"

# Add zippey filter settings  
git config --global filter.zippey.smudge "~/src/bitbucket.org/sippey/zippey/zippey.py d"
git config --global filter.zippey.clean "~/src/bitbucket.org/sippey/zippey/zippey.py e"

# Set global attributes file
git config --global core.attributesfile ~/.gitattributes

# Create/update global gitattributes
echo "Setting up global .gitattributes..."
grep -q "*.FCStd filter=zippey" ~/.gitattributes 2>/dev/null || cat >> ~/.gitattributes << 'EOF'

# FreeCAD files - use zippey for efficient storage and zip diff for viewing
*.FCStd filter=zippey
*.FCStd diff=zip
EOF

echo "✅ Git configured for FreeCAD files!"

# Test the setup
echo "Testing configuration..."
if git config --global filter.zippey.clean > /dev/null; then
    echo "✅ Zippey filter configured"
else
    echo "❌ Zippey filter failed"
fi

echo "Run this script on each machine where you'll use FreeCAD with Git."
echo "Use 'git diff' to see readable changes in .FCStd files."