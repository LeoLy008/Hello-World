# docker run 相关命令

## docker run
``docker run <options> <image> <command>`` 用于启动镜像

``docker run --help`` 查看帮助<br>
常用的 ``options`` 有
+ --name "containerName"
  指定运行容器的名称,不指定的话为随机
+ -t
  开始终端
+ -i
  开启交互
+ -d
  detach 容器的终端
+ --rm
  容器停止运行时自动删除

## docker start
``docker start <containerName/ID>`` 启动一个已经停止的容器

## docker attach
``docker attach <containerName/ID>`` 连接到一个运行的容器

## docker rm
``docker rm <containerName/ID>`` 删除一个容器<br>

eg: ``docker rm $(docker ps -a -q)``<br>
删除所有处于停止状态的容器, ``$(docker ps -a -q)`` 返回所有容器的ID
``docker rm containerID``会删除停止运行的容器, 运行中的容器直接忽略,
