
## ZeroMQ
ZeroMQ 提供面向消息的 socket 封装, 支持 `N:M` 的连接模式

### Request - Reply 模式
服务端作为 `Reply` 端, 使用 `zmq_recv()` 和 `zmq_send()` 接收再发送
客户端作为 `Request` 端, 使用 `zmq_send()` 和 `zmq_recv()` 发送再接收, 乱序调用会导致错误.

服务端:
``` c++
zmq::content_t content(1);
zmq::socket_t socket(content, ZMQ_REP); // 初始化为 ZMP_REP 模式 响应方
socket.bind("tcp://*:5555"); // tcp, 接收任意源到接口上5555端口的请求

while (true) {
    zmq::message_t request;

    socket.recv(&request); // 阻塞等待消息
    std::cout << "Receive Data:" << std::endl;

    zmq::message_t reply(5); // reply data length
    memcpy(reply.data(), "World", 5);
    socket.send(reply);
}
```

客户端:
``` c++
zmq::content_t content(1);
zmq::socket_t socket(content, ZMQ_REQ); // 初始化为 ZMP_REQ 模式 请求方
socket.connect("tcp://localhost:5555"); // tcp, 连接到本地的5555端口

zmq::message_t request;
memcpy(request.data(), "Hello", 5);
socket.send(request);

zmq::message_t reply;
socket.recv(&reply); // 阻塞等待消息
std::cout << "Receive Data:" << std::endl;

```

