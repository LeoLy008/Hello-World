# git 命令

### git 本地操作基本命令 
[http://blog.csdn.net/hangyuanbiyesheng/article/details/6731629]学习链接

#### 1 git init
创建一个空的``git`` 库。在当前目录生成一个``.git``子目录，将当前路径作为仓库的根目录。
``.git/config``文件存放着配置信息

#### 2 git add
将当前目录中**修改**或**新增**的文件加入到``git``的索引中。加入索引表示记入版本历史。**是提交之前必须执行的一步**。
自动识别目录，并添加目录下的所有文件及子目录(及子目录的文件)
```
git add dir1  (添加dir1目录及其下的所有内容)
git add f1 f2 (添加文件f1, f2)
git add . (添加当前目录下的所有文件及子目录)
```

#### 3. git rm
从当前目录和索引中删除文件或目录。
与``git add``相反的操作
```
git rm -r * (删除当前目录下的所有文件及子目录)
git rm f1 (删除 f1 , 删除本地文件及索引中的文件)
git rm -ached f1  (删除文件f1,不删除本地目录文件，只删除索引中的文件，不提交f1; 将f1移动到 cache 中 )
```

#### 4. git commit
提交当前工作目录的修改内容，不能没有注释，
```
git commit -m "this is a comment"
git commit -a (将没有使用 git add 命令添加的变化也一起提交)
```
每次提交，``git``会为``commit``操作建议一个唯一的标识，可通过``git reset``命令恢复到任意提交时的代码。
```
git commit --amend -m "message" (在当前 commit id 上不断修改提交的内容，不重新创建commit标识)
```

#### 5. git status
查看当前库的状态，可检查发生了哪些变化

#### 6. git log
查看历史日志，
```
git log -1 (显示日志及提交的commit的一个日志，-n, n表示要看的comment的数量,)
```