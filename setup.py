from setuptools import setup
import re


with open("README.rst", "r") as f:
    long_description = f.read()


with open("tf2_sku/__init__.py") as f:
    version = re.search(
        r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE).group(1)


setup(
    name="tf2_sku",
    version=version,
    author="offish",
    author_email="overutilization@gmail.com",
    description="Format TF2 items as strings or objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/offish/tf2_sku",
    download_url="https://github.com/offish/tf2_sku/tarball/v" + version,
    packages=["tf2_sku"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
