import grpc
from concurrent import futures
from proto_compiled import product_pb2, user_pb2
from proto_compiled import product_pb2_grpc, user_pb2_grpc

class ProductService(product_pb2_grpc.ProductServiceServicer):

    def GetProduct(self, request, context):
        print(f"Received request for proudct ID: {request.id}")

        return product_pb2.ProductResponse(
            id=request.id,
            name="Super Fast Laptop",
            price=1999.99
        )

class UserService(user_pb2_grpc.UserServiceServicer):    
    def GetUsers(self, request, context):
        print(f"Received request for user ID: {request.id}")

        return user_pb2.CreateUserResponse(
            users = [
                user_pb2.User(
                    id=request.id,
                    name="John Doe",
                    email="john.doe@example.com"
                )
            ]
        )

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(),server)
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(),server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    server()