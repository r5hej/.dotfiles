#!/usr/bin/env python3
import os
import paths
import shutil
import subprocess

"""
Install vim with plugins

For ubuntu, the following packages are needed:
    exuberant-ctags
    build-essentials
    python-dev
    python3-dev
    cmake
"""

home_path = os.path.expanduser("~")
git_path = home_path + "/.dotfiles"
os.chdir(git_path)
subprocess.call(["git", "pull"])


os.chdir(home_path)
for path in paths.vim_dirs:
    if (not os.path.exists(path)):
        os.mkdir(path)# exist_ok=True)

os.chdir(git_path)
for path in paths.vim_files:
    shutil.copyfile(path, home_path + "/" + path)

for tree in paths.vim_trees:
    if os.path.exists(home_path + "/" + tree):
        shutil.rmtree(home_path + "/" + tree)

    print(os.getcwd())
    shutil.copytree(tree, home_path + "/" + tree)

os.chdir(home_path)
subprocess.call(["vim", "+PluginInstall", "+qall"])
os.chdir(home_path + "/.vim/bundle/YouCompleteMe")
subprocess.call(["./install.py"])

print("############################")
print("#  vim has been installed  #")
print("############################")
