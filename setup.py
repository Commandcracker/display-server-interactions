from setuptools import setup, find_packages
from os.path import dirname, join, abspath
# def read_requirements(file):
#    with open(file) as f:
#        return f.read().splitlines()


def read(rel_path: str) -> str:
    here = abspath(dirname(__file__))
    with open(join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


#requirements = read_requirements("requirements.txt")

def main() -> None:
    setup(
        name="dsi",
        version=get_version("dsi/__init__.py"),

        url="https://github.com/Commandcracker/dsi",

        documentation="https://dsi.readthedocs.io/en/latest/",

        description="DSI allows you to perform basic interactions on your display server, like screenshotting a window or sending input to it.",
        long_description_content_type="text/markdown",
        long_description=read("README.md"),

        py_modules=["dsi"],

        keywords=[
            "screen",
            "display",
            "screenshot",
            "input",
            "window",
            "screencapture",
            "screengrab",
        ],

        license="Apache Software License",
        packages=find_packages(exclude=["test"]),
        # install_requires=requirements,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            #"Operating System :: OS Independent",
        ]
    )


if __name__ == "__main__":
    main()
