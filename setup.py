from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "simple gRPC stream client-server project"

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="grpc_stream",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_dir={"": "grpc_stream"},
    packages=find_packages(where="grpc_stream"),
    url="https://github.com/glebcomissarov/grpc_simple",
    python_requires=">=3.11",
    install_requires=[
        "grpcio==1.54.0",
        "grpcio-tools==1.54.0",
        "pyarrow==11.0.0",
        "duckdb==0.7.1",
    ],
)
