from setup import get_version
from os import system
import subprocess
import hashlib
from os.path import basename, dirname, join


def printB(string: str) -> str:
    print("\033[34m" + string + "\033[0m")


def printG(string: str) -> str:
    print("\033[32m" + string + "\033[0m")


def exitR(string: str) -> None:
    exit("\033[31m" + string + "\033[0m")


def check_returncode(*popenargs) -> int:
    try:
        return subprocess.run(
            *popenargs,
            stderr=subprocess.STDOUT,
            stdout=subprocess.DEVNULL
        ).returncode
    except Exception:
        return 1


def check_requirements() -> None:
    exit_code = check_returncode("pip")
    if exit_code != 0:
        exitR("Please install pip by running\n`curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py`\n and `python get-pip.py`.")

    exit_code = check_returncode(["twine", "--version"])
    if exit_code != 0:
        exitR("Please install twine by running `pip install twine`.")

    exit_code = check_returncode(["git", "--version"])
    if exit_code != 0:
        exitR("Please install git (https://git-scm.com/downloads).")

    exit_code = check_returncode("gh")
    if exit_code != 0:
        exitR("Please install GitHub CLI (https://cli.github.com/manual/installation)\nand dont forget to run `gh auth login`.")


def gen_SUMS_files(files: list) -> None:
    # create temp dir and put md5SUMS file there

    dir = dirname(files[0])
    md5SUMS = open(join(dir, "md5SUMS"), "w")
    sha256SUMS = open(join(dir, "sha256SUMS"), "w")
    BLAKE2_256SUMS = open(join(dir, "BLAKE2_256SUMS"), "w")

    for file in files:
        file_content = open(file, "rb").read()
        name = basename(file)

        md5 = hashlib.md5(file_content).hexdigest()
        md5SUMS.write(f"{md5} {name}\n")

        sha256 = hashlib.sha256(file_content).hexdigest()
        sha256SUMS.write(f"{sha256} {name}\n")

        BLAKE2_256 = hashlib.blake2b(file_content, digest_size=32).hexdigest()
        BLAKE2_256SUMS.write(f"{BLAKE2_256} {name}\n")


def main() -> None:
    check_requirements()

    printG("Getting version...")
    version = get_version("display_server_interactions/__init__.py")
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
    # for testing add " -r pypitest"
    exit_code = system(f"twine upload dist/*{version}*")
    if exit_code != 0:
        exitR("Failed to upload DSI to PyPI.")

    printG("Creating git Tag...")
    exit_code = system(f"git tag {version}")
    if exit_code != 0:
        exitR("Failed to create git tag.")

    printG("Pushing git Tag...")
    exit_code = system("git push origin --tags")
    if exit_code != 0:
        exitR("Failed to push git tag.")

    printG("Generating SUMS files...")
    gen_SUMS_files([
        f"dist/display-server-interactions-{version}.tar.gz",
        f"dist/display_server_interactions-{version}-py3-none-any.whl"
    ])

    printG("Creating GitHub Release...")
    exit_code = system(
        f"gh release create {version} dist/*-{version}* dist/md5SUMS dist/sha256SUMS dist/BLAKE2_256SUMS --generate-notes")
    if exit_code != 0:
        exitR("Failed to create GitHub Release.")


if __name__ == "__main__":
    main()
