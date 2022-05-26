from setup import get_version
from os import system

# https://github.com/bast/pypi-howto


def printB(string: str) -> str:
    print("\033[34m" + string + "\033[0m")


def printG(string: str) -> str:
    print("\033[32m" + string + "\033[0m")


def exitR(string: str) -> None:
    exit("\033[31m" + string + "\033[0m")


def main() -> None:
    printG("Getting version...")
    version = get_version("dsi/__init__.py")
    printB("Version: " + version)

    printG("Building DSI...")
    exit_code = system("python setup.py bdist_wheel sdist")
    if exit_code != 0:
        exitR("Failed to build DSI.")

    printG("Installing DSI...")
    exit_code = system("pip install -e .")
    if exit_code != 0:
        exitR("Failed to install DSI.")

    printG("Uploading DSI to PyPI...")
    exit_code = system("twine upload dist/* -r pypitest")
    if exit_code != 0:
        exitR("Failed to upload DSI to PyPI.")


if __name__ == "__main__":
    main()
