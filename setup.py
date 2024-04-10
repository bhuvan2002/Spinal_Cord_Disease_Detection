from csv import __version__
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__=="0.0.0"

REPO_NAME = "Spinal_Cord_Disease_Detection"
AUTHOR_USER_NAME = "bhuvan2002"
SRC_REPO = "Spinal_Cord_disease_detection"
AUTHOR_EMAIL = "bhuvanumesh123@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=("A deep learning model for the detection of spinal cord disease from MRI scans."),
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/@{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where="src"),
)