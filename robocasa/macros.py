"""
Macro settings that can be imported and toggled. Internally, specific parts of the codebase rely on these settings
for determining core functionality.

To make sure global reference is maintained, should import these settings as:

`import robocasa.macros as macros`
"""

import os

SHOW_SITES = os.getenv("ROBOCASA_SHOW_SITES", False)

# whether to print debugging information
VERBOSE = os.getenv("ROBOCASA_VERBOSE", False)

# Spacemouse settings. Used by SpaceMouse class in robosuite/devices/spacemouse.py
SPACEMOUSE_VENDOR_ID = os.getenv("ROBOCASA_SPACEMOUSE_VENDOR_ID", 9583)
SPACEMOUSE_PRODUCT_ID = os.getenv("ROBOCASA_SPACEMOUSE_PRODUCT_ID", 50741)

DATASET_BASE_PATH = os.getenv("ROBOCASA_DATASET_BASE_PATH")