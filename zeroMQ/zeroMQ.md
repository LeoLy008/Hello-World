
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


### PUB - USB 模式
发布订阅模式, 较多的抱怨是订阅端无法收到全部的发送信息\b
需要初始化的部分是:\b
1. 发送端
```
    zmq::content_t content(1);
    zmq::socket_t socket(content, ZMQ_PUB); // 初始化为 ZMQ_PUB 模式
    socket.bind("tcp://*:5556"); // 服务端总是使用 bind 

    while (true) {
        zmq::message_t msg;
        memcpy(msg.data(), "blah blah blah", 14);
        socket.send(msg);
        sleep(1);
    }

```
   发送端可以使用 `PGM` 协议进行多播, 支持两种形式的 `PGM` 协议\b
   使用多播时,必须提供多播地址, `bind`的参数为 `protocol://netIF;multipcastAddress:port`, 其中 `netIF`网卡表示或网卡IP\b
   1. 原始套接字封装的 `PGM` 协议, 因此需要访问`raw socket`的权限运行, `bind` 的 `protocol` 为 `PGM`
   2. 基于 `UDP` 实现的 `PGM` 协议, 无需`raw socket`权限, `protocol` 为 `EPGM`


2. 订阅端
```
    zmq::socket_t socket(content, ZMQ_SUB); // 构造 ZMQ_SUB 模式的socket
    socket.connect("tcp://localhost:5556"); // connect to publisher
    socket.setsocketopt(ZMQ_SUBSCRIBE, "", 0); // 接收说有消息

    while (true) {
        zmq::message_t msg;
        socket.recv(&msg);
        std::cout << "Subscriber receive message:" << ((char*)msg.data()) << std::endl;

    }
```
   订阅端必须使用 `zmq::socket_t.setsocketopt(option, optionValue, valueLength)` 设置订阅过滤器\b
   `option` 应为 `ZMQ_SUBSCRIBEE`
   如果订阅全部内容, `optionValue` 为空(`""`), 且 `valueLength` 为0\b
   非空的`optionValue`会匹配收到的订阅信息的首部, 如果匹配, 则可见, 否则不可见\b
   可以在此`zmq::socket`上多次调用`setsocketopt`来追加多个过滤器, 满足任意一个过滤器的消息都将被接收\b


特点:
1. 如果发送端发现没有接收端连接, 直接丢弃所有消息
2. 一个`subscriber`可以连接多个`publisher`通过多次调用 `connect`方法 [zmq_connect man page](http://api.zeromq.org/4-0:zmq-connect)
3. 如果是基于`tcp`的连接, `subscriber`较慢会影响`publisher`(`publisher`将会将消息排队)
4. 自`3.x`开始, 使用`tcp`或`ipc`协议时`filter`是在`publisher`侧工作, `epgm`协议是在`subscriber`侧工作


