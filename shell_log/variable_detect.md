# shell parameter substitution

+ ``${var}`` 返回变量``var``的值

+ ``${var-default}`` 如果`var`未声明, 则返回`default`作为表达式的值,`var`无变化
+ ``${var:-default}`` 如果`var`未声明或`var`为null, 则返回`default`作为表达式的值,`var`无变化

+ ``${var=default}`` 如果`var`未声明, 则设置`var=default`, 并返回 ${var}; 否则无变化
+ ``${var:=default}`` 如果`var`未声明或`var`为null, 则设置`var=default`, 并返回 ${var}; 否则无变化

+ ``${var+alt_val}`` 如果`var`已声明, 则返回`alt_val`作为表达式的值, 否则返回null
+ ``${var:+alt_val}`` 如果`var`已声明, 且不为null, 则返回`alt_val`作为表达式的值, 否则返回null

+ ``${var?"err msg"}`` 如果变量`var`未声明, 则打印 `err msg` 并退出当前脚本, 返回值为`-1`
+ ``${var:?"err msg"}`` 如果变量`var`未声明或`var`为`null`, 则打印`err msg`并退出当前脚本, 返回值为`-1`
