#!/bin/bash

# remove unwanted VSCode extension(s)
sudo code --uninstall-extension eamodio.gitlens

# change default git config to ignore chmod changes and symbolic links
git config core.fileMode false

# change pull to alway rebase to eliminate common git error
git config pull.rebase true

# upgrade pip and install required packages
pip install --upgrade pip
pip install pytest
