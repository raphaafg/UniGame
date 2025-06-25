from cx_Freeze import setup, Executable
import os

# Read all asset list to include on .exe
path = "./asset"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

# cx_Freeze code
executables = [
    Executable(
        "main.py",
        icon="asset/icon.png"  # Set your icon here
    )
]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="SpaceShooter",
    version="1.0",
    description="Space Shooter app",
    options={"build_exe": files},
    executables=executables
)
