import subprocess


def format():
    print("Formatting files")

    subprocess.call(["python", "-m" "black", "."])


if __name__ == "__main__":
    format()
