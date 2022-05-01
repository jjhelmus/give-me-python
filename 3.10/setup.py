import shutil

from setuptools import setup, find_packages

# copy the interpreter from the manylinux image into the package data dir
src = "/opt/python/cp310-cp310/"
dst = "./src/give_me_python/data"
shutil.copytree(src, dst)

setup(
    name="give-me-python",
    version="3.10.4",
    description="CPython installable via pip",
    url="https://github.com/jjhelmus/give-me-python",
    author="Jonathan Helmus",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    include_package_data = True,
    entry_points={
            "console_scripts": [
                "gm-python3.10=give_me_python:python3",
            ]
    }
)
