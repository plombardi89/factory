from setuptools import setup, find_packages

setup(
    name="factory",
    version="2018.09.12",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "factory = factory.cli:factory",
        ]
    },
    author="datawire.io",
    author_email="dev@datawire.io",
    url="https://github.com/datawire/factory"
)
