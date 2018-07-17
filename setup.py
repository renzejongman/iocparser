import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name                            = "iocparser",
    version                         = "1.0.11",
    author                          = "Renze Jongman",
    author_email                    = "info@renzejongman.nl",
    description                     = "scrapes IOCs from plaintext",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/renzejongman/iocparser",
    packages                        = setuptools.find_packages(),
    data_files                      = [('data', ['iocparser/data/tlds', 'iocparser/data/extensions'])],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
