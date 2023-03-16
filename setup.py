from setuptools import setup, find_packages


setup(
    name="my-ml-project",
    version="0.1.0",
    url="siddharthsah.com",
    author="siddharthksah",
    author_email="siddharth123sk@gmail.com",
    description="An end-to-end sample MLOps project",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here, e.g.:
        "pandas",
        "numpy",
        "scikit-learn",
        "flask",
        "mlflow",
    ],
    extras_require={
        "dev": [
            # Add any development dependencies here, e.g.:
            "pytest",
            "black",
        ],
    },
    entry_points={
        # Define any console scripts or entry points for your project
    },
    classifiers=[
        # Add any relevant classifiers, e.g.:
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)