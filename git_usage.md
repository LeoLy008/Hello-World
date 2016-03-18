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
git log -1 (显示提交日志，-n, n表示要看的commit的数量)
git log --stat --summary (显示git commit 每次提交的状态，变化)

git show (显示当前git commit 的信息，提交人信息，变更的 git diff 结果)
git show commit-id (显示特定commit-id的提交信息)
git show commit-id-first-part (同上，不许提供完整的commit-id 前缀即可)
git show HEAD (当前版本)
git show HEAD~ (当前版本的前一个版本)
git show HEAD~~ (当前版本的前两个版本)
git show HEAD~n (当前版本的前n个版本, n 是数子)
```

#### 7. git tag
增加标签

#### 8. git merge
合并操作

#### 9. git diff
比较操作

#### 10. git checkout 
切换分支操作
1. 创建新分支
  ```
  git checkout -b branch-name
  ```

2. 切换到本地其他分支
  ```
  git checkout local-branch-name
  git branch -l (显示本地分支, == git branch)
  ```

3. 切换到服务器某个分支
  ```
  git checkout remote-branch-name
  git branch -r (显示远程的分支)
  ```

4. 切换到特定的 commit-id
  ```
  git checkout commit-id
  ```

5. 切换到特定的 tag
  ```
  git checkout tag
  ```

除了 ``1``, ``2``外，其他只是临时切换(切换后当前无branch)
