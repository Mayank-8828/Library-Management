from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in library_management/__init__.py
with open("library_management/__init__.py") as f:
    exec(f.read())

setup(
    name="library_management",
    version=__version__,
    description="Library Management System",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)