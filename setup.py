from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

extras = {
    "quality": ["black", "flake8", "isort"],
}

extras["dev"] = extras["quality"]

setup(
    name="edge_camera",
    version="0.0.0",
    author="Ben Cunningham",
    author_email="benjamescunningham@gmail.com",
    description="Streaming and object detection on an edge device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benjcunningham/edge-camera",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[],
    extras_require=extras,
    python_requires=">=3.8.0",
)
