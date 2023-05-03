import grpc
import stream_pb2, stream_pb2_grpc

import pandas as pd
from io import BytesIO

import time


def send_request():
    with grpc.insecure_channel("localhost:443") as channel:
        stub = stream_pb2_grpc.ReturnPurchasesStub(channel)
        request = stream_pb2.get_req(bank_id=1, day="2023-01-25")

        for i, resp in enumerate(stub.return_data(request)):
            # print(str(resp.schema), pickle.loads(resp.bin_table).shape)
            # print(pickle.loads(resp.bin_table).head(3))
            print(f"resp {i}")
            print(resp.date_sent.ToDatetime())
            # print(resp.schema)
            # df = pq.read_table(pa.BufferReader(resp.bin_table)).to_pandas()
            df = pd.read_parquet(BytesIO(resp.bin_table))
            print(df.head(1))
            # print(pd.read_parquet(resp.bin_table).head(3))
            # print(resp.bin_table)
            # pq.read_table(resp.bin_table).to_pandas()
            print("=== === ===")
            # pickle.loads(resp.bin_table).to_csv(f"table{i}.csv")


t_start = time.time()
send_request()
t_finish = time.time()
print(f"appox time: {round(t_finish - t_start, 4)} sec.")
