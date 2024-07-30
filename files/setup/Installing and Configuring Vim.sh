#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Vim Python IDE Setup Script

echo "Starting Vim Python IDE setup..."

# Create and enter temporary directory
mkdir -p ~/tmp_vim_setup
cd ~/tmp_vim_setup

# Install necessary tools and development packages
sudo dnf install -y w3m
sudo dnf group install -y "Development Tools"
sudo dnf install -y cmake python3-devel ncurses-devel

# Install additional development libraries
sudo dnf install -y gcc make ruby ruby-devel lua lua-devel luajit \
    luajit-devel ctags git python python-devel python3 python3-devel tcl-devel \
    perl perl-devel perl-ExtUtils-ParseXS perl-ExtUtils-XSpp perl-ExtUtils-CBuilder \
    perl-ExtUtils-Embed

# Clone Vim repository
git clone https://github.com/vim/vim.git
cd vim/src

# Clean any previous builds
make clean
make distclean

# Configure Vim build (without Perl support)
./configure --with-features=huge \
    --enable-multibyte \
    --enable-python3interp=yes \
    --with-python3-config-dir=$(python3-config --configdir) \
    --disable-perlinterp \
    --enable-luainterp=yes \
    --enable-cscope \
    --prefix=/usr/local

# Compile and install Vim
make
sudo make install

# Verify Python support in Vim
vim --version | grep python

# Set up the Python IDE environment
cd ../..
git clone https://github.com/jarolrod/vim-python-ide
cd vim-python-ide
bash setup.sh

echo "Vim Python IDE setup completed!"