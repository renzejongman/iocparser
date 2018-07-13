import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name                            = "iocparser",
    version                         = "1.0.0",
    author                          = "Renze Jongman",
    author_email                    = "info@renzejongman.nl",
    description                     = "scrapes IOCs from text",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/renzejongman/iocparser",
    packages                        = setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)