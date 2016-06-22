# Docker Networks

## 默认网络
当安装完docker后, 可以使用``docker network ls``查看网络
默认网络有三个
+ bridge
  + 由 ``docker0``标识,是容器的默认网络配置
  + 可以使用 ``docker run --net=<NETWORK>`` 在容器启动时调整
  + 在容器内可以用 ``ifconfig`` 观察``docker0``的配置; 没有的话需要安装 ``net-tools``
  + 在host上可以用 ``docker inspect <Container>``分析容器, 查看 ``NetworkSettings`` 部分的配置
  + 使用 ``docker network inspect <Network>`` 可查看网络的配置详情
+ none
+ host


### bridge
``bridge``是容器的默认网络, 所有容器启动时自动添加到该网络<br>
``bridge``也是容器链接外部网络的网桥<br>
``# docker run -tid --name hadoop my/hadoop-base:2.7.2 /bin/bash``<br>
启动容器后, 运行 ``docker network inspect bridge``
```
root@VBX:/home/xy# docker network inspect bridge
......
        "Containers": {
            "b11f52bf711d2b2d36672b4ec9e5ab66b78b6e61f0df9573ccc1411aeec17f77": {
                "Name": "hadoop",
                "EndpointID": "94379eba02ce8d7c1255255ca9dcd80a5b0ed4ba3f07597cb87772e2b2efd3f4",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
......
```
多出的``Containers``部分, 是连接到此网络的容器的信息


### docker 网络命令

+ ``docker network create``
+ ``docker network connect``
+ ``docker network ls``
+ ``docker network rm``
+ ``docker network disconnect``
+ ``docker network inspect``

### 自定义网络
创建网络时可以指定
+ 子网 (--subnet=192.168.0.0/16)
+ 网关 (--gateway=192.168.0.1)
+ ip范围 (--ip-range=192.168.1.0/24)
+ 选项 Options (-o "com.docker.network.bridge.name"="myDockerBridge" or --opt )
这些参数都应出现在 ``--driver`` 后, 并在 ``NetworkName`` 前, 即:<br>
``docker network create --driver <DriverName> <Options> <NetworkName>``

``docker network create --driver bridge --subnet=173.0.0.0/16 -o "com.docker.network.bridge.name"="myDockerBridge" myDockerBridge``


#### bridge
``docker network create --driver bridge myNetwork``<br>
以上命令创建新的名为 ``myNetwork``的网络, 使用的``驱动``为``bridge``<br>


可以使用``docker network inspect myNetwork``查看创建的网络<br>


容器启动时使用``docker run --net=myNetwork`` 指定使用的网络, 可以指定多了, 带多个 `` --net=<Network> `` 参数即可


#### overlay
``overlay`` 网络支持多个host的Container之间互相通信, 但需要
+ 一个 ``key-value store`` 支持 (Consul, Etcd, ZooKeeper)
+ 所有 host 可以访问 ``key-value store``
+ 每个主机上配置: properly configured Engine ``deamon`` on each host in the swarm

``overlay`` 网络支持配置多个``子网(--subnet)``


#### network plugin
......
