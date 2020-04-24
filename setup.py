from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="goldbar",
    version="0.0.0.1",
    packages=["goldbar",],
    install_requires=[],
    license="MIT",
    url="https://github.com/reity/goldbar",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Embedded language for defining and working "+\
                "with genetic design spaces.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
