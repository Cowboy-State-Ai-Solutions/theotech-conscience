"""
TheoTech Neural Conscience System
=================================

A revolutionary AI safety system implementing Divine Anxiety and Moral Scar Tissue
mechanisms for permanent ethical boundaries in AI systems.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Core requirements
install_requires = read_requirements("requirements.txt")

# Development requirements
dev_requires = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pytest-benchmark>=4.0.0",
    "black>=23.7.0",
    "flake8>=6.0.0",
    "mypy>=1.4.1",
    "isort>=5.12.0",
    "pre-commit>=3.3.3",
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=1.3.0",
    "mutmut>=2.4.0",
]

# Optional dependencies for different features
extras_require = {
    "dev": dev_requires,
    "openai": ["openai>=1.0.0"],
    "anthropic": ["anthropic>=0.3.0"],
    "google": ["google-cloud-aiplatform>=1.35.0"],
    "aws": ["boto3>=1.28.0", "sagemaker>=2.0.0"],
    "all": [
        "openai>=1.0.0",
        "anthropic>=0.3.0", 
        "google-cloud-aiplatform>=1.35.0",
        "boto3>=1.28.0",
        "sagemaker>=2.0.0",
    ],
}

setup(
    name="theotech-conscience",
    version="1.0.0",
    author="TheoTech Neural Systems",
    author_email="info@theotech.ai",
    description="Divine Anxiety and Moral Scar Tissue for AI Safety",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theotech/theotech-conscience",
    project_urls={
        "Bug Tracker": "https://github.com/theotech/theotech-conscience/issues",
        "Documentation": "https://docs.theotech.ai",
        "Source": "https://github.com/theotech/theotech-conscience",
        "Changelog": "https://github.com/theotech/theotech-conscience/blob/main/CHANGELOG.md",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: FastAPI",
        "Natural Language :: English",
    ],
    python_requires=">=3.10",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "theotech=theotech.cli:main",
            "theotech-server=theotech.api.server:main",
            "theotech-monitor=theotech.monitoring.dashboard:main",
        ],
    },
    include_package_data=True,
    package_data={
        "theotech": [
            "config/*.yaml",
            "models/*.json",
            "templates/*.html",
            "static/*",
        ],
    },
    keywords=[
        "ai safety",
        "machine learning",
        "ethics",
        "moral ai",
        "divine anxiety",
        "moral scar tissue",
        "ai governance",
        "ai monitoring",
        "llm safety",
        "artificial intelligence",
    ],
    license="MIT",
    platforms=["any"],
)
