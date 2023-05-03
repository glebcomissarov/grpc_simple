# grpc_simple

## Usage

Setup python environment:

```bash
git clone git@github.com:glebcomissarov/grpc_simple.git

python3 -m venv .grpcvenv
source .grpcvenv/bin/activate

pip install grpcio grpcio-tools pyarrow duckdb
```

Update (generate) proto python files:

```bash
python -m grpc_tools.protoc -I ./grpc_stream/proto \
    --python_out=grpc_stream/ --grpc_python_out=grpc_stream/ stream.proto
```
