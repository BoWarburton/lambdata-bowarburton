# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-dspt5-bowarburton", # the name that you will install via pip
    version="1.0",
    author="Bo Warburton",
    author_email="bo@warburton.com",
    description="Lambda School Data Science Unit 3, Sprint 1",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/bowarburton/lambdata-dspt5-bowarburton",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)