#!/usr/bin/env python3

import os
import subprocess

folder = os.getcwd()

for file in os.listdir(folder):
    
    if file.startswith("p") and file.endswith(".py"):
        command = ["mypy", "--strict", file]
        print(f"I'm running: {' '.join(command)}")
        print("________________________________________________________________________________")
        subprocess.run(command)
        print()
