# HDFS 架构
HDFS由一些互联的节点集群组成, 文件和目录驻留在这些节点上.

一个HDFS集群包含一个(至少)管理文件系统名称空间并规范客户端对文件的访问的节点, 称为``NameNode``

将数据作为块存储在文件中的节点,称为 ``DataNode``

一个给定的``NameNode``管理一些文件系统名称空间操作,如打开,关闭及重命名文件和目录.

``NameNode``还将数据块映射到``DataNode``,处理来自HDFS客户端的读写请求.

``DataNode``根据``NameNode``的指令创建,删除和复制数据块

## NameNode 和 DataName 的关系
HDFS由java构建, ``NameNodeh``和``DataName``都是由一些软件组成的. 任何安装了java环境的机器都可以作为``NameNode``或``DataNode``运行.

``DataNode``持续循环,询问``NameNode``的指令.

``NameNode``不能直接连接到``DataNode``, 它只是从``DataNode``调用的函数返回值.

每一个``DataNode``都维护一个服务,以便客户端代码或其他的``DataNode``能够读写数据.


### HDFS 通信协议
多有HDFS协议都基于 TCP/IP.<br>
HDFS客户端连接到``NameNode``上的TCP端口,使用RPC与``NameNode``通信.<br>
``DataNode``使用给予数据块(TCP)的协议与``NameNode``通信

## 数据复制
HDFS复制文件块以便于容错. 应用程序可以在一个文件创建时指定该文件的副本数, 这个数可以以后更改.``NameNode``负责所有块的复制决定.

HDFS使用一个智能的副本放置模型来提高可靠性和性能.

HDFS 可以指定机柜ID, 因此具有机柜意识, 同一机柜内的主机的网络带宽高于不同机柜的, 依次可以进行存储优化.


## 数据组织
HDFS 支持大文件. 典型的HDFS块的大小为64MB. 每个HDFS文件包含一个或多个64MB块. HDFS尝试将每个块都放置到独立的``DataNode``上.

客户端在向HDFS中创建文件时,首先在本地打开一个临时文件,将提交的内容写入临时文件.
当临时文件的大小达到一个HDFS块时,客户端向``NameNode``报告,<br> ``NameNode``将文件转换为一个永久的``DataNode`<br>`
客户端关闭临时文件,打开一个新的临时文件写入,直到写满块或关闭文件.

### 复制管道化 (pipelining)
当客户端累计一个完整的块数据时,它将从``NameNode``检索包含那个块的副本的``DataNode``的列表.然后客户端将整个数据块注入到副本``DataNode``列表的第一个中. 当``DataNode``接收数据块时, 它将数据块写入磁盘, 然后将副本转移至列表的下一个``DataNode``. 这一过程持续至复制因子被满足.


## 可靠性
HDFS 使用心跳来检测``NameNode``和``DataNode``的联通性.

HDFS心跳是由``DataNode``发送给``NameNode``, 如果``NameNode``不能接收``DataNode``的心跳, 则认为此节点不可用,标记为``DeadNode``, 不再向他发送请求. ``DataNode``对客户端也就不可见了, 从而有效的删除了``DataNode``.

如果``DataNode``死亡导致数据复制因子降至最小值之下, ``NameNode``将启动附加复制. 将复制因子带回正常状态.


## 数据完整性

### 同步元数据更新

## 用户文件和目录权限
