import pygame
import importlib.util
import sys

name = "pygame"

if name in sys.modules:
    print(f"package {name!s} is already installed")
else:
    print("package has not yet been installed")