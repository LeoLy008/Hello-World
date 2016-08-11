# golang book
2016-01-22

## Types
- difficult conecpt to grasp
- different perspectives
- how they are implemented in Go

Philosohpers make a distinction between **types** and **token**<br>
> You have a *dog* named *Max*.
*Max* is the **token** (a particular instance or member) and *dog* is the **type**<br>
**Type** describes a set of properties that all this type have in common.

Golang 是静态类型(cumbersome)语言。所以所有变量都有特定的类型，且类型不可变。

### build in types
#### Numbers
##### Integers
machine independent type
- uint8, uint16, uint32, uint64
- int8, int16, int32, int64
- byte (the same as uint8)
- rune (the same as int32)

machine dependent types
- uint
- int
- uintptr


##### Floating Point Numbers
- NaN 0/0 （not a number)
- float32, float64
- complex64, complex128


##### Operateion
Symbol | Means
:----:|:-----
+|addition
-|subtraction
\*|multiplication
/|divison
%|remainder

#### Strings
Go strings are made up of individual bytes (utf-8)<br>
String can be created using
- **double quotes** `""`<br>
  can't contain newlines and they allow special escape sequences<br>
  as `\n` is newline, `\t` is tab
- **back ticks** <code>\`\`</code><br>
  can contain any character and will not be escaped

##### Operateion
Symbol | Means|
:---:|:-----
len() | get length of string<br> ``len("123")``
[*i*] | iterator in byte, *i* as index<br> ``"123"[1] is '1'``
 +    | string concatenate,<br> ``"123" + "456" is "123456"``


##### Notice
1. Strings are **indexed** starting at **0**
2. ``string[i]`` return value is **byte**

#### Booleans
##### Operateion
Symbol | Means
:---:|:-----
&& | and
|| | or
! | not


### 数组类型
#### array
array 是定长数组，使用``[size]type``定义，
- 不能改变大小
- 同类型，不同大小的数组不能比较

#### Slice
slice 是切片，是 golan 中的变长数组，可以通过以下方式创建
- a := []int{123} // 长度1
- b := make([]int, 10, 100) //初始长度是10，容量100
- c := b[:] // 从其他数组或 slice 切片得到

##### Slice Operateion
- append<br>
  `append(sliceA, element1, element2, ...)``
  将`element1, elemnt2`追加到`sliceA`的
- copy<br>
  `copy(dstSlice, srcSlice)``
  将`srcSlice`中`dstSlice长度`个数的元素复制到`dstSlice`中
- []<br>
  索引

#### Map
map 是无顺序的 key-value 对集合(associative array, hash table or dictionary).
1. var x map[string]int // key as string, value as int<br>
  x is a map of `string`s to `int`s, 没有赋值
2. map 是动态类型，上句只是声明`x`是`string`到`int`的字典，并未为其创建实体
3. x = make(map[string]int) //创建 map 实体并赋值给x，**不能指定大小及容量**

##### Map Operateion
- delete element using with `delete(mapVar, key)`<br>
  使用`delete`删除字典中key为索引的元素
- 使用并行赋值提取元素并判断是否存在<br>
  `value, ok := x["key"]`,如果`key`存在，则`ok`为`true`
- 嵌套map<br>
  ```Golang
  x := make(map[string]map[string]string)
  x["a"] = map[string]string{
    "a1":"a",
    "a2":"b",
  }
  x["b"] = map[string]string{
    "b1":"xx",
    "b2":"xxx",
  }
  ```

## Function
函数的格式
`func funcName(paraName type) (type) {}`
``func 函数名(参数列表) (返回值列表) {函数体}``

### 函数名
### 参数列表
- 参数类表的`()`是必须的，参数列表以 `valName type` 的形式出现
- `...type` 表示不定参数列表，类型为`type`,只能出现在参数列表的末端
- `x ...type` 表示零个到任意个`type`类型的变量, `x`是一个数组
- `x ...interface{}`表示接受任意个 `interface{}`类型
- 传递数组时，可以使用`arraryTypeVariable...` 表示展开数组元素并传递给函数


### 返回值列表
- 返回值列表的`()`是可选的，在命名返回变量，多返回值(命名或不命名返回变量)是必须的
- 命名返回值可以在函数内作为变量使用
- 函数返回时，直接使用 `return` 即可，无需明确指明返回值，命名返变量的值将被返回
- 执行到函数体末端也会结束
- 函数可以返回函数


### closure
golang 允许在函数内定义匿名函数，匿名函数可以直接访问定义它的函数中的变量
```golang
func fool() int {
  i := uint(0)
  f := func () {
    fmt.Println("fool() inner function f can see i:%x", i)
  }
}
```
使用此种方式可以创建生成器/迭代器：
```golang
oddGen := oddGenerator(3)
func oddGenerator(startVal ...int) func() int {
  var i int = 1
  return func() int {
    i += 2
    return i
  }
}
```
`oddGenerator()` 调用时，返回的函数对象`oddGen`引用了`oddGenerator()中的i`，因此`i`作为返回的函数对象的一部分被保留，只有当前返回的函数对象可以访问它`


### defer
- `defer`在函数中用户管理函数退出前的行为。
- `defer` 指定的行为将在函数退出时被执行，golang 保证其执行，无论是正常退出或是异常退出
- `defer` 指定的行为按照 `FILO` 的顺序被执行
- `defer` 可指定匿名函数执行

### panic
- 使用`panic`可以抛出异常<br>
  ``panic(value)`` 将引发 `panic` 并产生 `value` 作为 `panic` 的值

### recover
- `reocver` 可以捕获 panic<br>
- `recover` 必须放在函数的 `defer` 中才有效
- `value := recover() `返回panic的赋值, 未发生`panic`,`value`是`nil`,否则为抛出的值


## pointer
golang 默认使用传值调用函数，如果想在被调用函数中修改输入变量的值，需要传递指针给被调用函数<br>
- \*type 表示指定类型的指针
- \*(pointer variable) 表示取指针的值
- &(variable)表示获取对应变量的指针

## struct
### method

## interface
### reflect

## concurrency
### channel
### select

## Packages
> Don't Repeat Yourself

Three purposes<br>
1. reduces the chance of having overlapping names
2. organizes code, reuse code
3. speeds up compiler, only compile chunks changed

### create Packages
#### src path
`package` 的源代码应该放在 `GOPATH` 指定目录的`src`目录下<br>
如：<br>
`f:\study\golang\lib` 为 `GOPATH` 的路径，则`f:\study\golang\lib\src`为合法的`package src`目录
`f:\study/golang\lib\src/golang-book/chapter11/testPackage` 目录作为包路径，创建 `math.go`
```golang
package math

import "fmt"

func Add(iList ...int) (sum int64) {
  for v, idx := range iList {
    sum += int64(v)
  }
}
```
之后在`f:/study/golang/lib/src/`任意目录下运行 `go install` 将会编译此路径下所有可用的包源文件<br>
编译成功将在会把对应的包的可链接目标文件拷贝到 `f:\study/golang/lib/pkg/os_path/` **对应路径** 下<br>
如`f:\study/golang\lib\src/golang-book/chapter11/testPackage/math.go` 编译后生成的可链接目标文件将生成到`f:\study/golang/lib/pkg/window_amd64/golang-book/chapter11/testPackage.a`<br>

##### 为何是 `testPackage.a`, 而不是 `testPackage/math.a`?
- golang 中包可有多个目标文件组成，`testPackage.a` 是包的引用路径名`f:\study/golang\lib\src/golang-book/chapter11/testPackage/math.go`下所有源文件编译后的集合文件，`testPackage`目录下的源文件中 `package packageName`指定实际的包名字
- 同一个包路径下不能存在多个不同 `package packageName` 的源文件，否则会报错<br>
- 使用包时`import`的是从`src`之后的路径名,直到`src`文件的路径，`golang-book/chapter11/testPackage`
- 使用 `math` 包时，使用`math.`引用`math`包内的导出对象
- 导出对象使用 **首字母大写规则** (表示`public`,外部可直接访问)，适用于 **包内的函数，类型，结构体的成员及方法**

#### short name
`import shortName "packagePathFullName"`
`shortName` 是包的别名，在使用时可以简化输入，可以防止重名
``包``源码内置使用``包名``即可


## testing
- 测试引入包`package "testing"`
- 测试文件命名规则 `xxxx_test.go`
- 测试函数名 `TestXxxx(t *testing.T)`
- `t.Fail() 当前函数测试失败，继续f`


## init function
每个文件都可以包含一个 `init` 函数 `func init() {}`
这个函数在文件被加载完成时执行
- 文件范围变量被初始化后(evaluated)
- 引入的包被初始化后
- 执行 `init` 函数

## sort 接口
golang 的 sort 接口定义为
```golang
type sortable interface {
    func Len() int
    func Less(i, j interface{}) bool
    func Swap(i, j interface{})
}
```

## interface conver and type assertions
类型断言只能在 `switch` 中能够使用，格式为 `interfaceVariable.(type)` 返回 `interfaceVariable` 的实际类型的变量，`switch` 隐含获得`类型`，可在`case`中直接判断，如下
```golang
type Stringer interface {
    String() string
}
func getString(value interface{}) string {
    switch str := value.(type) {
    case string:
        return str
    case Stringer:
        return str.String()
    }
}
```
其中 `switch str := value.(type) ` `str` 被赋予``value实际类型的值``，因为`value`是``interface{} 是空接口``，可以是任何值，.(type)获取他的实际类型的变量<br>
`switch`隐含获得了``value的type值``，在`case`分支中可直接判断`value`的`type`<br>

- ``ifVar.(type)`` 是获得实际存储类型的变量
- ``ifVar.(typeName)`` 是试图获得 typeName 类型的变量
- 返回的变量是``type/typeName``类型的新变量，而非原变量的引用


## blank identifier `_`
`_` 用来接收不用的变量，可以用来做：
- 避免编译时提示未使用的变量， `_ = fd` 这样 `fd` 就不会被报未使用
- 导入包但不用或导入包是为其 `side effects`, 如`import _ net/http/pprof` 这样不使用包也不会提示编译错误
- interface conversion check for run-timer
  `var _ json.Marshaler = (*RawMessage)(nil)` 只做类型检查，不做变量的实体转换。<br>
  将 `nil`(空)的``*RawMessage``类型转换为 `json.Marshaler`，即 RawMessage 是否实现了 json.Marshaler接口，如果未实现，此行代码在编译时会报错，否则不会报错
