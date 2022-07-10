from setuptools import find_packages, setup


VERSION = "0.0.1"
IS_RELEASED = False
NAME = "tiff2pdf"


setup(
    name=NAME,
    version=VERSION,
    description="a small package for converting tiff images to python",
    url="https://github.com/cogentlabs/img_align.git",
    author="Ayan Sengupta",
    author_email="ayansengupta17@gmail.com",
    include_package_data=True,
    package_data={NAME: ["py.typed"]},
    packages=find_packages(),
    install_requires=["click==8.1.3", "pathlib==1.0.1", "Pillow==9.2.0", "tomli==2.0.1", "tqdm==4.64.0"],
    entry_points={
        "console_scripts": [
            "to-pdf=tiff2pdf.tiff2pdf:tiff_to_pdf",
        ],
    },
)
