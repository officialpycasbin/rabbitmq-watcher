from setuptools import setup, find_packages, __version__
from os import path

desc_file = "README.md"

with open(desc_file, "r") as fh:
    long_description = fh.read()

here = path.abspath(path.dirname(__file__))
# get the dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]

setup(
    name="casbin-rabbitmq-watcher",
    author="Casbin",
    author_email="admin@casbin.org",
    description="Casbin role watcher to be used for monitoring updates to policies for PyCasbin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/officialpycasbin/rabbitmq-watcher",
    keywords=[
        "casbin",
        "Rabbitmq",
        "casbin-watcher",
        "rbac",
        "access control",
        "abac",
        "acl",
        "permission",
    ],
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.5",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
