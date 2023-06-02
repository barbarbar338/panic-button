import shutil
import subprocess

from format import format
from prebuild import prebuild


def build():
    prebuild()
    format()

    print("🚧 Building")

    subprocess.call(
        [
            "pyinstaller",
            "--onefile",
            "--noconsole",
            "--icon=assets/favicon.ico",
            "--name",
            "panic",
            "main.py",
        ]
    )

    print("📌 copying assets to dist")
    shutil.copytree("assets", "dist/assets")

    print("🎈 Build successfull")


if __name__ == "__main__":
    build()
