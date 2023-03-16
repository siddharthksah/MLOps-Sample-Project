from setuptools import setup, find_packages


test_deps = [
    "pytest>=6.2.3",
    "pytest-flask>=1.2.0",
    "pip>=21.0.1",
    "flake8>=3.9.2",
    "flake8-annotations>=2.6.2",
    "pytest-cov>=2.12.1",
    "black>=21.7b0"
]

serve_deps = [
    "dploy-kickstart>=0.1.5",
]

extras = {"test": test_deps, "serve": serve_deps}

setup(
    name="mlops-sample-project",
    version="0.1.0",
    url="siddharthsah.com",
    author="siddharthksah",
    author_email="siddharth123sk@gmail.com",
    description="An end-to-end sample MLOps project",
    packages=find_packages(),
    install_requires=["pandas>=1.3.2", "scikit-learn>=0.24.2"],
    tests_require=test_deps,
    extras_require=extras,
)
