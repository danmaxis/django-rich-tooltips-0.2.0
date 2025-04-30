from setuptools import setup, find_packages
import os

# Function to read the README file.

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-rich-tooltips",
    version="0.2.0", # Start work on new features
    author="Manus AI (for User)", # Replace with actual author if desired
    author_email="<your-email@example.com>", # Replace with actual email if desired
    description="A Django plugin to add rich HTML/Markdown tooltips to the admin interface.",
    license="MIT",
    keywords="django admin tooltip markdown html rich interactive",
    url="https://github.com/yourusername/django-rich-tooltips", # Replace with actual URL later
    # Specify the actual package directory
    packages=find_packages(exclude=["test_project", "test_project.*"]),
    package_dir={},
    # Ensure templates and static files are included
    include_package_data=True,
    long_description=read("README.md"),
    long_description_content_type="text/markdown", # Specify markdown type for PyPI
    classifiers=[
        "Development Status :: 3 - Alpha", # Initial development stage
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1", # Add compatible versions
        "Framework :: Django :: 5.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "Django>=5.0",
    ],
    python_requires=">=3.10", # Specify compatible Python versions
    # Add extras if needed, e.g., for testing
    # extras_require={
    #     'test': ['pytest', 'pytest-django'],
    # }
)

