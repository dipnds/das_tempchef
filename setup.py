from setuptools import setup, find_packages

setup(
    name="daschef",
    version="0.0.1",
    author="Deepan Das",
    author_email="dipn.ds@gmail.com",
    description="DataChef take home assignment",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "numpy", "sklearn", "pandas"],
    entry_points={"console_scripts": ["daschef = src.main:main"]},
)