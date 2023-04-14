以下是一个简单的 Python gRPC 示例：

1. 首先，需要安装必要的依赖项：

   ```
   pip install grpcio grpcio-tools
   ```

2. 接下来，定义你的服务和协议。例如，我们可以创建一个名为 `messages.proto` 的文件，并在其中添加以下内容：

   ```protobuf
   syntax = "proto3";

   package messages;

   message Request {
       string text = 1;
   }

   message Response {
       string result = 1;
   }

   service MyService {
       rpc MyMethod(Request) returns (Response) {}
   }
   ```

3. 然后，使用 protobuf 编译器根据 .proto 文件生成所需的代码：

   ```
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. messages.proto
   ```

4. 现在，可以编写服务器端代码。以下是一个简单的示例：

   ```python
   import grpc
   import messages_pb2
   import messages_pb2_grpc

   class MyService(messages_pb2_grpc.MyServiceServicer):
       def MyMethod(self, request, context):
           return messages_pb2.Response(result='Hello, {}'.format(request.text))

   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   messages_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
   server.add_insecure_port('[::]:50051')
   server.start()
   server.wait_for_termination()
   ```

5. 最后，编写客户端代码以连接到服务器并调用服务：

   ```python
   import grpc
   import messages_pb2
   import messages_pb2_grpc

   channel = grpc.insecure_channel('localhost:50051')
   stub = messages_pb2_grpc.MyServiceStub(channel)
   response = stub.MyMethod(messages_pb2.Request(text='World'))
   print(response.result)
   ```

这是一个简单的示例来帮助你入门 gRPC 开发。如果需要更多信息，请参阅官方文档：[https://grpc.io/docs/tutorials/basic/python.html](https://grpc.io/docs/tutorials/basic/python.html)



# 创建一个虚拟环境
$ python3 -m venv venv
# 激活虚拟环境
$ source venv/bin/activate
# 安装依赖
$ pip install -r requirements.txt
# 运行服务端
$ python server.py