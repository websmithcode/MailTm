import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MailTm Py",
    version="0.1.4",
    author="WSCode",
    description="Temporary Email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["mail", "email", "temporary mail", "temporary email", "mailtm"],
    url="https://github.com/websmithcode/MailTm",
    project_urls={
        "Bug Tracker": "https://github.com/websmithcode/MailTm/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=["requests", "pydantic"],
)
