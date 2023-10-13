"""IMPORTANT: You must already have Python 3 to run this."""

import os
import sys

py = sys.executable
install = py + " -m pip install "
os.system(install + "--upgrade pip")
os.system(install + "astropy")

print("If this failed, then check https://www.astropy.org/ for details on how to install astropy.")
