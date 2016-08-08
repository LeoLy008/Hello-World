# special characters in shell

+ `#` 表示注释, `#` 后的当前行内容被视为注释<br>
  `''`及`""`内的`#`, `\#` 使shell认为`#`为标准的输出字符, 而非注释的开始<br>
  `#` 后应带空格; <br>
  `#` 非行首时, 前方应带空格; <br>
  `#` 多行的注释, 续行应以``+``开头; <br>

+ `;` 可以将多个`cmd; cmd`写在一行, `cmd`按顺序执行, 前一个执行完成后, 执行下一个
  ';' 后应至少跟一个空格, 如在 `if []; then; cmd; else; cmd; fi;` 中, `then`, `else`及`fi`都为shell命令, 而非 `if test condition then cmds else cmds fi`的语法, 所以他们如果写在一行,必须使用`; `分隔

+ `;;` `case`分支的结束标记

+ ``"`` 部分引用, ``""``内的`shell`变量将被解释

+ `'` 全引用, ``''``内的`shell`特殊字符不被解释, 直接原样输出

+ `,` 算数表达式分隔符, 所有的表达式都会被计算, 之后最后的表达式被作为结果返回<br>
  ``let "t2 = ((a = 9, 15 / 3))"`` 结果为 ``a = 9, t2 = 15 / 3``
+ `,` 也可以连接字符串<br>
  ``` shell
  for file in /{,usr/}bin/*calc
  #             ^  find all executable files ending in "calc"
  #+               in /bin and /usr/bin directoires.
  do
    if test -x "$file"
    then
      echo $file
    fi
  done

  ```

+ `\` 转意字符

+ `/` 目录分隔符

+ <code>\`</code> 命令替换符, <code>\`cmd\`</code>; 将被替`cmd`执行的结果替换

+ `:` 代表空, 也是 `Bash buildin cmd`, `: > aaa.log` 将清空 aaa.log, 等价于 `cat /dev/null > aaa.log` 且因是`shell buildin cmd` 不会`fork`子进程
  + `while :; do; cmds; done;` while 无限循环, 等价与 `while true`
  + `if test condition; then : ; else; cmds; fi;` `then :`表示空的分支
  + `: expression` 空操作与表达式求值写在同一行, 计算表达式,且`shell`不会报错说这不是命令!
