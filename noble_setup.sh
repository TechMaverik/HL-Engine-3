#!/bin/bash

echo "===== HL Engine 3 Setup ====="

# Check if python3.10 exists
if command -v python3.10 &> /dev/null
then
    echo "Python 3.10 already installed."
else
    echo "Python 3.10 not found. Installing from source..."

    sudo apt update

    # Install build dependencies
    sudo apt install -y \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libncurses5-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libgdbm-dev \
        libdb5.3-dev \
        libbz2-dev \
        libexpat1-dev \
        liblzma-dev \
        tk-dev \
        wget \
        curl \
        llvm \
        libffi-dev

    cd /tmp || exit

    wget https://www.python.org/ftp/python/3.10.14/Python-3.10.14.tgz
    tar -xf Python-3.10.14.tgz

    cd Python-3.10.14 || exit

    ./configure --enable-optimizations
    make -j$(nproc)

    sudo make altinstall

    echo "Python 3.10 installed."
fi

# Verify installation
if command -v python3.10 &> /dev/null
then
    python3.10 --version

    echo "Installing pip..."
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

    echo "Installing project dependencies..."
    python3.10 -m pip install -r requirements.txt

    echo "Cloning Unitree SDK..."
    git clone https://github.com/unitreerobotics/unitree_sdk2_python.git

    cd unitree_sdk2_python || exit

    python3.10 -m pip install -e .

    cd ..

    echo "===== HL Engine 3 Setup Completed Successfully ====="
else
    echo "Python 3.10 installation failed."
    exit 1
fi