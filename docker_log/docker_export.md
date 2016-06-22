# docker import/export

docker 的容器是基于特定的镜像运行的实例, 镜像启动后, 所有的改动在下次启动镜像时将丢失
容器如果被删除, 我们必须重复操作.

docker 支持将运行的容器导出为文件, 可以保存容器对镜像的所有改动, 再使用 ``import`` 命令根据导出的文件生成镜像

## dock export
``docker export <containerName/ID> > localFileName.tar`` 将指定的容器`containerName/ID`导出, 生成文件`localFileName.tar`

e.g.: ``docker export hadoop myHadoopBase.tar``<br>
将名为``hadoop``的`Container`导出, 生成 `myHadoopBase.tar` 文件

## docker import
``docker import <localFileName> imageRep/Name:Tag`` 将指定的文件导入为指定标识的镜像

e.g.: ``docker import myHadoopBase.tar my/hadoop-base:2.7.2``<br>
将名为`myHadoopBase.tar`的文件导入为镜像, Repository为``my``, Name为``hadoop-base``, Tag为:``2.7.2``
