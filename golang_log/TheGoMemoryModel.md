## go channel 的同步特性

1. The closing of a channel happens before a receive that returns a zero value because the channel is closed.
2. A receive from an unbuffered channel happens before the send on that channel completes. (无缓冲的channel的读取发生在channel的写入完成之前; 缓冲channel无此特性)
```golang
var c = make(chan int) // 无缓冲的channel
var a string

func f() {
    a = "hello, world"
    <- c // receive from unbuffered channel
}

func main() {
    go f()
    c <- 0 // send on the unbuffered channel
    // 因为 channel 的同步特性, c <- 0 必然发生在 <- c 后, 所以 print(a) 必然在 a = "hello, world" 赋值后
    print(a)
}
```
3. The `kth` receive on a channel with capacity `C` happens before the `k+Cth` send from that channel completes. (容量为C的channel, 其第n次读取必定发生在第n+C次写入完成之前 此机制可以模拟信号量同步方式,控制任务线程的数量)
```
var limit = make(chann int, 3) // 容量为3的channel

func main() {
    for _, w := range work {
        go func(w func()) {
            limit <- 1 //写入, 消耗一个位置
            w()
            <- limit // 读取, 释放一个位置
        }(w)
    }
    select{}
}
```
因 limit 只有三个位置, 因此当第四个goroutine执行到 `limit <- 1` 时, 会被阻塞(前提是前三个gorountine还未指定到 `<- limit` 的位置)


## Locks
golang 的锁由 `sync` 包提供的 `sync.Mutex` 及 `sync.RWMutex`

1. 对于 `sync.Mutex` 及 `sync.RWMutex` 且 n < m 时, n 时的 `Unlock()` 必定发生在m 时的 `Lock()` 返回前 (锁先被释放后才能被再次锁定, 废话!!)


## Once
`sync.Once` 确保多个 goroutines 中只有一个运行 `once.Do()` 指定的行为, 为多 goroutines 的初始化提供方便.
```
var a string
var once sync.Once

func setup() {
    a = "Hello, world"
}

func doprint() {
    once.Do(setup)
    print(a)
}

func main() {
    go doprint()
    go doprint()
}

```

## 错误的同步
1. 不能假设在某个goroutines中顺序执行的赋值操作的顺序为代码的书写顺序
```
var a, b int
var s string
var done bool

func f() {
    a = 1
    b = 2
}

func setup() {
    s = "Hello, world"
    done = true
}

func g() {
    print(b)
    print(a)
}

func main() {
    go f()
    g()
    go setup()
    for !done {
    }
    print(a)
}
```
如果 g() 打印的 `b` 为 `2`, 也不能确保 `a` 打印的值是 `1`
不能确保打印的`s`为`Hello,world`因为 `done`的赋值是在其他goroutines中

