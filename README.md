# Hello-World

## 增加 ssh 登录
1. 生成 ssh key
  ```
  $ ssh-keygen -t rsa -b 4096 -C
  ```
  生成 
  ~/.ssh/id_rsa
  ~/.ssh/id_rsa.pub

2. 上传 ssh key 至 github
  将 ~/.ssh/id_rsa.pub 的内容加入 github 的 Settings -> SSH Keys -> New SSH key 内，保存

3. 测试 github 的 ssh 链接
  ```
  $ ssh -T git@github.com
  ```

4. 检查本地 origin 地址
  ```
  $ git config -l
  .....
  remote.origin.url=https://github.com/...
  .....
  ```
  remote.origin.url 是 https 的，提交还要用户名密码

5. 更新本地 origin 地址为 ssh 方式
  ```
  $ git remote remove origin

$ git remote add origin git@github.com:...

$ git config -l
......
remote.origin.url=git@github.com:...
......
```
现在应该好了

6. Done

