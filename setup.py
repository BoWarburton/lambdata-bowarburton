# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-bowarburton",
    version="1.1",
    author="Bo Warburton",
    author_email="bo@warburton.com",
    description="Lambda School Data Science Cohort DSPT5, Unit 3, Sprint 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/bowarburton/lambdata-bowarburton",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)