# install hadoop
[http://hadoop.apache.org/docs/r1.2.1/cluster_setup.html]

## prerequisites
1. java, install openjdk-7/8-jdk
  # apt-get install openjdk-8-jdk

2. build-essential, libssl-dev libfuse-dev, vim,

3. install apache maven which is used to build hadoop
  + download maven from https://archive.apache.org/dist/maven/binaries/
  + untar to /usr/local/maven/
  * add path /usr/local/maven/bin
  + add M2_HOME=/usr/local/maven to .bashrc

4. install protocol buffer
  + install git
  + get protocol from git:https://github.com/google/protobuf.git
  + autoreconf --install && ./configure && make install

5. build hadoop
  +mvn clean install -DskipTests
    + hadoop common require protocol buffer version 2.5.0, can't download that version (git get latest version is 3.0.0)

    install bin version of hadoop instead
    
