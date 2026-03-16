import os

default_assets_root = os.path.join(os.path.dirname(__file__), "assets")

# Use the user-specified assets root (through environment variable) if available,
# otherwise use the default assets root
assets_root = os.getenv("ROBOCASA_ASSETS_ROOT", default_assets_root)
