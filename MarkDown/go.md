# go语言的学习


- [go语言的学习](#go语言的学习)
  - [第一章 基础知识](#第一章-基础知识)
    - [1.1 rune](#11-rune)
    - [1.2 字符串](#12-字符串)
    - [1.3 数组与切片](#13-数组与切片)
      - [1.3.1 数组](#131-数组)
      - [1.3.2 切片](#132-切片)
    - [1.4 字典与布尔类型](#14-字典与布尔类型)
    - [1.5 指针](#15-指针)
    - [1.6 流程控制：if-else](#16-流程控制if-else)
    - [1.7 流程控制：switch-case](#17-流程控制switch-case)
    - [1.8 流程控制：for循环](#18-流程控制for循环)
    - [1.9 goto无条件跳转](#19-goto无条件跳转)
    - [1.10 defer延迟调用](#110-defer延迟调用)
    - [1.11 流程控制：理解select用法](#111-流程控制理解select用法)
    - [1.12 异常机制：panic和recover](#112-异常机制panic和recover)
  - [第二章 面向对象](#第二章-面向对象)
    - [2.1 结构体与继承](#21-结构体与继承)
    - [2.2 接口与多态](#22-接口与多态)
    - [2.3 go语言中的空接口](#23-go语言中的空接口)
    - [2.4 接口的三个潜规则](#24-接口的三个潜规则)
    - [2.5 详解类型断言](#25-详解类型断言)
    - [2.6 结构体里的Tag标签](#26-结构体里的tag标签)
    - [2.7 反射三定律](#27-反射三定律)
    - [2.8 全面学习反射的函数](#28-全面学习反射的函数)
    - [2.9 make和new的区别](#29-make和new的区别)
    - [2.10 面向对象：go语言中的空结构体](#210-面向对象go语言中的空结构体)
  - [第三章 项目管理](#第三章-项目管理)
    - [3.1 依赖管理：包导入的重要知识点](#31-依赖管理包导入的重要知识点)
    - [3.2 Go语言中的编码规范](#32-go语言中的编码规范)
  - [第四章 并发编程](#第四章-并发编程)
    - [4.1 函数基础](#41-函数基础)
    - [4.2 Go协程：goroutine](#42-go协程goroutine)
      - [4.2.1 协程的初步使用](#421-协程的初步使用)
      - [4.2.2 多个协程的效果](#422-多个协程的效果)
    - [4.3 详解信道/通道](#43-详解信道通道)
      - [4.3.1 信道的定义与使用](#431-信道的定义与使用)
      - [4.3.2 信道的容量和长度](#432-信道的容量和长度)
      - [4.3.3缓冲信道和无缓冲信道](#433缓冲信道和无缓冲信道)
      - [4.3.4 双向信道与单向信道](#434-双向信道与单向信道)
      - [4.3.5 遍历信道](#435-遍历信道)
      - [4.3.6 用信道来做锁](#436-用信道来做锁)
      - [4.3.7信道传递是深拷贝吗](#437信道传递是深拷贝吗)
    - [4.4 WaitGroup](#44-waitgroup)
      - [4.4.1 使用信道标记完成](#441-使用信道标记完成)
      - [4.4.2 使用waitgroup](#442-使用waitgroup)
    - [4.5 互斥锁和读写锁](#45-互斥锁和读写锁)
      - [4.5.1 互斥锁](#451-互斥锁)
      - [4.5.2 读写锁](#452-读写锁)
    - [4.6 信道死锁经典错误案例](#46-信道死锁经典错误案例)
    - [4.7实现一个协程池](#47实现一个协程池)
    - [4.8 理解go语言中的Context](#48-理解go语言中的context)
      - [4.8.1 为何需要Context](#481-为何需要context)
      - [4.8.2 简单使用Context](#482-简单使用context)
      - [4.8.3 根Context是什么](#483-根context是什么)
      - [4.8.4 Context的继承衍生](#484-context的继承衍生)
      - [4.8.5 Context注意事项](#485-context注意事项)
    - [4.9 函数类型](#49-函数类型)
## 第一章 基础知识

### 1.1 rune

rune占4个字节，共32个bit位，表示的是一个unicode字符

```go
import (
    "fmt"
    "unsafe"
)

func main() {
    var a byte = 'A'
    var b rune = 'B'
    fmt.Printf("a 占用 %d 个字节数\nb 占用 %d 个字节数", unsafe.Sizeof(a), unsafe.Sizeof(b))
}
```

输出如下
```
a 占用 1 个字节数
b 占用 4 个字节数
```

由于byte类型能表示的值是有限额，如果想要表示中文只能用rune类型
```go
var name rune ='中'
```

在定义字符时不管是byte还是rune，都要使用单引号。

单引号表示字符，双引号表示字符串。

### 1.2 字符串
```go
var mystr string ="hello"
```

上面的byte和rune都是字符类型，要是多个字符放在一起就成了字符串

```go
import (
    "fmt"
)

func main() {
    var mystr01 string = "hello"
    var mystr02 [5]byte = [5]byte{104, 101, 108, 108, 111}
    fmt.Printf("mystr01: %s\n", mystr01)
    fmt.Printf("mystr02: %s", mystr02)
}
```

输出如下,说明这两个本质上一样，string本质上就是一个byte数组
```
mystr01: hello
mystr02: hello
```

提问：hello,中国包含几个字节
在go中，英文和字符占1个字节，中文占3个字节
回答：包含5+1+(3*2)个

```go
import (
    "fmt"
)

func main() {
    var country string = "hello,中国"
    fmt.Println(len(country))
}
// 输出
12
```

双引号和反引号在大多数情况下没有区别，但是如果字符串中含有转义字符`\`那么就有区别了。**反引号中是不会识别转义字符的**

```go
var mystr1 string ="\\r\\n"
var mystr2 string =`\r\n`
//这两个的打印结果是一样的
```

同时，反引号可以不用写换行符来表示一个多行的字符串

```go
var mystr string=`你好，
                我是Weirdo`
fmt.Println(mystr)
//输出结果为
你好，
我是Weirdo
```

### 1.3 数组与切片
#### 1.3.1 数组
数组是由固定长度的特定类型元素组成的序列，由于数组长度固定，所以在go语言中很少直接使用数组

声明数组和赋值与其他语言是一样的
```go
var arr [3]int
arr[0]=1
arr[1]=2
arr[2]=3
```
声明并直接初始化数组
```go
//第一种方法
var arr [3]int=[3]int{1,2,3}
//第二种方法
arr:=[3]int{1,2,3}
```
但是这种写法比较僵硬，万一需要修改数组长度时不好操作。可以采用下面这种方式进行根据实际长度分配空间
```go
arr := [...]int{1,2,3}
```
关于数组的类型，`[3]int`和`[4]int`虽然都是int但是他们的数组类型是不同的，可以通过以下代码查看
```go
arr1 :=[3]int{1,2,3}
arr2 :=[4]int{1,2,3,4}
fmt.Printf("%d的类型：%T\n%d的类型:%T",arr1,arr1,arr2,arr2)
//输出如下
[1 2 3] 的类型是: [3]int
[1 2 3 4] 的类型是: [4]int
```

如果觉得每次写`[3]int`比较麻烦的话，可以将他定义为一个类型字面量，也就是别名类型。

使用`type`关键字可以定义一个类型字面量，后面想要定义这个类型就可以直接用这里的别名定义
```go
type int3 [3]int
arr :=int3{1,2,3}
fmt.Printf("%d的类型是：%T",arr,arr)
//输出如下
[1 2 3] 的类型是: main.arr3
```

定义数组还有一个偷懒方法
```go
arr :=[3]int{1:9}
//打印输出如下
[0,9,0]
```
他将索引为1的元素设置为9，其他元素默认设置为0

#### 1.3.2 切片

切片就是数组，但是他是将数组作为其底层结构，是对数组的一个连续片段的引用。左闭右开

```go
myarr := [...]int{1, 2, 3}
fmt.Printf("%d 的类型是: %T", myar[0:2], myarr[0:2])

//输出如下
[1 2] 的类型是: []int
//注意这里数组的定义不管是[...]还是[3]，打印出来的切片类型都是[]int
```

切片的构造方式有4种：
1. 对数组片段进行截取，有如下两种写法
   ```go
   //定义一个数组
   arr :=[5]int{1,2,3,4,5}
   //第一种
   myarr1:=arr[1,3]
   //第二种
   myarr2:=arr[1,3,4]
   ```
   这两种方法得到的切片内容是一样的，但是如果不指定第三个数的话，切片的容量会一直到原数组的结尾，第三个数就是指定容量到达的位置。

   可以用下面的代码进行验证
   ```go
    fmt.Printf("arr长度为：%d，容量为：%d",len(arr),cap(arr))
    fmt.Printf("myarr1长度为：%d，容量为：%d",len(myarr1),cap(myarr1))
    fmt.Printf("myarr2长度为：%d，容量为：%d",len(myarr2),cap(myarr2))

    //输出如下
    myarr 的长度为：5，容量为：5
    mysli1 的长度为：2，容量为：4
    mysli2 的长度为：2，容量为：3
   ```

2. 从头声明赋值
    ```go
    //字符串切片
    var strList []string
    //整型切片
    var intList []int
    //空切片
    var numListEmpty =[]int{}
    ```

3. 使用make函数构造，make函数的格式：    `make([]type,size,cap)`

    ```go
    a:=make([]int,2)
    b:=make([]int,2,10)
    fmt.Println(a,b)
    fmt.Println(len(a),len(b))
    fmt.Println(cap(a),cap(b))
    //输出如下
    [0,0] [0,0]
    2 2
    2 10
    ```

4. 使用和数组一样的偷懒的方法
    ```go
    a:=[]int{4:2}
    fmt.Println(a)
    fmt.Println(len(a),cap(a))
    //输出如下
    [0,0,0,0,2]
    5 5 
    ```
由于切片是引用类型，所以如果不对它赋值，它的零值是nil
```go
var arr []int
fmt.Println(arr==nil)
//true
```

数组与切片相同点：都可以容纳若噶类型相同的元素

数组与切片不同点：数组容器大小固定，切片是引用类型，可以append添加元素，更像python中的列表

```go
arr:=[]int{1}
//追加一个元素
arr=append(arr,2)
//追加多个元素
arr=append(arr,3,4)
//追加一个切片 ...不能省略 表示解包
arr=append(arr,[]int{7,8}...)
//在第一个位置插入一个元素,相当于将arr解包append到另一个切片上
arr=append([]int{0},arr...)
//在中间位置插入一个元素
arr=append(arr[:5],append([]int{0},arr[5:]...)...)
```

思考：为什么myslice长度为2却能够访问到第四个元素
```go
var numbers4 = [...]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
myslice := numbers4[4:6:8]
fmt.Printf("myslice为 %d, 其长度为: %d\n", myslice, len(myslice))

myslice = myslice[:cap(myslice)]
fmt.Printf("myslice的第四个元素为: %d", myslice[3])

//输出如下
myslice为 [5 6], 其长度为: 2
myslice的第四个元素为: 8

```
直接用索引进行访问是访问不到的，因为切片本身其实是一个指针，它指向了数组所在的位置

### 1.4 字典与布尔类型

字典由键值对构成，但是key不可以是切片、字典和函数，其他所有go的内建类型都可以作为key。声明字典：
`map[key_type]value_type`

**三种声明并初始化字典的方法：**
```go
    //第一种方法
    var scores map[string]int =map[string]int      {"english":56,"chinese":43}
    //第二种方法
    scores:=map[string]int{"english":56,"chinese":43}
    //第三种方法
    scores:=make(map[string]int)
    scores["english"]=80
    scores["chinese"]=32
    ```
    当然如果第一种方法拆成多步的话会比较麻烦
    ```go
    //第一步，声明字典
    var scores map[string]int
    //未初始化的字典零值为nil，无法直接赋值
    if scores ==nil{
        scores=make(map[string]int)
    }
    //经过初始化之后就可以直接惊醒赋值了
    scores["english"]=80
```

**字典的相关操作**

添加元素
```go 
scores["new_key"]=value 
```

读取元素，直接使用key作为索引，如果key不存在也不会报错，会返回其value-type的零值
```go
fmt.Println(scores["math"])
```

删除元素，使用delete函数，如果key不存在，会静默处理，不会报错
```go
delete(scores,"math")
```

**判断key是否存在**

无法根据返回的结果来判断对应的key是否存在，因为可能他的value就是零值。

字典的下标读取可以返回两个值，使用第二个返回值就表示对应的key是否存在
```go
scores:=map[string]int{"english":10,"chinese":100}
math,ok:=scores["math"]
if ok{
    fmt.Printf("math的值是：%d",math)
}
else{
    fmt.Println("math 不存在")
}
```
可以对上述代码进行一下优化
```go
    scores := map[string]int{"english": 80, "chinese": 85}
    if math, ok := scores["math"]; ok {
        fmt.Printf("math 的值是: %d", math)
    } else {
        fmt.Println("math 不存在")
    }
```

**对字典进行循环**

go中没有提供类似python的keys()、values()这样方便的函数，想要获取，必须自己循环

循环分为三种：

1. 获取key和value
   ```go
    for key,value :=range scores
   ```
2. 只获取key，这里不用占用符`_`
   ```go
    for key:=range scores
   ```
3. 只获取value，key用占位符代替
   ```go
    for _,scores:=range scores
   ```

**布尔类型**

在go语言中，true不但不与1相等，其规则更加严格，不同类型的变量无法进行比较。

如果要实现bool和int的转换，需要自己实现函数

### 1.5 指针

指针的创建有3种方法

1.  先定义对应的变量，再通过变量取得内存地址，创建指针
    ```go
    //定义普通变量
    aint:=1
    //定义指针变量
    ptr:=&aint
    ```
2. 先创建指针，分配好内存后，再向指针指向的内存地址写入对应的值
   ```go
    //创建指针
    astr:=new(string)
    //给指针赋值
    *astr="wierdo"
   ```
3. 先声明一个指针变量，再将其他变量的地址赋值给他
   ```go
    aint:=1
    var bint *int
    bint=&aint
   ```

想要打印指针指向的内存地址，方法有两种
```go
//第一种
fmt.Printf("%p",ptr)
//第二种
fmt.Println(ptr)
```

**指针的类型**

```go
    astr := "hello"
    aint := 1
    abool := false
    arune := 'a'
    afloat := 1.2

    fmt.Printf("astr 指针类型是：%T\n", &astr)
    fmt.Printf("aint 指针类型是：%T\n", &aint)
    fmt.Printf("abool 指针类型是：%T\n", &abool)
    fmt.Printf("arune 指针类型是：%T\n", &arune)
    fmt.Printf("afloat 指针类型是：%T\n", &afloat)

    //输出如下
    astr 指针类型是：*string
    aint 指针类型是：*int
    abool 指针类型是：*bool
    arune 指针类型是：*int32
    afloat 指针类型是：*float64
```

可以看出，*变量类型就是该变量对应的指针类型

指针的零值也为nil

**指针与切片**

切片和指针一样都是引用类型

如果想通过函数改变一个数组的值，有两种方法

1. 将这个数组的切片作为参数传给函数
2. 将这个数组的指针作为参数传给函数

按照go语言的习惯，通常使用第一种方法

**使用切片**
```go
func modify(sls []int){
    sls[0]=90
}
func main(){
    a:=[3]int{1,2,3}
    modify(a[:])
    fmt.Println(a)
}
```
**使用指针**
```go
func modify(ptr *[3]int){
    ptr[0]=90
}
func main(){
    a:=[3]int{1,2,3}
    modify(&a)
    fmt.Println(a)
}
```

### 1.6 流程控制：if-else

go里面的条件语句的模型是这样的
```
if 条件 1 {
  分支 1
} else if 条件 2 {
  分支 2
} else if 条件 ... {
  分支 ...
} else {
  分支 else
}
```
go中对于`{`和`}`的位置有严格的要求，他要求else if（或else）两边的花括号必须在同一行

由于go是强类型，所以条件表达式的返回值必须是布尔类型的（nil，0，1都不可以）

在if里允许先运行一个表达式，取得变量之后，再对其进行判断
```go
if age:=20;age>18{
    fmt.Println("已经成年了")
}
```

### 1.7 流程控制：switch-case

go里面的语句选择模型是这样的
```
switch 表达式 {
    case 表达式1:
        代码块
    case 表达式2:
        代码块
    case 表达式3:
        代码块
    case 表达式4:
        代码块
    case 表达式5:
        代码块
    default:
        代码块
}
```
用switch后的表达式分别和case的表达式比较，只要有一个满足，就会执行对应的代码块，然后退出switch-case，如果没有满足的，才会执行default

```go
education := "本科"

switch education {
case "博士":
    fmt.Println("我是博士")
case "研究生":
    fmt.Println("我是研究生")
case "本科":
    fmt.Println("我是本科生")
case "大专":
    fmt.Println("我是大专生")
case "高中":
    fmt.Println("我是高中生")
default:
    fmt.Println("学历未达标..")
```
一个case后面可以接多个条件，多个条件之间是或的关系，用逗号相隔

```go
month := 2

switch month {
case 3, 4, 5:
    fmt.Println("春天")
case 6, 7, 8:
    fmt.Println("夏天")
case 9, 10, 11:
    fmt.Println("秋天")
case 12, 1, 2:
    fmt.Println("冬天")
default:
    fmt.Println("输入有误...")
```

**case条件常量不可以重复**

当case后接的是常量时，该常量只能出现一次

错误案例1
```go
gender := "male"

switch gender {
    case "male":
        fmt.Println("男性")
    // 与上面重复
    case "male":
        fmt.Println("男性")
    case "female":
        fmt.Println("女性")
}
```
错误案例2
```go
gender := "male"

switch gender {
    case "male", "male":
        fmt.Println("男性")
    case "female":
        fmt.Println("女性")
}
```

**switch后面可以接函数**

switch后面可以接一个函数，只要保证case后的值与函数的返回值一致即可
```go
import "fmt"

//判断同学是否有挂科记录
func getResult(args ...int) bool{
    for _,i :=range args{
        if i <60{
            return false
        }
    }

    return true
}

func main() {
    chinese :=80
    english :=45
    math :=60

    switch getResult(chinese,english,math){
        case true:
            fmt.Println("全部合格")
        case false:
            fmt.Println("有挂科")
    }
}
```

**switch可以不接表达式**

不接任何东西时，就相当于if-elseif-else
```go
score := 30

switch {
    case score >= 95 && score <= 100:
        fmt.Println("优秀")
    case score >= 80:
        fmt.Println("良好")
    case score >= 60:
        fmt.Println("合格")
    case score >= 0:
        fmt.Println("不合格")
    default:
        fmt.Println("输入有误...")
}
```

**switch的穿透能力**

通常case执行完会直接break，但是再case段代码末尾加上fallthrough就可以穿透下一个case
```go
s := "hello"
switch {
case s == "hello":
    fmt.Println("hello")
    fallthrough
case s != "world":
    fmt.Println("world")
}
//输出如下
hello
world
```

### 1.8 流程控制：for循环

for循环的基本模型
```go
for [condition |  ( init; condition; increment ) | Range]
{
   statement(s);
}
```

可以看出有三种情况
1. 接一个条件表达式
   ```go
    a:=1
    for a<=5{
        fmt.Println(a)
        a++
    }
    //会输出1-5
   ```
2. 接3个表达式
   ```go
    for i:=1;i<=5;i++{
        fmt.Println(i)
    }
   ```
3. 不接表达式
   go语言中没有while，无限循环可以用for来实现

   不加判断条件就默认为true，但是一般不会无限循环，可以在满足某个条件的时候break或者continue跳到下一个循环

   无限循环的两种写法
   ```go
    for {

    }

    for ;;{

    }
   ```

**for-range语句**

range会返回两个值：索引和数据，若后面用不到索引的话，需要用_来获取索引

```go
arr:=[...]string{"zhou","ying","see-you"}
for _,item in range arr{
    fmt.Println(item)
}
```

### 1.9 goto无条件跳转

goto后接一个标签，标签的意义是告诉程序下一步需要执行哪里的代码，所以标签如何放置，放置在哪里是goto需要注意的

```go
goto flag
fmt.Println('A')
flag:
    fmt.Println('B')
```
上面的代码只会输出B而不会输出A

### 1.10 defer延迟调用
用法很简单，defer后面跟一个函数，只有当前函数执行完成后，再执行defer后跟着的函数

```go
import "fmt"

func myfunc() {
    fmt.Println("B")
}

func main() {
    defer myfunc()
    fmt.Println("A")
}

//输出如下
A
B
```

由于defer只是延迟调用函数，所以传递给该函数里的变量，不会受到后续程序的影响。就好像给变量做了一个副本先保存。

```go
import "fmt"

func main() {
    name := "go"
    defer fmt.Println(name) // 输出: go

    name = "python"
    fmt.Println(name)      // 输出: python
}
//输出如下
python
go
```

注意：如果defer后面跟的是匿名函数，情况会有所不同，defer会取到最后的变量值
```go
name:="weirdo"
defer func(){
    fmt.Println(name)
}()
name="zhang"
fmt.Println(name)
```
**多个defer反序调用**

若是再一个函数里使用了多个defer，那么这些defer的执行函数是什么样的呢？

```go
name:="go"
defer fmt.Println(name)

name="python"
defer fmt.Println(name)

name="java"
defer fmt.Println(name)

//输出如下
java
python
go
```
这说明多个defer的调用是反序的，类似于栈，先进后出

而且defer是在return之后才会调用的

defer的重要作用是可以做上下文管理的文件打开的时候，直接defer文件关闭，这样这个函数执行结束的时候会自动关闭文件。类似于python的with open

### 1.11 流程控制：理解select用法
他跟switch-case很像，但是又有不同的select-case

他仅能用于信道/通道的相关操作

```go
select {
    case 表达式1:
        <code>
    case 表达式2:
        <code>
  default:
    <code>
}
```

最简单的例子
先创建两个信道，并且在select前往c2发送数据
```go
c1:=make(chan string,1)
c2:=make(chan string,1)

c2<-"hello"
select{
    case msg1:=<-c1:
        fmt.Println("c1 received:",msg1)
    case msg2 :=<-c2:
        fmt.Println("c2 received:",msg2)
    default:
        fmt.Println("No data received")
}
```

select在执行过程中，必须命中某一个分支，如果没有写default的话，就会阻塞，直到某个case可以命中，而如果一直没有命中的话，select就会抛出deadlock的错误

### 1.12 异常机制：panic和recover

通常程序发生错误时会引发程序的退出，但是我们也可以手动触发程序的退出，在我们判断当前环境无法完成我们的程序的时候，可以手动触发panic，让程序退出运行

```go
panic("crash")
```
**捕获panic**
发生异常时需要捕获，这就要引出另一个内建函数`recover`,他可以让程序宕机之后起死回生

但是revocer一定要在defer函数中才能够生效，其他作用域下他不会生效
```go
func set_data(x int){
    defer func(){
        //recover可以将捕获到的panic信息打印
        if err :=recover();err!=nil{
            fmt.Println(err)
        }
    }()

    //故意制造数组越界，触发panic
    var arr [10]int
    arr[x]=88
}

func main(){
    set_data(20)

    //如果能运行到这一句说明pannic被捕获了
    //后续程序能够正常运行
    fmt.Println("everything is ok")
}
```

通常来说，不应该对进入 panic 宕机的程序做任何处理，但有时，需要我们可以从宕机中恢复，至少我们可以在程序崩溃前，做一些操作，举个例子，当 web 服务器遇到不可预料的严重问题时，在崩溃前应该将所有的连接关闭，如果不做任何处理，会使得客户端一直处于等待状态，如果 web 服务器还在开发阶段，服务器甚至可以将异常信息反馈到客户端，帮助调试。

但是这个defer在多个协程里面是没有效果的，在子协程触发panic，只能触发自己携程内的defer，不能调用main协程里的defer
```go
import (
    "fmt"
    "time"
)

func main() {
    // 这个 defer 并不会执行
    defer fmt.Println("in main")

    go func() {
        defer println("in goroutine")
        panic("")
    }()

    time.Sleep(2 * time.Second)
}

//输出如下
in goroutine
panic:
```

## 第二章 面向对象
### 2.1 结构体与继承
go语言中没有class类的概念，只有struct结构体，因此也没有继承

声明结构体
```go
type my_struct struct{
    a int
    b float
    ...
}
```

**规则1：**当最后一个字段和`}`不在同一行时，`,`不可以省略 反之则可以
```go
xm := Profile{
    name: "小明",
    age: 18,
    gender: "male",
}

xm := Profile{
    name: "小明",
    age: 18,
    gender: "male"}
```
**规则2：**字段名要么全写，要么全不写，不能有的写有的不写
```go
//这种写法是错误的
xm := Profile{
    name: "小明",
    18,
    "male",
}
```
**规则3：**初始化结构体不一定所有字段都赋值，未赋值的字段会自动初始化为其零值

**绑定方法**

无法在结构体内定义方法，需要使用组合函数的方式来定义结构体方法
```go
func (person Profile) FmtProfile() {
    fmt.Printf("名字：%s\n", person.name)
    fmt.Printf("年龄：%d\n", person.age)
    fmt.Printf("性别：%s\n", person.gender)
}
```
其中`FmProfile`是方法名，而(person Profile) ：表示将 FmtProfile 方法与 Profile 的实例绑定。我们把 Profile 称为方法的接收者，而 person 表示实例本身，它相当于 Python 中的 self，在方法内可以使用 person.属性名 的方法来访问实例属性。
```go
package main

import "fmt"

// 定义一个名为Profile 的结构体
type Profile struct {
    name   string
    age    int
    gender string
    mother *Profile // 指针
    father *Profile // 指针
}

// 定义一个与 Profile 的绑定的方法
func (person Profile) FmtProfile() {
    fmt.Printf("名字：%s\n", person.name)
    fmt.Printf("年龄：%d\n", person.age)
    fmt.Printf("性别：%s\n", person.gender)
}

func main() {
    // 实例化
    myself := Profile{name: "小明", age: 24, gender: "male"}
    // 调用函数
    myself.FmtProfile()
}

//输出如下
名字：小明
年龄：24
性别：male
```

当想要在方法内改变实例的属性的时候，必须使用指针作为方法的接收者
```go
package main

import "fmt"

// 声明一个 Profile 的结构体
type Profile struct {
    name   string
    age    int
    gender string
    mother *Profile // 指针
    father *Profile // 指针
}

// 重点在于这个星号: *
func (person *Profile) increase_age() {
    person.age += 1
}

func main() {
    myself := Profile{name: "小明", age: 24, gender: "male"}
    fmt.Printf("当前年龄：%d\n", myself.age)
    myself.increase_age()
    fmt.Printf("当前年龄：%d", myself.age)
}
```
不管你使用哪种方法定义方法，指针实例对象、值实例对象都可以直接调用属性，而没有什么约束。这一点Go语言做得非常好。

**结构体实现“继承”**

go语言本身不支持继承，但可以用组合的方法，实现类似继承的效果

把一个结构体嵌入到另一个结构体的方法，称之为组合

这里有一个表示公司（company）和员工（staff）的结构体
```go
type company struct{
    companyName string
    companyAddr string
}
type staff struct{
    name string
    age int 
    gender string
    position string
}
```
可以将 company 这个 结构体嵌入到 staff 中，做为 staff 的一个匿名字段，staff 就直接拥有了 company 的所有属性了。
```go
type staff struct{
    name string
    age int 
    gender string
    position string
    company
}
```
可以用下面这个例子理解一下
```go
import "fmt"

type company struct {
    companyName string
    companyAddr string
}

type staff struct {
    name string
    age int
    gender string
    position string
    company
}

func main()  {
    myCom := company{
        companyName: "Tencent",
        companyAddr: "深圳市南山区",
    }
    staffInfo := staff{
        name:     "小明",
        age:      28,
        gender:   "男",
        position: "云计算开发工程师",
        company: myCom,
    }

    fmt.Printf("%s 在 %s 工作\n", staffInfo.name, staffInfo.companyName)
    fmt.Printf("%s 在 %s 工作\n", staffInfo.name, staffInfo.company.companyName)
}
```
输出结果如下，可以看出`staffInfo.companyName`和`staffInfo.company.companyName`的效果是一样的
```
小明 在 Tencent 工作
小明 在 Tencent 工作
```

**内部方法和外部方法**
在go语言中，函数首字母的大小写非常重要，它用来实现控制对方法的访问权限
* 方法的首字母大写时，这个方法对于所有的包都是public，其他包可以随意调用
* 当方法的首字母小写时，这个方法时private的，其他包无法访问

### 2.2 接口与多态
在面向对象的领域里，接口一般这样定义：接口定义一个对象的行为。接口只指定了对象应该做什么，至于如何实现这个行为（即实现细节），则由对象本身去确定。

在 Go 语言中，接口就是方法签名（Method Signature）的集合。当一个类型定义了接口中的所有方法，我们称它实现了该接口。这与面向对象编程（OOP）的说法很类似。接口指定了一个类型应该具有的方法，并由该类型决定如何实现这些方法。

**如何定义接口**

使用type关键字来定义接口

下面的代码定义了一个电话接口，接口要求必须实现call方法
```go
type phone interface{
    call()
}
```
**如何实现接口**

如果有一个类型/结构体，实现了一个接口要求的所有方法，这里 Phone 接口只有 call方法，所以只要实现了 call 方法，我们就可以称它实现了 Phone 接口。

意思是如果有一台机器，可以给别人打电话，那么我们就可以把它叫做电话。

这个接口的实现是隐式的，不像 JAVA 中要用 implements 显示说明。

继续上面电话的例子，我们先定义一个 Nokia 的结构体，而它实现了 call 的方法，所以它也是一台电话。

```go
type Iphone struct{
    name string
}

//接收者为iphoe
func (phone Iphone) call(){
    fmt.Println("我是iphone，一台电话")
}
```
**接口实现多态**

不同的人标准不一，有的人认为必须有一定的学历，有的人认为必须要有老师资格证。

而我认为只要能育人，能给传授给其他人知识的，都可以称之为老师。

而不管你教的什么学科？是体育竞技，还是教人烹饪。

也不管你怎么教？是在教室里手执教教鞭、拿着粉笔，还是追求真实，直接实战演练。

通通不管。

这就一个接口（老师）下，在不同对象（人）上的不同表现。这就是多态。

在go语言中，通过接口实现多态

```go
//先定义一个商品的接口
type good interface{
    settleAccount() int
    orderInfo() string
}
//在定义一个电话结构体和赠品结构体
type phone struct{
    name string
    quantity int
    price int
}
type freeGift interface{
    name string
    quantity int
    price int
}

//然后分别为他们实现good接口的两个方法
//phone
func (phone phone) settleAccount() int{
    return phone.quantity*phone.price
}
func (phone phone) orderInfo() int{
    return "您要购买"+strconv.Itoa(phone.quantity)+"个"+phone.name+"计："+strconv.Itoa(phone.settleAccount())+"元"
}
//freeGift
func (gift FreeGift) settleAccount() int {
    return 0
}
func (gift FreeGift) orderInfo() string{
    return "您要购买" + strconv.Itoa(gift.quantity)+ "个" +gift.name + "计：" + strconv.Itoa(gift.settleAccount()) + "元"
}
```
实现了Good接口要求的两个方法后，手机和赠品在go语言看来就都是商品类型了

这时候挑选两件商品（实例化），分别为手机和耳机（耳机时赠品，不要钱）
```go
iphone:=phone{
    name:"iphoneX",
    quantity:1,
    price:8000,
}
earphone:=freeGift{
    name:"beats solo3",
    quantity:1,
    price:200,
} 
```
然后创建一个购物车（也就是类型为good的切片，来存放这些商品）
```go
goods:=[]Good{iphone,earphone}
```
最后，定义一个方法来计算购物车里的金额
```go
func calculationAllPrice(goods []Good){
    var allPrice int
    for _,good:=range goods{
        fmt.Println(good.orderInfo())
        allPrice+=good.settleAccount()
    }
    return allPrice
}
```
运行之后，输出如下
```
您要购买1个iPhone计：8000元
您要购买1个耳机计：0元
该订单总共需要支付 8000 元
```

### 2.3 go语言中的空接口
空接口时特殊接口，没有定义任何方法，因此，我们也可以说所有类型都至少实现了空接口

```go
type empty_iface interface{

}
```
**如何使用空接口**

1. 通常我们会直接使用interface{}作为哦类型声明的一个实例，它可以承载任何类型的值
```go
    package main

import (
    "fmt"
)

func main()  {
    // 声明一个空接口实例
    var i interface{}

    // 存 int 没有问题
    i = 1
    fmt.Println(i)

    // 存字符串也没有问题
    i = "hello"
    fmt.Println(i)

    // 存布尔值也没有问题
    i = false
    fmt.Println(i)
}
```
2. 如果想让函数接收任意类型的值，也可以使用空接口接受任意类型的值
   
   接收一个任意类型的值
   ```go
    func myfunc(iface interface{}){
        fmt.Println(iface)
    }
    func main(){
        a:=10
        b:="hello"
        c:=true

        myfunc(a)
        myfunc(b)
        myfunc(c)
    }
   ```
   接受任意个任意类型的值
   ```go
    func myfunc(ifaces ...interface{}){
        for _,iface :=range ifaces{
            fmt.Println(iface)
        }
        func main(){
            a:=10
            b:="hello"
            c:=true

            myfunc(a,b,c)
        }
    }
   ```
3. 也可以定义一个可以接收任何类型的array、slice、map、struct
   ```go
    any:=make([]interface{},5)
    any[0] =11
    any[1]="hello world"
    any[2]=[]int{1,2,3,4,5}
    for _,value :=range any{
        fmt.Println(value)
    }
   ```
**空接口的几个要注意的坑**
1. 空接口可以承载任何值，但是不代表任意类型都可以承接口接口
2. 空接口承载数组和切片之后，该对象无法再进行切片
3. 当使用空接口接收任意类型时，它的静态类型是interface{},但是动态类型(int,float或者其他)我们并不知道，因此需要类型断言
```go
    package main

import (
    "fmt"
)

func myfunc(i interface{})  {

    switch i.(type) {
    case int:
        fmt.Println("参数的类型是 int")
    case string:
        fmt.Println("参数的类型是 string")
    }
}

func main() {
    a := 10
    b := "hello"
    myfunc(a)
    myfunc(b)
}

//输出如下
参数的类型是 int
参数的类型是 string
```

### 2.4 接口的三个潜规则
**对方法的调用限制**
```go
package main

import "fmt"

type Phone interface {
    call()
}

type iPhone struct {
    name string
}

func (phone iPhone)call()  {
    fmt.Println("Hello, iPhone.")
}

func (phone iPhone)send_wechat()  {
    fmt.Println("Hello, Wechat.")
}

func main() {
    var phone Phone
    phone = iPhone{name:"ming's iphone"}
    phone.call()
    phone.send_wechat()
}
```
这里调用`phone.send_wechat`的时候会报错，因为我们显式地声明了phone对象为Phone接口，这会导致其受到接口的限制。

解决方案也很简单，可以不显式地声明为phone接口类型，但要清楚phone对象实际上隐式地实现了phone接口。

只需要修改main方法如下就可以了
fuc main(){
    phone:=iPhone{name:"weirdo's iphone"}
    phone.call()
    phone.send_wechat()
}

go语言中的函数调用都是值传递的，变量会在方法调用前进行类型转换

```go
import (
    "fmt"
)

func printType(i interface{})  {

    switch i.(type) {
    case int:
        fmt.Println("参数的类型是 int")
    case string:
        fmt.Println("参数的类型是 string")
    }
}

func main() {
    a := 10
    printType(a)
}
```
这段代码运行后一切正常
```
参数的类型是 int
```

但是如果把函数的内容搬到外面
```go
package main

import "fmt"


func main() {
    a := 10

    switch a.(type) {
    case int:
        fmt.Println("参数的类型是 int")
    case string:
        fmt.Println("参数的类型是 string")
    }
}
```
就会报错

原因很简单，当函数接口interface{}空接口类型时，我们可以说他能接收任意类型，但接收到了之后，会隐式的将其转换为interface{}类型

那我们就可以通过对变量的显示转换来在main中完成这一操作而不非要依赖外部的函数
```go
package main

import "fmt"


func main() {
    a := 10

    switch interface{}(a).(type) {
    case int:
        fmt.Println("参数的类型是 int")
    case string:
        fmt.Println("参数的类型是 string")
    }
}

```

### 2.5 详解类型断言
Type Assertion可以做到
* 检查`i`是否为nil
* 检查`i`存储的值是否为某个类型

具体的使用方法有两种

第一种
```go
t:=i.(T)
```
这个表达式可以断言一个接口对象（i）里不是 nil，并且接口对象（i）存储的值的类型是 T，如果断言成功，就会返回值给 t，如果断言失败，就会触发 panic。
```go
package main

import "fmt"

func main() {
    var i interface{} = 10
    t1 := i.(int)
    fmt.Println(t1)

    fmt.Println("=====分隔线=====")

    t2 := i.(string)
    fmt.Println(t2)
}
```
第二种
```go
t, ok:= i.(T)
```
和上面一样，这个表达式也是可以断言一个接口对象（i）里不是 nil，并且接口对象（i）存储的值的类型是 T，如果断言成功，就会返回其值给 t，并且此时 ok 的值 为 true，表示断言成功。

如果接口值的类型，并不是我们所断言的 T，就会断言失败，但和第一种表达式不同的事，这个不会触发 panic，而是将 ok 的值设为 false ，表示断言失败，此时t 为 T 的零值。

```go
package main

import "fmt"

func main() {
    var i interface{} = 10
    t1, ok := i.(int)
    fmt.Printf("%d-%t\n", t1, ok)

    fmt.Println("=====分隔线1=====")

    t2, ok := i.(string)
    fmt.Printf("%s-%t\n", t2, ok)

    fmt.Println("=====分隔线2=====")

    var k interface{} // nil
    t3, ok := k.(interface{})
    fmt.Println(t3, "-", ok)

    fmt.Println("=====分隔线3=====")
    k = 10
    t4, ok := k.(interface{})
    fmt.Printf("%d-%t\n", t4, ok)

    t5, ok := k.(int)
    fmt.Printf("%d-%t\n", t5, ok)
}
```
**Type Switch**
如果需要区分多种类型的话，可以使用type switch断言，这比一个一个来更加简单高效
```go
package main

import "fmt"

func findType(i interface{}) {
    switch x := i.(type) {
    case int:
        fmt.Println(x, "is int")
    case string:
        fmt.Println(x, "is string")
    case nil:
        fmt.Println(x, "is nil")
    default:
        fmt.Println(x, "not type matched")
    }
}

func main() {
    findType(10)      // int
    findType("hello") // string

    var k interface{} // nil
    findType(k)

    findType(10.23) //float64
}
```
输出如下
```
10 is int
hello is string
<nil> is nil
10.23 not type matched
```
**注意：**

* 如果值是nil，匹配的是case nil
* 如果值在分支里没有匹配到，那对应的是default



### 2.6 结构体里的Tag标签
定义结构体的时候可以在属性字段之外再额外增加一个属性，用反引号包含，称之为tag
```go
type Person struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
    Addr string `json:"addr,omitempty"`
}
```
```go
package main

import (
    "encoding/json"
    "fmt"
)

type Person struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
    Addr string `json:"addr,omitempty"`
}

func main() {
    p1 := Person{
        Name: "Jack",
        Age:  22,
    }

    data1, err := json.Marshal(p1)
    if err != nil {
        panic(err)
    }

    // p1 没有 Addr，就不会打印了
    fmt.Printf("%s\n", data1)

    // ================

    p2 := Person{
        Name: "Jack",
        Age:  22,
        Addr: "China",
    }

    data2, err := json.Marshal(p2)
    if err != nil {
        panic(err)
    }

    // p2 则会打印所有
    fmt.Printf("%s\n", data2)
}
```
由于 Person 结构体里的 Addr 字段有 omitempty 属性，因此 encoding/json 在将对象转化 json 字符串时，只要发现对象里的 Addr 为 false， 0， 空指针，空接口，空数组，空切片，空映射，空字符串中的一种，就会被忽略。

因此运行之后，输出的结果如下：
```
{"name":"Jack","age":22}
{"name":"Jack","age":22,"addr":"China"}
```

获取tag可以分为三个步骤
* 获取字段field
* 获取标签tag
* 获取键值对key:value
  
```go
//三种方法获取field

```

### 2.7 反射三定律
* 反射可以将接口类型变量转换为“反射类型对象”
* 反射可以将“反射类型对象”转换为接口类型对象
* 如果要修改“反射类型对象”其类型必须是可写的

**第一定律**

接口类型变量转换为反射类型对象

为了实现接口变量到反射对象的转换，需要提到reflect包里很重要的两个方法
1. reflect.TypeOf(i):获得接口值的类型
2. reflect.ValueOf(i):获得接口的值
```go
package main

import (
"fmt"
"reflect"
)

func main() {
    var age interface{} = 25

    fmt.Printf("原始接口变量的类型为 %T，值为 %v \n", age, age)

    t := reflect.TypeOf(age)
    v := reflect.ValueOf(age)

    // 从接口变量到反射对象
    fmt.Printf("从接口变量到反射对象：Type对象的类型为 %T \n", t)
    fmt.Printf("从接口变量到反射对象：Value对象的类型为 %T \n", v)

}
```
输出如下
```
原始接口变量的类型为 int，值为 25
从接口变量到反射对象：Type对象的类型为 *reflect.rtype
从接口变量到反射对象：Value对象的类型为 reflect.Value
```
**第二定律**

反射对象转换为接口对象

```go
package main

import (
"fmt"
"reflect"
)

func main() {
    var age interface{} = 25

    fmt.Printf("原始接口变量的类型为 %T，值为 %v \n", age, age)

    t := reflect.TypeOf(age)
    v := reflect.ValueOf(age)

    // 从接口变量到反射对象
    fmt.Printf("从接口变量到反射对象：Type对象的类型为 %T \n", t)
    fmt.Printf("从接口变量到反射对象：Value对象的类型为 %T \n", v)

    // 从反射对象到接口变量
    i := v.Interface()
    fmt.Printf("从反射对象到接口变量：新对象的类型为 %T 值为 %v \n", i, i)

}
```
输出如下
```
原始接口变量的类型为 int，值为 25
从接口变量到反射对象：Type对象的类型为 *reflect.rtype
从接口变量到反射对象：Value对象的类型为 reflect.Value
从反射对象到接口变量：新对象的类型为 int 值为 25
```
**第三定律**

如果要修改反射对象，其值必须是可写类型

在反射的规则里
* 不是接收变量指针创建的反射对象是不具备可写性的
* 是否既有可写性可以通过`CanSet()`来获取得知
* 对不具备可写性的对象进行修改，是没有意义的，会报错
```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var name string = "Go编程时光"

    v := reflect.ValueOf(name)
    fmt.Println("可写性为:", v.CanSet())
}
//输出如下
可写性为: false

```
要让反射对象具备可写性，需要注意两点
1. 创建反射对象的时候传入变量的指针
2. 使用Elem()函数返回指针指向的数据
```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var name string = "Go编程时光"
    v1 := reflect.ValueOf(&name)
    fmt.Println("v1 可写性为:", v1.CanSet())

    v2 := v1.Elem()
    fmt.Println("v2 可写性为:", v2.CanSet())
}
```

知道具有可写性之后，需要了解一下如何对他进行修改更新

反射对象都会有几个以`Set`单词开头的方法，这些方法就是我们修改值的入口
```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var name string = "Go编程时光"
    fmt.Println("真实世界里 name 的原始值为：", name)

    v1 := reflect.ValueOf(&name)
    v2 := v1.Elem()

    v2.SetString("Python编程时光")
    fmt.Println("通过反射对象进行更新后，真实世界里 name 变为：", name)
}
```
输出如下
```
真实世界里 name 的原始值为： Go编程时光
通过反射对象进行更新后，真实世界里 name 变为： Python编程时光
```

### 2.8 全面学习反射的函数
**获取类别：Kind()**

Type 对象 和 Value 对象都可以通过 Kind() 方法返回对应的接口变量的基础类型。

Kind函数如何使用

第一种：传入值
```go
package main

import (
    "fmt"
    "reflect"
)

type Profile struct {
    name string
    age int
    gender string
}

func main() {
    m := Profile{}

    t := reflect.TypeOf(m)
    fmt.Println("Type: ",t)
    fmt.Println("Kind: ",t.Kind())
}
```
输出如下
```
Type:  main.Profile
Kind:  struct
```

第二种：传入指针
```go
package main

import (
    "fmt"
    "reflect"
)

type Profile struct {
    name string
    age int
    gender string
}

func main() {
    m := Profile{}

    t := reflect.TypeOf(&m)

    fmt.Println("&m Type: ",t)
    fmt.Println("&m Kind: ",t.Kind())

    fmt.Println("m Type: ",t.Elem())
    fmt.Println("m Kind: ",t.Elem().Kind())
}
```
输出如下
```
&m Type:  *main.Profile
&m Kind:  ptr
m Type:  main.Profile
m Kind:  struct
```
如果这里不用TypeOf而是使用ValueOf
```go
package main

import (
    "fmt"
    "reflect"
)

type Profile struct {
    name string
    age int
    gender string
}

func main() {
    m := Profile{}

    v := reflect.ValueOf(&m)

    fmt.Println("&m Type: ",v.Type())
    fmt.Println("&m Kind: ",v.Kind())

    fmt.Println("m Type: ",v.Elem().Type())
    fmt.Println("m Kind: ",v.Elem().Kind())
}
```

**进行类型的转换**

使用Int()函数将值转换为int类型
```go
package main

import (
    "fmt"
    "reflect"
)

func main() {

    var age int = 25

    v1 := reflect.ValueOf(age)
    fmt.Printf("转换前， type: %T, value: %v \n", v1, v1)
    v2 := v1.Int()
    fmt.Printf("转换后， type: %T, value: %v \n", v2, v2)
}
```
输出如下
```
转换前， type: reflect.Value, value: 25
转换后， type: int64, value: 25
```

其他float、bool、interface、pointer等的操作跟这个是一样的就不多做赘述了

**对切片的操作**

切片操作与上述的操作都不一样，他返回的还是reflect.Value反射对象，而不是真实世界中的切片对象

**Slice():对切片再切片(两下标)**

```go
package main

import (
    "fmt"
    "reflect"
)

func main() {

    var numList []int = []int{1,2}

    v1 := reflect.ValueOf(numList)
    fmt.Printf("转换前， type: %T, value: %v \n", v1, v1)

    // Slice 函数接收两个参数
    v2 := v1.Slice(0, 2)
    fmt.Printf("转换后， type: %T, value: %v \n", v2, v2)
}
```
**Slice3():对切片再切片(三下标)**

和两下标的函数一样，都是对一个切片的反射对象

**Set()和Append():更新切片**

```go
package main

import (
    "fmt"
    "reflect"
)

func appendToSlice(arrPtr interface{}) {
    valuePtr := reflect.ValueOf(arrPtr)
    value := valuePtr.Elem()

    value.Set(reflect.Append(value, reflect.ValueOf(3)))

    fmt.Println(value)
    fmt.Println(value.Len())
}

func main() {
    arr := []int{1,2}

    appendToSlice(&arr)

    fmt.Println(arr)
}
```
输出如下
```
3
[1 2 3]
[1 2 3]
```

**对属性的操作**

NumField()和Field()
```go
package main

import (
    "fmt"
    "reflect"
)

type Person struct {
    name string
    age int
    gender string
}

func (p Person)SayBye()  {
    fmt.Println("Bye")
}

func (p Person)SayHello()  {
    fmt.Println("Hello")
}



func main() {
    p := Person{"写代码的明哥", 27, "male"}

    v := reflect.ValueOf(p)

    fmt.Println("字段数:", v.NumField())
    fmt.Println("第 1 个字段：", v.Field(0))
    fmt.Println("第 2 个字段：", v.Field(1))
    fmt.Println("第 3 个字段：", v.Field(2))

    fmt.Println("==========================")
    // 也可以这样来遍历
    for i:=0;i<v.NumField();i++{
        fmt.Printf("第 %d 个字段：%v \n", i+1, v.Field(i))
    }
}
```
输出如下
```
字段数: 3
第 1 个字段： 写代码的明哥
第 2 个字段： 27
第 3 个字段： male
==========================
第 1 个字段：写代码的明哥
第 2 个字段：27
第 3 个字段：male
```

**对方法的操作**

NumMethod()和Method()
```go
package main

import (
    "fmt"
    "reflect"
)

type Person struct {
    name string
    age int
    gender string
}

func (p Person)SayBye()  {
    fmt.Println("Bye")
}

func (p Person)SayHello()  {
    fmt.Println("Hello")
}



func main() {
    p := &Person{"写代码的明哥", 27, "male"}

    t := reflect.TypeOf(p)

    fmt.Println("方法数（可导出的）:", t.NumMethod())
    fmt.Println("第 1 个方法：", t.Method(0).Name)
    fmt.Println("第 2 个方法：", t.Method(1).Name)

    fmt.Println("==========================")
    // 也可以这样来遍历
    for i:=0;i<t.NumMethod();i++{
       fmt.Printf("第 %d 个方法：%v \n", i+1, t.Method(i).Name)
    }
}
```
输出如下
```
方法数（可导出的）: 2
第 1 个方法： SayBye
第 2 个方法： SayHello
==========================
第 1 个方法：SayBye
第 2 个方法：SayHello
```

**动态调用函数（使用索引且无参数）**
```go
package main

import (
    "fmt"
    "reflect"
)

type Person struct {
    name string
    age int
}

func (p Person)SayBye() string {
    return "Bye"
}

func (p Person)SayHello() string {
    return "Hello"
}


func main() {
    p := &Person{"wangbm", 27}

    t := reflect.TypeOf(p)
    v := reflect.ValueOf(p)


    for i:=0;i<v.NumMethod();i++{
       fmt.Printf("调用第 %d 个方法：%v ，调用结果：%v\n",
           i+1,
           t.Method(i).Name,
           v.Elem().Method(i).Call(nil))
    }
}

//输出如下
调用第 1 个方法：SayBye ，调用结果：[Bye]
调用第 2 个方法：SayHello ，调用结果：[Hello]
```

**动态调用函数（使用函数名且无参数）**
```go
package main

import (
    "fmt"
    "reflect"
)

type Person struct {
    name string
    age int
    gender string
}

func (p Person)SayBye()  {
    fmt.Print("Bye")
}

func (p Person)SayHello()  {
    fmt.Println("Hello")
}



func main() {
    p := &Person{"写代码的明哥", 27, "male"}

    v := reflect.ValueOf(p)

    v.MethodByName("SayHello").Call(nil)
    v.MethodByName("SayBye").Call(nil)
}
```

**动态调用函数（使用函数且有参数）**
```go
package main

import (
    "fmt"
    "reflect"
)

type Person struct {
}

func (p Person)SelfIntroduction(name string, age int)  {
    fmt.Printf("Hello, my name is %s and i'm %d years old.", name, age)
}



func main() {
    p := &Person{}

    //t := reflect.TypeOf(p)
    v := reflect.ValueOf(p)
    name := reflect.ValueOf("wangbm")
    age := reflect.ValueOf(27)
    input := []reflect.Value{name, age}
    v.MethodByName("SelfIntroduction").Call(input)
}
```
输出如下
```
Hello, my name is wangbm and i'm 27 years old.
```

### 2.9 make和new的区别

new函数做的事
* 分配内存
* 设置零值
* 返回指针（重要）
```go
import "fmt"

type Student struct {
   name string
   age int
}

func main() {
    // new 一个内建类型
    num := new(int)
    fmt.Println(*num) //打印零值：0

    // new 一个自定义类型
    s := new(Student)
    s.name = "wangbm"
}
```

make函数做的事
1. 用来为slice、map或者chan类型（只能用在这三个上）分配内存和初始化一个对象
2. make返回类型的本身而不是指针，而返回值也依赖于具体传入的类型，因为这三种类型就是引用类型，所以不用返回指针

因为这三种类型是引用类型，所以必须要初始化（size和cap），但不是置为零值，这是和new的区别

```go
//切片
a := make([]int, 2, 10)

// 字典
b := make(map[string]int)

// 通道
c := make(chan int, 10)
```

### 2.10 面向对象：go语言中的空结构体
空结构体和正常结构体一样，可以接收方法函数
```go
typt Lamp struct{}
func (l Lamp) On(){
    println("On")
}
func(l Lamp) Off(){
    println("Off")
}
```
**空结构体的妙用**

空结构体的特征就是没有属性，更确切地说，他不占用空间
```go
type Lamp struct{}

func main() {
    lamp := Lamp{}
    fmt.Print(unsafe.Sizeof(lamp))
}
// output: 0
```
而且这一特性和结构体是否有接收函数是没有关系的
```go
type Lamp struct{}

func (l Lamp) On ()  {
    fmt.Println("On...")
}

func main() {
    lamp := Lamp{}
    fmt.Print(unsafe.Sizeof(lamp))
}
// output: 0
```
这个特性在特殊情况下可以用作占位符使用，减少程序的内存占用

比如用信道控制并发的时候，我们只需要一个信号，不需要值，就可以用struct{}替代
```go
func main() {
    ch := make(chan struct{}, 1)
    go func() {
        <-ch
        // do something
    }()
    ch <- struct{}{}
    // ...
}
```

## 第三章 项目管理
### 3.1 依赖管理：包导入的重要知识点
**使用点操作**

如果我们程序中有个包经常用到，每次都要包名＋方法名很烦，可以import的时候加个.，这就是我们自己的方法了
```go
import . "fmt"

func main() {
    Println("hello, world")
}
```
但是这个方法有个缺点，就是导入的包里的函数可能会与我们自己命名的函数有冲突

**包的初始化**

每个包都有`init`函数，当被导入时，会执行这个函数

对于`init`函数有几个点需要注意
1. `init`函数优先于`main`函数执行
2. 包引用链中，包的初始化是深度优先的。比如引用关系：main-A-B-C那么初始化顺序为C-B-A-main
3. 同一个包甚至同一个源文件，可以有多个init函数
4. init函数不能有入参和返回值
5. init函数不能被其他函数调用
6. 同一个包内的多个ini函数顺序不受保证
7. init之前会先初始化包的作用域的常量和变量（常量优先于变量）
```go
package main

import "fmt"

func init()  {
 fmt.Println("init1:", a)
}

func init()  {
 fmt.Println("init2:", a)
}

var a = 10
const b = 100

func main() {
 fmt.Println("main:", a)
}
// 执行结果
// init1: 10
// init2: 10
// main: 10
```
**包的匿名导入**

导入包时，如果包没被用到，会报错。

但是我们只是想要这个包的init函数运行一下初始化，这时就可以用匿名导入。用下划线表示不能被访问
```go
import _"image/png"
```
import导入的是个目录，但是目录下的包名往往是跟目录的名字是一样的，所以会有导入的是个包的错觉

### 3.2 Go语言中的编码规范
**文件命名**

1. 文件名一律小写
2. 不同单词用下划线分词，不要用驼峰
3. 测试文件用_test.go
4. 若具有平台特性要用`文件名_平台.go`
5. 一般来说应用的主入口为main.go，或者用全小写形式命名，比如MyBlog的入口可以为myblog.go

**常量命名**

主流有两种
1. 驼峰
2. 全大写且用下划线分词

推荐使用第二种

**变量命名**

统一使用驼峰
1. 在相对简单环境下，完整单词可以简写为单个字母，如user可写为u
2. 若变量为bool，则应该以`has`、`is`、`can`或者`allow`开头
3. 其他情况一般第一个单词小写，后面单词首字母大写
4. 变量中有特有名词，且为私有，同3
5. 变量中有特有名词，且不是私有，首单词全部大写

**函数命名**

1. 函数名还是使用 驼峰命名法

2. 但是有一点需要注意，在 Golang 中是用大小写来控制函数的可见性，因此当你需要在包外访问，请使用 大写字母开头

3. 当你不需要在包外访问，请使用小写字母开头
另外，函数内部的参数的排列顺序也有几点原则
1. 参数的重要程度越高，应排在越前面

2. 简单的类型应优先复杂类型

3. 尽可能将同种类型的参数放在相邻位置，则只需写一次类型

## 第四章 并发编程
由于 Go语言是编译型语言，所以函数编写的顺序是无关紧要的，它不像 Python 那样，函数在位置上需要定义在调用之前。

### 4.1 函数基础
函数的声明
```go
func 函数名(形式参数列表)(返回值列表){
    函数体
}
```

**函数实现可变参数**

可变参数分为几种
* 多个类型一致的参数
* 多个类型不一致的参数

首先是多个类型一致的参数

使用...int表示一个元素为int类型的切片，用来接收调用者传入的参数
```go
// 使用 ...类型，表示一个元素为int类型的切片
func sum(args ...int) int {
    var sum int
    for _, v := range args {
        sum += v
    }
    return sum
}
func main() {
    fmt.Println(sum(1, 2, 3))
}

// output: 6

```
`...`是go语言的语法糖，如果函数下有多个类型的参数，这个语法糖必须是最后一个参数。同时这个语法糖只能在定义函数的时候使用

多个类型不一致的参数

可以指定为`...interface{}`，然后再遍历

```go
import "fmt"
func MyPrintf(args ...interface{}) {
    for _, arg := range args {
        switch arg.(type) {
            case int:
                fmt.Println(arg, "is an int value.")
            case string:
                fmt.Println(arg, "is a string value.")
            case int64:
                fmt.Println(arg, "is an int64 value.")
            default:
                fmt.Println(arg, "is an unknown type.")
        }
    }
}

func main() {
    var v1 int = 1
    var v2 int64 = 234
    var v3 string = "hello"
    var v4 float32 = 1.234
    MyPrintf(v1, v2, v3, v4)
}
```
**多个可变参数函数传递参数**

上面提到可以使用`...`接收多个参数，除此之外，他还可以用来解序列，将函数的可变参数一个一个取出来，传递给另一个可变参数的函数，而不是传递参数本身

同样这个用法，也只能在给定的函数传递参数里使用

```go
import "fmt"

func sum(args ...int) int {
    var result int
    for _, v := range args {
        result += v
    }
    return result
}

func Sum(args ...int) int {
    // 利用 ... 来解序列
    result := sum(args...)
    return result
}
func main() {
    fmt.Println(Sum(1, 2, 3))
}
```
### 4.2 Go协程：goroutine
一个goroutine本身就是一个函数，直接调用的时候就是一个普通函数，调用前加一个`go`字，就开启了一个routine
```go
//执行一个函数
func()
//开启一个协程执行这个函数
go func()
```

#### 4.2.1 协程的初步使用
在main中或者其下调用的代码才可以使用go+func()的方法启动协程，main的地位相当于主线程。当main结束时，其下的协程不管有没有运行完都会结束。
#### 4.2.2 多个协程的效果
```go
import (
    "fmt"
    "time"
)

func mygo(name string) {
    for i := 0; i < 10; i++ {
        fmt.Printf("In goroutine %s\n", name)
        // 为了避免第一个协程执行过快，观察不到并发的效果，加个休眠
        time.Sleep(10 * time.Millisecond)
    }
}

func main() {
    go mygo("协程1号") // 第一个协程
    go mygo("协程2号") // 第二个协程
    time.Sleep(time.Second)
}
```
输出如下
```
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程2号
In goroutine 协程1号
In goroutine 协程2号
```
### 4.3 详解信道/通道
信道是goroutine之间的通信机制。channel是能够让一个routine和另一个传输信息的通道。
#### 4.3.1 信道的定义与使用
每个信道只能传递一种数据类型的数据，声明的时候要指定数据类型
```
var 信道实例 chan 信道类型
```
声明后的信道，零值是nil，无法直接使用，必须配合make函数进行初始化
```
信道实例=make(chan 信道类型)
```
上面两行可以合并为1句
```
信道实例:=make(chan 信道类型)
```
假如要创建一个可以传输int类型的通道
```go
//定义信道
pipline:=make(chan int)
```
信道的数据操作，无非就两种：发送数据与读取数据
```go
//往信道中发送数据
pipline<-200
//信道中取出数据，并且赋值给mydata
mydata:=<-pipline
```
信道使用完毕之后可以关闭信号，避免有人一直等待。但是关闭后，接收方仍然可以从信道中取到数据。
```go
close(pipline)
```
关闭已关闭的信道，会报错。当从信道中读取数据时，会有多个返回值，其中第二个可以表示信道是否关闭，false为关闭，true为未关闭
```go
x,ok:=<-pipline
```
#### 4.3.2 信道的容量和长度
一般创建信道都是使用make函数，make函数接收两个参数
* 第一个参数：必填，指定信道类型
* 第二个参数：选填，不填默认为0，指定信道的容量
对于信道的容量，很重要：
* 容量为0说明没有缓冲区，发送后必须立刻接收，称为无缓冲信道
* 容量为1时，说明只能缓存一个数据，若已有一个数据，再发送会造成程序阻塞，利用这点可以利用信道做锁
* 容量大于1时，信道中可以存放多个数据，可以用于多个协程之间的通信管道，共享资源。

信道的容量可以用cap获取，长度可以用len获取
```go
package main

import "fmt"

func main() {
    pipline := make(chan int, 10)
    fmt.Printf("信道可缓冲 %d 个数据\n", cap(pipline))
    pipline<- 1
    fmt.Printf("信道中当前有 %d 个数据", len(pipline))
}
```
输出如下
```
信道可缓冲 10 个数据
信道中当前有 1 个数据
```
#### 4.3.3缓冲信道和无缓冲信道
* 缓冲信道：允许信道里存储多个数据，发送端和接收端可以处于异步状态
* 无缓冲信道：两端必须是同步的
#### 4.3.4 双向信道与单向信道
通常我们定义的信道都是双向的，可以发送数据，也可以接收数据。

但有时候我们希望信道只接受或者只发送，就有了双向通道和单向通道

* 双向通道
```go
    import (
    "fmt"
    "time"
)

func main() {
    pipline := make(chan int)

    go func() {
        fmt.Println("准备发送数据: 100")
        pipline <- 100
    }()

    go func() {
        num := <-pipline
        fmt.Printf("接收到的数据是: %d", num)
    }()
    // 主函数sleep，使得上面两个goroutine有机会执行
    time.Sleep(time.Second)
}
```
* 单向通道：分为只读通道和只写通道

只读信道
```go
var pipline = make(chan int)
type Receiver = <-chan int // 关键代码：定义别名类型
var receiver Receiver = pipline
```
只写信道
```go
var pipline = make(chan int)
type Sender = chan<- int  // 关键代码：定义别名类型
var sender Sender = pipline
```
#### 4.3.5 遍历信道
可以用for搭配range实现，在range的时候要确保信道处于关闭状态，否则会循环阻塞
```go
import "fmt"

func fibonacci(mychan chan int){
    n:=cap(mychan)
    x,y:=1,1
    for i:=0;i<n;i++{
        mychan<-x
        x,y=y,x+y
    }

    close(mychan)
}
func main(){
    pipline:=make(chan int,10)

    go fibonacci(pipline)

    for k:=range pipline{
        fmt.Println(k)
    }
}
```
#### 4.3.6 用信道来做锁
信道数据量达到容量时，再发送数据会发生阻塞，可以用来当锁
```go
package main

import (
    "fmt"
    "time"
)

// 由于 x=x+1 不是原子操作
// 所以应避免多个协程对x进行操作
// 使用容量为1的信道可以达到锁的效果
func increment(ch chan bool, x *int) {
    ch <- true
    *x = *x + 1
    <- ch
}

func main() {
    // 注意要设置容量为 1 的缓冲信道
    pipline := make(chan bool, 1)

    var x int
    for i:=0;i<1000;i++{
        //这里用goroutine会导致多个协程同时对x操作
        //而通过信道，里面有数据的时候，对x的操作无法进行，会被搁置，起到了锁的作用
        go increment(pipline, &x)
    }

    // 确保所有的协程都已完成
    // 以后会介绍一种更合适的方法（Mutex），这里暂时使用sleep
    time.Sleep(time.Second)
    fmt.Println("x 的值：", x)
}
```
```
x 的值：1000
```
#### 4.3.7信道传递是深拷贝吗
对于值类型来说，每次拷贝都会分配一块新的内存空间，改变其中一个变量不会影响另一个变量
```go
func main() {
    aArr := [3]int{0,1,2}
    fmt.Printf("打印 aArr: %v \n", aArr)
    bArr := aArr
    aArr[0] = 88
    fmt.Println("将 aArr 拷贝给 bArr 后，并修改 aArr[0] = 88")
    fmt.Printf("打印 aArr: %v \n", aArr)
    fmt.Printf("打印 bArr: %v \n", bArr)
}
```
输出结果来看，aArr和bArr互相独立，互不干扰
```
打印 aArr: [0 1 2]
将 aArr 拷贝给 bArr 后，并修改 aArr[0] = 88
打印 aArr: [88 1 2]
打印 bArr: [0 1 2]
```
对于指针类型来说，每次拷贝不会申请新的内存，而是使用它的指针，两个变量名都指向同一块内存，一个改变另一个也改变
```go
func main() {
    aslice := []int{0,1,2}
    fmt.Printf("打印 aslice: %v \n", aslice)
    bslice := aslice
    aslice[0] = 88
    fmt.Println("将 aslice 拷贝给 bslice 后，并修改 aslice[0] = 88")
    fmt.Printf("打印 aslice: %v \n", aslice)
    fmt.Printf("打印 bslice: %v \n", bslice)
}
```
输出结果可以看出aslice的更新直接反映到了bslice上
```
打印 aslice: [0 1 2]
将 aslice 拷贝给 bslice 后，并修改 aslice[0] = 88
打印 aslice: [88 1 2]
打印 bslice: [88 1 2]
```
### 4.4 WaitGroup
为保证每个协程能够完全执行，使用了sleep但这个方法并不好，我们可以用别的方法来实现
#### 4.4.1 使用信道标记完成
**不要通过共享内存来通信，要通过通信来共享内存**

学习了信道后，我们知道，信道可以实现多个协程间的通信，那么我们只要定义一个信道，在任务完成后，往信道中写入true，然后在主协程中获取到true，就认为子协程已经执行完毕。
```go
import "fmt"

func main() {
    done := make(chan bool)
    go func() {
        for i := 0; i < 5; i++ {
            fmt.Println(i)
        }
        done <- true
    }()
    <-done
}
```
输出如下
```
0
1
2
3
4
```
#### 4.4.2 使用waitgroup
上面的方法再协程数少的时候没什么问题，但协程数多的时候代码就会显得很复杂

可以用sync包提供的WaitGroup类型，只要实例化了就可以使用
```go
var 实例名 sync.WaitGroup
```
实例化后就可以使用它的方法
* Add：初始值为0，传入的值会往计数器上加，可以直接传入子协程的数量
* Done：当某个子协程完成之后可以调用这个方法，会从计数器上减一，通常搭配defer调用
* Wait：阻塞当前的协程，知道实例里的计数器归零

```go
import (
    "fmt"
    "sync"
)

func worker(x int, wg *sync.WaitGroup) {
    defer wg.Done()
    for i := 0; i < 5; i++ {
        fmt.Printf("worker %d: %d\n", x, i)
    }
}

func main() {
    var wg sync.WaitGroup

    wg.Add(2)
    go worker(1, &wg)
    go worker(2, &wg)

    wg.Wait()
}
```
输出如下：
```
worker 2: 0
worker 2: 1
worker 2: 2
worker 2: 3
worker 2: 4
worker 1: 0
worker 1: 1
worker 1: 2
worker 1: 3
worker 1: 4
```
### 4.5 互斥锁和读写锁
当遇到信道无法解决的并发问题时，需要用共享内存实现并发，golang中的锁机制就派上用场了

sync包中有两个很重要的锁类型
* `Mutex`,利用它可以实现互斥锁
* `RWMutex`利用它可以实现读写锁

#### 4.5.1 互斥锁
```go
package main

import (
    "fmt"
    "sync"
)

func add(count *int, wg *sync.WaitGroup) {
    for i := 0; i < 1000; i++ {
        *count = *count + 1
    }
    wg.Done()
}

func main() {
    var wg sync.WaitGroup
    count := 0
    wg.Add(3)
    go add(&count, &wg)
    go add(&count, &wg)
    go add(&count, &wg)

    wg.Wait()
    fmt.Println("count 的值为：", count)
}
```
输出如下，每次的count最终的值都不一样
```
// 第一次
count 的值为： 2854

// 第二次
count 的值为： 2673

// 第三次
count 的值为： 2840
```
原因是三个协程执行时，先读取count再更新count，这个过程不具备原子性。

可以给add这个函数加上mutex互斥锁，要求同一时刻仅能有一个协程对count操作

mutex锁的两种定义
```go
// 第一种
var lock *sync.Mutex
lock = new(sync.Mutex)

// 第二种
lock := &sync.Mutex{}
```
然后可以对上面的代码进行修改
```go
import (
    "fmt"
    "sync"
)

func add(count *int, wg *sync.WaitGroup, lock *sync.Mutex) {
    for i := 0; i < 1000; i++ {
        lock.Lock()
        *count = *count + 1
        lock.Unlock()
    }
    wg.Done()
}

func main() {
    var wg sync.WaitGroup
    lock := &sync.Mutex{}
    count := 0
    wg.Add(3)
    go add(&count, &wg, lock)
    go add(&count, &wg, lock)
    go add(&count, &wg, lock)

    wg.Wait()
    fmt.Println("count 的值为：", count)
}
```
此时无论执行多少次都只有一个结果
```go
count 的值为：3000
```
mutex锁的几个注意点
* t同一协程里，不要在尚未解锁时再次加锁
* 同一协程里，不要读已解锁的锁再次解锁
* 加锁后别忘记解锁，必要时使用defer语句
  
#### 4.5.2 读写锁
* 为了保证数据的安全，它规定了当有人还在读取数据（即读锁占用）时，不允计有人更新这个数据（即写锁会阻塞）

* 为了保证程序的效率，多个人（线程）读取数据（拥有读锁）时，互不影响不会造成阻塞，它不会像 Mutex 那样只允许有一个人（线程）读取同一个数据。

RWMutex的定义方法
```go
// 第一种
var lock *sync.RWMutex
lock = new(sync.RWMutex)

// 第二种
lock := &sync.RWMutex{}
```
RWMutex 里提供了两种锁，每种锁分别对应两个方法，为了避免死锁，两个方法应成对出现，必要时请使用 defer。

* 读锁：调用 RLock 方法开启锁，调用 RUnlock 释放锁
* 写锁：调用 Lock 方法开启锁，调用 Unlock 释放锁（和 Mutex类似）
```go
package main

import (
    "fmt"
    "sync"
    "time"
)

func main() {
    lock := &sync.RWMutex{}
    lock.Lock()

    for i := 0; i < 4; i++ {
        go func(i int) {
            fmt.Printf("第 %d 个协程准备开始... \n", i)
            lock.RLock()
            fmt.Printf("第 %d 个协程获得读锁, sleep 1s 后，释放锁\n", i)
            time.Sleep(time.Second)
            lock.RUnlock()
        }(i)
    }

    time.Sleep(time.Second * 2)

    fmt.Println("准备释放写锁，读锁不再阻塞")
    // 写锁一释放，读锁就自由了
    lock.Unlock()

    // 由于会等到读锁全部释放，才能获得写锁
    // 因为这里一定会在上面 4 个协程全部完成才能往下走
    lock.Lock()
    fmt.Println("程序退出...")
    lock.Unlock()
}
```
### 4.6 信道死锁经典错误案例
错误实例一
```go
package main

import "fmt"

func main() {
    pipline := make(chan string)
    pipline <- "hello world"
    fmt.Println(<-pipline)
}
```
因为是无缓冲信道，所以在接收者未准备好之前，信道是阻塞的

两种解决方法：
1. 接收者代码在发送者之前执行
2. 使用缓冲信道

第一种方法
```go
package main

import "fmt"

func main() {
    pipline := make(chan string)
    fmt.Println(<-pipline)
    pipline <- "hello world"
}
```
但是运行的时候还是会报错，因为需要从信道读取数据，信道中一直没有数据，整个过程就被阻塞在了这个地方

既然如此可以把接收者代码写在另一个协程里，并保证在发送者之前执行
```go
package main

import "fmt"

func hello(pipline chan string){
    <-pipline
}
func main(){
    pipline:=make(chan string)
    go hello(pipline)
    pipline <-"hello world"
}
```
第二种方法很简单，直接用可缓冲通道就可以了

错误实例二

每个缓冲信道都有容量，当信道满了时，再向其中传入数据会造成阻塞，必须要消费数据后，才能继续存入数据
```go
package main

import "fmt"

func main(){
    ch1:=make(chan string,1)

    ch1<-"weirdo"
    ch1<-"zhouying"//执行到这里就执行不下去了会阻塞

    fmt.Println(<-ch1)
}
```

错误实例三

程序一直等待读取信道的数据，但是之后不会再有人往信道中写数据了，此时就会死锁
```go
package main

import "fmt"

func main() {
    pipline := make(chan string)
    go func() {
        pipline <- "hello world"
        pipline <- "hello China"
        // close(pipline)
    }()
    for data := range pipline{
        fmt.Println(data)
    }
}
```
解决方法很简单，发送完数据之后关闭信道就可以了
```go
package main

import "fmt"

func main() {
    pipline := make(chan string)
    go func() {
        pipline <- "hello world"
        pipline <- "hello China"
        close(pipline)
    }()
    for data := range pipline{
        fmt.Println(data)
    }
}
```
### 4.7实现一个协程池
池化技术就是利用复用来提升性能的，golang中由于协程的轻量级大部分情况下用不到协程池。

但是抛开需求，单从技术角度来说，我们应该怎样实现一个通用的协程池呢

首先定义一个协程池（Pool）结构体，包含两个属性，都是 chan 类型的。

一个是 work，用于接收 task 任务

一个是 sem，用于设置协程池大小，即可同时执行的协程数量
```go
type Pool struct{
    work chan func()
    sem chan struct()
}
```
然后定义一个 New 函数，用于创建一个协程池对象，有一个细节需要注意

work 是一个无缓冲通道

而 sem 是一个缓冲通道，size 大小即为协程池大小
```go
func New(size int) *Pool{
    return &Pool{
        work:make(chan func()),
        sem:make(chan struct{},size)
    }
}
```
最后给协程池对象绑定两个函数
1. NewTask:往协程池中添加任务

第一次调用newtask添加任务的时候，work是无缓冲通道，所以一定会走第二个case的分支：使用go worker开启一个协程
```go
func (p *Pool) NewTask(task func){
    select{
        case p.work<-task:
        case p.sem<-struct{}{}:
            go p.worker(task)
    }
}
```
2. worker：用于执行任务

为了实现协程的复用，使用了for无限循环，使这个协程在执行完任务后，也不退出，而是一直接收新的任务
```go
func (p *Pool) worker(task func()){
    defer func(){<-p.sem}()

    for{
        task()
        task=<-p.work
    }
}
```
这两个函数是协程池实现的关键函数，里面的逻辑很值得推敲：

1. 如果设定的协程池数大于 2，此时第二次传入往 NewTask 传入task，select case 的时候，如果第一个协程还在运行中，就一定会走第二个case，重新创建一个协程执行task

2. 如果传入的任务数大于设定的协程池数，并且此时所有的任务都还在运行中，那此时再调用 NewTask 传入 task ，这两个 case 都不会命中，会一直阻塞直到有任务执行完成，worker 函数里的 work 通道才能接收到新的任务，继续执行。

使用它也特别简单
```go
func main(){
    pool:=New(128)
    pool.NewTask(func(){
        fmt.Println("run task")
    })
}
```
为了展现效果，将协程池数设置为2，开四个任务
```go
func main(){
    pool:=New(2)

    for i:=1;i<5;i++{
        pool.NewTask(func(){
            time.sleep(2*time.Second)
            fmt.Println(time.Now())
        })
    }

    time.Sleep(5*time.Second)
}

```
执行结果如下，可以看到总共 4 个任务，由于协程池大小为 2，所以 4 个任务分两批执行（从打印的时间可以看出）
```
2020-05-24 23:18:02.014487 +0800 CST m=+2.005207182
2020-05-24 23:18:02.014524 +0800 CST m=+2.005243650
2020-05-24 23:18:04.019755 +0800 CST m=+4.010435443
2020-05-24 23:18:04.019819 +0800 CST m=+4.010499440
```

### 4.8 理解go语言中的Context
Context也叫上下文，它的接口定义如下
```go
type Context interface {
    Deadline() (deadline time.Time, ok bool)
    Done() <-chan struct{}
    Err() error
    Value(key interface{}) interface{}
}
```
可以看到 Context 接口共有 4 个方法

* `Deadline`：返回的第一个值是 截止时间，到了这个时间点，Context 会自动触发 Cancel 动作。返回的第二个值是 一个布尔值，true 表示设置了截止时间，false 表示没有设置截止时间，如果没有设置截止时间，就要手动调用 cancel 函数取消 Context。

* `Done`：返回一个只读的通道（只有在被cancel后才会返回），类型为 struct{}。当这个通道可读时，意味着parent context已经发起了取消请求，根据这个信号，开发者就可以做一些清理动作，退出goroutine。

* `Err`：返回 context 被 cancel 的原因。

* `Value`：返回被绑定到 Context 的值，是一个键值对，所以要通过一个Key才可以获取对应的值，这个值一般是线程安全的。

#### 4.8.1 为何需要Context
当一个协程（goroutine）开启后，我们无法强制关闭它

常见的关闭协程的原因如下：
1. goroutine跑完后自己退出，正常关闭，不讨论
2. 主进程crash退出，goroutine被迫退出，异常关闭，需要优化代码
3. 通过通道发送信号，引导协程的关闭，开发者可以手动控制协程的方法

```go
func main() {
    stop := make(chan bool)

    go func() {
        for {
            select {
            case <-stop:
                fmt.Println("监控退出，停止了...")
                return
            default:
                fmt.Println("goroutine监控中...")
                time.Sleep(2 * time.Second)
            }
        }
    }()

    time.Sleep(10 * time.Second)
    fmt.Println("可以了，通知监控停止")
    stop<- true
    //为了检测监控过是否停止，如果没有监控输出，就表示停止了
    time.Sleep(5 * time.Second)

}
```

使用一个通道实现对多个goroutine的控制（取消），使用 close 关闭通道后，如果该通道是无缓冲的，则它会从原来的阻塞变成非阻塞，也就是可读的，只不过读到的会一直是零值，因此根据这个特性就可以判断 拥有该通道的 goroutine 是否要关闭。
```go
package main

import (
    "fmt"
    "time"
)

func monitor(ch chan bool, number int)  {
    for {
        select {
        case v := <-ch:
            // 仅当 ch 通道被 close，或者有数据发过来(无论是true还是false)才会走到这个分支
            fmt.Printf("监控器%v，接收到通道值为：%v，监控结束。\n", number,v)
            return
        default:
            fmt.Printf("监控器%v，正在监控中...\n", number)
            time.Sleep(2 * time.Second)
        }
    }
}

func main() {
    stopSingal := make(chan bool)

    for i :=1 ; i <= 5; i++ {
        go monitor(stopSingal, i)
    }

    time.Sleep( 1 * time.Second)
    // 关闭所有 goroutine
    close(stopSingal)

    // 等待5s，若此时屏幕没有输出 <正在监控中> 就说明所有的goroutine都已经关闭
    time.Sleep( 5 * time.Second)

    fmt.Println("主程序退出！！")

}
```
输出如下
```go
监控器4，正在监控中...
监控器1，正在监控中...
监控器2，正在监控中...
监控器3，正在监控中...
监控器5，正在监控中...
监控器2，接收到通道值为：false，监控结束。
监控器3，接收到通道值为：false，监控结束。
监控器5，接收到通道值为：false，监控结束。
监控器1，接收到通道值为：false，监控结束。
监控器4，接收到通道值为：false，监控结束。
主程序退出！！
```
#### 4.8.2 简单使用Context
如果不使用上面close通道的方式，还有没有其他更加优雅的方法来实现？

用Context实现
```go
package main

import (
    "context"
    "fmt"
    "time"
)

func monitor(ctx context.Context, number int)  {
    for {
        select {
        // 其实可以写成 case <- ctx.Done()
        // 这里仅是为了让你看到 Done 返回的内容
        case v :=<- ctx.Done():
            fmt.Printf("监控器%v，接收到通道值为：%v，监控结束。\n", number,v)
            return
        default:
            fmt.Printf("监控器%v，正在监控中...\n", number)
            time.Sleep(2 * time.Second)
        }
    }
}

func main() {
    ctx, cancel := context.WithCancel(context.Background())

    for i :=1 ; i <= 5; i++ {
        go monitor(ctx, i)
    }

    time.Sleep( 1 * time.Second)
    // 关闭所有 goroutine
    cancel()

    // 等待5s，若此时屏幕没有输出 <正在监控中> 就说明所有的goroutine都已经关闭
    time.Sleep( 5 * time.Second)

    fmt.Println("主程序退出！！")

}
```
其中关键的代码其实只有三行

第一行：以 context.Background() 为 parent context 定义一个可取消的 context
```go
ctx, cancel := context.WithCancel(context.Background())
```

第二行：然后你可以在所有的goroutine 里利用 for + select 搭配来不断检查 ctx.Done() 是否可读，可读就说明该 context 已经取消，你可以清理 goroutine 并退出了。
```go
case <- ctx.Done():
```

第三行：当你想到取消 context 的时候，只要调用一下 cancel 方法即可。这个 cancel 就是我们在创建 ctx 的时候返回的第二个值。
```go
cancel()
```
运行结果如下。
```
监控器3，正在监控中...
监控器4，正在监控中...
监控器1，正在监控中...
监控器2，正在监控中...
监控器2，接收到通道值为：{}，监控结束。
监控器5，接收到通道值为：{}，监控结束。
监控器4，接收到通道值为：{}，监控结束。
监控器1，接收到通道值为：{}，监控结束。
监控器3，接收到通道值为：{}，监控结束。
主程序退出！！
```
#### 4.8.3 根Context是什么
创建Context必须要指定父Context，那要创建第一个Context的时候该怎么办呢

Go本身已经帮我们实现了两个。
```go
var (
    background = new(emptyCtx)
    todo       = new(emptyCtx)
)

func Background() Context {
    return background
}

func TODO() Context {
    return todo
}
```
一个是Background，主要用于main函数、初始化以及测试代码中，作为Context这个树结构的最顶层的Context，也就是根Context，它不能被取消。
```go
type emptyCtx int

func (*emptyCtx) Deadline() (deadline time.Time, ok bool) {
    return
}

func (*emptyCtx) Done() <-chan struct{} {
    return nil
}

func (*emptyCtx) Err() error {
    return nil
}

func (*emptyCtx) Value(key interface{}) interface{} {
    return nil
}
```
#### 4.8.4 Context的继承衍生
上面自定义Context的时候，使用的是WithCancel方法，此外还有其他几个With方法
```go
func WithCancel(parent Context) (ctx Context, cancel CancelFunc)
func WithDeadline(parent Context, deadline time.Time) (Context, CancelFunc)
func WithTimeout(parent Context, timeout time.Duration) (Context, CancelFunc)
func WithValue(parent Context, key, val interface{}) Context
```
这四个函数有一个共同的特点，就是第一个参数，都是接收一个 父context。

通过一次继承，就多实现了一个功能，比如使用 WithCancel 函数传入 根context ，就创建出了一个子 context，该子context 相比 父context，就多了一个 cancel context 的功能。

如果此时，我们再以上面的子context（context01）做为父context，并将它做为第一个参数传入WithDeadline函数，获得的子子context（context02），相比子context（context01）而言，又多出了一个超过 deadline 时间后，自动 cancel context 的功能。

接下来我会举例介绍一下这几种 context，其中 WithCancel 在上面已经讲过了，下面就不再举例了

**例子1：WithDeadline**
```go
package main

import (
    "context"
    "fmt"
    "time"
)

func monitor(ctx context.Context, number int)  {
    for {
        select {
        case <- ctx.Done():
            fmt.Printf("监控器%v，监控结束。\n", number)
            return
        default:
            fmt.Printf("监控器%v，正在监控中...\n", number)
            time.Sleep(2 * time.Second)
        }
    }
}

func main() {
    ctx01, cancel := context.WithCancel(context.Background())
    ctx02, cancel := context.WithDeadline(ctx01, time.Now().Add(1 * time.Second))

    defer cancel()

    for i :=1 ; i <= 5; i++ {
        go monitor(ctx02, i)
    }

    time.Sleep(5  * time.Second)
    if ctx02.Err() != nil {
        fmt.Println("监控器取消的原因: ", ctx02.Err())
    }

    fmt.Println("主程序退出！！")
}
```
输出如下
```
监控器5，正在监控中...
监控器1，正在监控中...
监控器2，正在监控中...
监控器3，正在监控中...
监控器4，正在监控中...
监控器3，监控结束。
监控器4，监控结束。
监控器2，监控结束。
监控器1，监控结束。
监控器5，监控结束。
监控器取消的原因:  context deadline exceeded
主程序退出！！
```
**例子2：WithTimeout**

WithTimeout 和 WithDeadline 使用方法及功能基本一致，都是表示超过一定的时间会自动 cancel context。

唯一不同的地方，我们可以从函数的定义看出

WithDeadline 传入的第二个参数是 time.Time 类型，它是一个绝对的时间，意思是在什么时间点超时取消。

而 WithTimeout 传入的第二个参数是 time.Duration 类型，它是一个相对的时间，意思是多长时间后超时取消
```go
package main

import (
    "context"
    "fmt"
    "time"
)

func monitor(ctx context.Context, number int)  {
    for {
        select {
        case <- ctx.Done():
            fmt.Printf("监控器%v，监控结束。\n", number)
            return
        default:
            fmt.Printf("监控器%v，正在监控中...\n", number)
            time.Sleep(2 * time.Second)
        }
    }
}

func main() {
    ctx01, cancel := context.WithCancel(context.Background())

    // 相比例子1，仅有这一行改动
    ctx02, cancel := context.WithTimeout(ctx01, 1* time.Second)

    defer cancel()

    for i :=1 ; i <= 5; i++ {
        go monitor(ctx02, i)
    }

    time.Sleep(5  * time.Second)
    if ctx02.Err() != nil {
        fmt.Println("监控器取消的原因: ", ctx02.Err())
    }

    fmt.Println("主程序退出！！")
}
```
通过Context我们也可以传递一些必须的元数据，这些数据会附加在Context上以供使用。

元数据以 Key-Value 的方式传入，Key 必须有可比性，Value 必须是线程安全的。

还是用上面的例子，以 ctx02 为父 context，再创建一个能携带 value 的ctx03，由于他的父context 是 ctx02，所以 ctx03 也具备超时自动取消的功能。
```go
package main

import (
    "context"
    "fmt"
    "time"
)

func monitor(ctx context.Context, number int)  {
    for {
        select {
        case <- ctx.Done():
            fmt.Printf("监控器%v，监控结束。\n", number)
            return
        default:
            // 获取 item 的值
            value := ctx.Value("item")
            fmt.Printf("监控器%v，正在监控 %v \n", number, value)
            time.Sleep(2 * time.Second)
        }
    }
}

func main() {
    ctx01, cancel := context.WithCancel(context.Background())
    ctx02, cancel := context.WithTimeout(ctx01, 1* time.Second)
    ctx03 := context.WithValue(ctx02, "item", "CPU")

    defer cancel()

    for i :=1 ; i <= 5; i++ {
        go monitor(ctx03, i)
    }

    time.Sleep(5  * time.Second)
    if ctx02.Err() != nil {
        fmt.Println("监控器取消的原因: ", ctx02.Err())
    }

    fmt.Println("主程序退出！！")
}
```
#### 4.8.5 Context注意事项
1. 通常 Context 都是做为函数的第一个参数进行传递（规范性做法），并且变量名建议统一叫 ctx

2. Context 是线程安全的，可以放心地在多个 goroutine 中使用。

3. 当你把 Context 传递给多个 goroutine 使用时，只要执行一次 cancel 操作，所有的 goroutine 就可以收到 取消的信号

4. 不要把原本可以由函数参数来传递的变量，交给 Context 的 Value 来传递。

5. 当一个函数需要接收一个 Context 时，但是此时你还不知道要传递什么 Context 时，可以先用 context.TODO 来代替，而不要选择传递一个 nil。

6. 当一个 Context 被 cancel 时，继承自该Context的所有子Context 都会被 cancel。

### 4.9 函数类型
函数类型表示所有拥有同样的入参类型和返回值类型的函数集合
```go
typt Greeting func(name string) string
```
这种类型有两个特征：
1. 只接收一个参数，并且该参数类型为string
2. 返回值也只有一个参数，类型为string
   
一个函数只要满足这些特征，那么它就可以通过如下方式将该函数转换成 Greeting 类型的函数对象（也即 greet）
```go
func english(name string) string{
    return "hello"+name
}
greet:=Greeting(english)
```
greet 做为 Greeting 类型的对象，自然也拥有 Greeting 类型的所有方法，比如下面的 say 方法
```go
func (g Greeting) say(n string) {
    fmt.Println(g(n))
}
//直接调用并不会报错
greet.say("world")
```


