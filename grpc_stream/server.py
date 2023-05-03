from concurrent import futures
from grpc_interceptor.exceptions import NotFound
from google.protobuf.timestamp_pb2 import Timestamp

import grpc
from stream_pb2 import DataFrame
import stream_pb2_grpc

from datetime import datetime
import duckdb


class ReturnPurchasesServicer(stream_pb2_grpc.ReturnPurchasesServicer):
    def return_data(self, request, context):
        for response in self.__sql_response(request.bank_id, request.day):
            if response is None:
                raise NotFound("Data was not found. Change your request.")

            date_sent = Timestamp()
            date_sent.FromDatetime(datetime.now())

            yield DataFrame(
                name="purchases",
                date_sent=date_sent,
                bin_table=response,
            )

    @staticmethod
    def __sql_response(bank_id: int, day: str) -> list[bytes] | None:
        con = duckdb.connect(
            database="grpc_stream/data/server_db.duckdb", read_only=True
        )

        tables = ["purchases", "products_info", "categories_info"]
        request = []
        for tb in tables:
            request.append(con.sql(f"select * from {tb}").df().to_parquet())

        return request


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stream_pb2_grpc.add_ReturnPurchasesServicer_to_server(
        ReturnPurchasesServicer(), server
    )

    server.add_insecure_port("[::]:443")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run_server()
