from __future__ import print_function

import sys
from pathlib import Path

# Ensure the project root is on sys.path so `proto_compiled` can be imported
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import grpc
from proto_compiled import product_pb2, user_pb2
from proto_compiled import product_pb2_grpc, user_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        product_stub = product_pb2_grpc.ProductServiceStub(channel)
        user_stub = user_pb2_grpc.UserServiceStub(channel)

        # Call GetProduct
        product_response = product_stub.GetProduct(product_pb2.ProductRequest(id="123"))
        print(f"Product: {product_response.name}, Price: {product_response.price}")

        # Call GetUsers
        user_response = user_stub.GetUsers(user_pb2.GetUserRequest(id="456"))
        for user in user_response.users:
            print(f"User: {user.name}, Email: {user.email}")