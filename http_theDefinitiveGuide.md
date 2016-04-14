# HTTP - The Definitive Guide.pdf

始于 2016-04-14 12:46

## Part1
1. over view of HTTP
2. format of URLs, outline of URN revolution
3. HTTP Messages details
4. Connection Managements


### Over View Of HTTP
HyperText Transport Protocol - HTTP<br>
Resource: any kind of content source.

#### Media Types
使用 MIME (Multipurpose Internet Mail Extensions) 作为 tag 标识不同的数据(Media)类型.

MIME type 是文字标签, 描述对象的类型和子类型，使用``/``分割, 如:<br>
* HTML-formatted text doc 是 ``text/html``
* plain ASCII text doc 是 ``text/plain``
* JPEG version 图片是 ``image/jpeg``
* GIF 图片 ``image/gif``
* QuickTime movie 为 ``video/quicktime``
* MS PPT 是 ``application/vnd.ms-powerpoint``

MIME type 在 ``Content-type:``中转递, 数据长度由 ``Content-length:``指定

#### URIs
服务资源名称为``uniform resource identifier`` -> URI, 相当于邮寄地址(postal address), 如:<br>
``http://www.joes-hardware.com/specials/saw-blade.gif``

URI 分为两只
* URL
* URN

##### URLs
URL -> ``uniform resource locator``, 是最常见的 URI. 它描述了特定资源在特定的服务器上, 使用特定协议获取. 如:<br>
``http://www.joes-hardware.com/specials/saw-blade.gif``
其中<br>
* ``http://`` 表示使用的协议为http协议
* ``www.joes-hardware.com`` 为服务地址
* ``/specials/saw-blade.gif`` 为特定资源名字
当今, 大部分 ``URI`` 为 ``URL``

1. ``http``被称为``URL scheme``, 它告诉浏览器使用 HTTP 协议获取资源
  ``://`` 是什么呢?
2. ``www.joes-hardware.com`` 是服务地址(server location), 它告诉浏览器资源所在的位置
3. ``/specials/saw-blade.gif`` 是资源路径(resource path), 说明资源在服务器的具体位置

URL 不光局限于HTTP, 他被广泛应用在Web上, 如:<br>
* 邮件地址 ``mailto:president@whitehouse.gov``
* FTP ``ftp://ftp.lots-o-books.com/publ/complete-price-list.xls``
* movie ``rtsp://www.joes-hardware.com:514/interview/cto_video``

URL 通常的格式是 ``scheme://serverLocation/resourcePath`` 但是必须这样

###### URL syntax
URL 根据 scheme 不同，其格式可能有所变化，可以总结为:<br>
``<scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<frag>``<br>
最重要的三部分是 ``scheme``, ``host`` 及 ``path``.

URL component 说明:

Component | 说明 | 默认值
----|----|---
scheme | 使用何种协议获取资源 | None
user | 某些 scheme 要求用户名才能访问资源 | anonymous
password | 紧跟 user 的密码, 用 ``:`` 分隔 | <Email Address>
host | 主机名或点分格式的IP资源所在的主机 | None
port | 主机监听的端口号, 不同的 scheme 不同 | Scheme-specific
path | 资源在主机上的位置, 和host/port用``/``分隔, 分隔符随 scheme 变化 | None
params | 某些 scheme 支持传递参数, 格式为 ``name/value``, 使用``;``分隔多个参数及其他部分 | None
query | 某些 scheme 支持传递查询参数与服务器交互, 使用 ``?`` 与URL前部分分隔 | None
frag | 页面标签, 使用 ``#``与其他部分分隔 | None



##### URNs
URN -> ``uniform resource name``, 是特定内容的唯一标识名字，不依赖资源的位置。允许资源在不同位置上移动。也不定义获取资源的协议(允许使用多种协议获取数据); 如:
* ``urn:ietf:rfc:2141``<br>
URN 处于试验阶段，他需要资源定位功能的支持。


#### Transactions
HTTP 传输由请求命令(request command, from client), 响应结果(response result, from server to client)组成. 使用格式化的 HTTP 消息通信.

##### Methods
HTTP 支持以下命令, 称为 HTTP methods, 每个 HTTP 请求都必须有一个 methods.<br>
Method 告诉服务器应该做什么操作, methods 如下表

HTTP method | 说明 | 是否有 Message Body
------------|------|-----
GET | 请求Server发送指定名字的资源给client | No
HEAD | 只发送特定的资源 HTTP response headers(与GET比较，服务端不返回entity-body) 可以根据返回的Headers判断是否需要重新加载 | No
PUT | 将client数据存储为Server上指定的资源 | Yes
DELETE | 删除Server上指定名字的资源 | No
POST | 将client的数据发送给Server特定的application | Yes
TRACE | 跟踪消息, 从proxy直到server, 服务端会返回其收到的request的信息, 可以验证request在途中是否被修改过; 主要用于诊断 | No
OPTIONS | 请求服务端返回其支持的method类型 | No
LOCK | 锁定目标资源, extension method | No
MKCOL | 创建资源, extension method | Yes
COPY | 复制服务端资源, extension method | ?
MOVE | 移动服务端资源, extension method | ?

不是所有的服务都支持所有method
服务也可以自己扩展其他method


##### Status Codes
每个 HTTP 响应消息都带一个状态字, 三位数字组成, 告诉客户端请求是否成功, 或是要求客户端执行其他行为; status code 有:

HTTP status code | 说明
------|------
100 | Continue, 初始部分已经收到, client 可以继续发送后续部分的请求
101 | Switch Protocols, 服务端正在按照客户端的请求做协议切换
200 | OK, 请求成功, 对应资源在 entity-body 中
201 | Created, 创建成功
202 | Accepted, 请求已被接收,  
203 | Non-Authoritative Information,  
204 | No Content, 响应消息无entity-body
205 | Reset Content, 要求browser清楚当前页的内容
206 | Partial Content, 部分内容成功
300 | Multiple Choices, 返回多个选项可供重定向
301 | Moved Permanently, 对应资源已经被永久移动到其他地方
302 | Found, Redirect, 重定向, 要求client去其位置获取资源
303 | See Other, 同上, 响应POST请求
304 | Not Modified, 如果client查询内容是否变化, 304表示内容未变化
305 | Use Proxy, 资源必须通过proxy获取, 并返回proxy地址
306 | (Unused),
307 | Temporary Redirect, 当前请使用返回的地址请求资源, 稍后的请求可以继续使用当前URL
400 | Bad Request, client的请求格式错误
401 | Unauthorized, 需要输入用户名密码来访问资源
402 | Payment Required,
403 | Forbidden, 服务端拒绝服务
404 | Not Found, 没找到. 没找到特定的资源
405 | Method Not Allowed, 服务端不支持请求中的 method
406 | Not Acceptable, client 参数不可用
407 | Proxy Authentication Required, 同401, 由Proxy Server返回
408 | Request Timeout, client 请求超时
409 | Conflict, client 请求使Server Conflict
410 | Gone, 同404, 资源已被移除
411 | Length Required, 要求client提供 Content-length
412 | Precondition Failed, client请求Conditional request, 但Conditional不满足
413 | Request Entity Too Large, client的entity-body太大
414 | Request URL Too Long, 请求的URL太长
415 | Unsupported Media Type, 不支持的Content-type类型
416 | Requested Range Not Statisfiable, 请求的资源范围无效
417 | Expectation Failed, client的 Expectation request server 无法满足
500 | Internal Server Error, server在处理请求时出错, 无法完成服务
501 | Not Implemented, 不支持的服务类型
502 | Bad Gateway, proxy or gateway server 发现请求下一站报错
503 | Service Unavailable, server当前暂时无法提供服务


HTTP协议同时返回解释性文本(explanatory textural)作为参考, 应以 status code 为准.

Status code 分段<br>

code range | 已定义的范围 | 分类
-----------|-------------|------
100-199 | 100-101 | Informational 信息
200-299 | 200-206 | Successful 成功
300-399 | 300-305 | Redirection 重定向
400-499 | 400-415 | 客户端错误
500-599 | 500-505 | 服务端错误

##### Web Pages Can Consist of Multiple Objects
Web Page 是 collection of resource, 不是单一资源, browser 根据 Web Page 的内容请求资源并展示.


#### Messages
HTTP request 和 HTTP response的结构<br>
HTTP 消息是简单的, 以行为单位的字符序列. 他们是纯文本, 没有二进制, 易于用户读写的.
可分为三部分<br>
Message 中的换行使用ASCII码的(13, 回车)和(10, 换行), CRLF
* Start line 首行消息, 表明请求类型. 只能是纯文本
* Headers 可以为空或多个字段, 紧接 Start line; Headers的每个字段由 ``name`` 和 ``value``对组成, 使用 ``:`` 分隔. Headers 结束后需要跟一个空行. 只能是纯文本
* Body Headers空行后的是body, 可有可无. 它可以包含任意数据. request body 包含请求数据， response body 包含响应数据. body可以包含任意类型的数据, (images, video, audio, ...)


##### Message syntax
request message syntax:
```
<method> <request-URL> <version>
<headers>

<entity-body>
```

response message syntax:
```
<method> <status> <reason-phrase>
<headers>

<entity-body>
```

* request-URL: 完整的 URL 或 URL 的 resource path
* version: 格式为 ``HTTP/<major>.<minor>``
* status: 返回的状态码, 三位数字`XXX``
* reason-phrase: 状态码说明, 文本
* headers: 0或多个, 每个占据至少一行, 多行的 header 第二行开始, 行首应以空字符开头(空格或制表符) 格式为 ``name:value`` 行以CRLF结尾; headers以一个空行结束.
* entity-body: 数据, 可包含任意数据


##### Headers
headers提供请求和响应的额外信息.<br>
header 的分类(classifications)
* General headers<br>
  可以出现在请求或响应中<br>

Information Header | Desc
---|---|
Connection | 指定请求或响应的连接
Date | 消息创建的时间戳
MIME-Version | 发送端 MIME 的版本信息
Trailer | Lists the set of headers that are in the trailer of a message encoded with the chunked trasfer encoding
Transfer-Encoding | 消息的编码方式
Upgrade | 发送端期望使用的鞋业版本
Via | 消息都经过了哪些 proxy or gateway

HTTP/1.0 开始允许HTTP App缓存数据<br>

Caching Header | Desc
---|---
Cache-Control | pass caching directions along with the message
Pragma | another way to pass directions along with then message, though not specific to caching


* Request headers<br>
  请求消息的附加信息<br>

Information Header | Desc
---|---
Client-IP | 客户端IP
From | client 的 email
Host | 接收请求的server和端口
Referer | 当前请求的 URI
UA-Color | client display color capailities
UA-CPU | client CPU type, manufacturer
UA-Disp | client display screen capabilities
UA-OS | client OS name and version
UA-Pixels | client machine display pixel
User-Agent | 发送请求的app信息

告诉Server client的接受限制<br>

Accept header | Desc
Accept | client 能处理的media types
Accept-Charset | client 接受的字符集
Accept-Encoding | client 接受的编码方式
Accept-Language | client 接受的语言类型
TE | 其他可用的扩展代码 (what extension transfer codings are OK to use)

限定条件头<br>

Conditional request header | Desc
Expect | 列出client期望server为当前请求做的行为
If-Match | 如果当前tag匹配, 则返回资源
If-Modified-Since | 如果请求的资源新与指定时间, 则返回资源
If-None-Match | 如果tag不匹配, 则返回资源
If-Range | 请求部分资源
If-Unmodified-Since | 如果请求的资源旧与指定时间, 则返回资源
Range | 返回指定范围的资源

安全相关的头<br>

security header | Desc
Authorization | 服务端可作为验证client身份的数据
Cookie | client 将 token 发送给服务端
Cookie2 | 新版Cookie



* Response headers<br>
  响应消息的附加信息
* Entity headers<br>
  描述 entity-body 的信息
* Extension headers<br>
  未明确定义的信息

Headers | 说明
----|----
Data | 服务端生成响应的时间
Content-length | entity-body 的字节数
Content-type | entity-body 的类型
Accept | 客户端可以识别的 MIME 类型





#### Connections
HTTP 消息通过 TCP/IP 协议传输.<br>
TCP 提供自动纠错, 顺序, 自动分段功能, 保证通信的可靠性. HTTP 不用关注消息传送的问题.

URI/URL提供了服务端地址(IP)或域名(DNS解析为地址/IP), 端口(默认80), browser 建立与服务器的TCP链接, 发送请求, 接受响应. 关闭连接


##### Telent as browser
因为HTTP基于TCP/IP的文本协议, 我们可以使用 telnet 链接服务端, 模拟HTTP请求.
```
$ telnet www.baidu.com 80
Trying 115.239.210.27...
Connected to www.baidu.com.
Escape character is '^]'.
# 这是我们的请求
GET / HTTP/1.1
Host: www.baidu.com
 # 这是 Headers 后的空行

# 这是响应
HTTP/1.1 200 OK
Date: Thu, 14 Apr 2016 05:55:51 GMT
Content-Type: text/html
Content-Length: 14613
Last-Modified: Wed, 03 Sep 2014 02:48:32 GMT
Connection: Keep-Alive
...
```


#### Protocol Versions
HTTP 协议有几个版本在用
* HTTP/0.9
* HTTP/1.1
* HTTP/2.0


#### Architectural Components of the Web
Web 上重要的应用有:
* Proxies<br>
  HTTP intermediaries (中间人) 在 client 与 server 间.<br>
  important building blocks for web security, application integration, and performace optimization.<br>
  它位于客户端网路外延，将client的请求转发给server，可以过滤、修改request和response
* Caches<br>
  HTTP storehouses 在距离client更近的地方, 存储Web资源<br>
  缓存服务，特定的Proxy，如果Proxy上有需要的资源，则直接返回给client.
* Gateways ??<br>
  特定的Server, 连接到其他应用<br>
  常用与做协议转换. client不知道其转换的源数据, 如(HTTP/FTP Gateways),客户端收到的相应依然是HTTP响应
* Tunnels ??<br>
  特定 Proxies 转发所有特定的 HTTP 通信<br>
  使用HTTP协议建立通信连接，使用HTTP协议的请求发送内部封装的数据, 如 HTTP/SSL Tunnel
* Agents ??<br>
  半智能 web-client 自动生成 HTTP 请求<br>
  spider 算 Agent, 所有client都算Agent



#### Cookies
Cookies 是当前最好的表示用户及允许持久会话的方式<br>
Cookies 引入定义了新的HTTP headers.

Cookies 分为2种:
1. session cookies<br>
  临时的cookie, 用户追踪用户在特定网站上的设置和喜好<br>
  session cookies在用户关闭浏览器时被清除
2. persistent cookies<br>
  生存更长时间，被存储在磁盘上. 即使重启浏览器或电脑, 也不一定被清除.<br>
  保存用户浏览特定网站的配置信息, 用户登陆信息.

他们的区别就是持续时间, 设置时是否指定了``Discard``参数,  是否有过期时间设置.

##### Cookies 如何工作
client请求server时, server可以在response中使用
``Set-Cookie``或``Set-Cookie2`` header在client侧添加cookie<br>
cookie 是任意``name=value``形式的值, ``name``是名字, ``value``是值
一般server用cookie标识用户, 分配一个唯一值标识一个用户.<br>
浏览器将服务端响应中的cookie存在cookie DB中. 当client再次访问相同server时, 会读出cookie的值, 附加在request的header中, 发送给server.

cookie的目的就是累计服务端制定的client信息，在client访问服务端时把信息返回给服务端.<br>
因为cookie存放在client端, 所以这种机制被称为``client-side state``.<br>
cookie的官方名称(official name for cookie specification is the HTTP State Management Mechanism).

###### Cookie Domain
服务端发送cookie时可以指定可读取cookie的域名, 如<br>
``Set-Cookie: user="mary18"; domain="xxx.com"``<br>
当用户访问 ``www.xxx.com`` 或 ``specials.xxx.com`` 或任意网站以 ``xxx.com``结尾时,
``Cookie: user="mary18"`` 将被发送到服务端.

###### Cookie Path
cookie也可以指定特定站点的一部分可以获取客户端cookie, 通过cookie的Path属性可以指定 URL<br> Path的匹配信息, 对匹配的 URL Path的访问才会返回cookie信息. 如<br>
``Set-Cookie: pref=compact; domain="xxx.com", path=/aaa/``<br>
当访问``www.xxx.com/special.html``时, 只能得到<br>
``Cookie: user="mary18"``<br>
当访问``www.xxx.com/aaa/`` ``www.xxx.com/aaa/asdfasdf``时, 可以得到<br>
``Cookie: user="mary18"; pref=compact``


##### Cookie Ingredients (成分, 要素)
Cookie有2个版本, Version 0(Netscape cookies) 和 Version 1(RFC 2965)

###### Version 0 cookies
cookie设置header如下: (注意, ;后有空格)<br>
``Set-Cookie: name=value [; expires=data] [; path=path] [; domain=domain] [; secure]``

返回给服务端的Cookie如下: (注意, ;后有空格)<br>
``Cookie: name=value [; name1=value2]``


* expires=data<br>
  唯一有效的TIME ZONE 是 GMT, 格式是 DD-Mon-YY HH:MM:SS GMT; 如果不指定, 会话结束时, 清楚cookie
* secure<br>
  可选, 如果指定, 只有在服务端使用 SSL 连接时才发送 Cookie 给服务端
asdf
###### Version 1 cookies
version 1 引入了 ``Set-Cookie2`` 和 ``Cookie2`` header
* 支持在浏览器退出时强制删除cookie, 不管其是否设置了超时
* Max-Age 用秒数来计算Cookie的国企时间, 而不是绝对日期
* 可以使用 domain port path 来区分 Cookie
* Cookie 返回时, 附带 domain, port 和 path
* Version number for interoperability
* $ prefix in Cookie header to 区分其他关键字和用户名

Version 1 cookie attribute
* NAME=VALUE<br>
  必须有. NAME不能以`$`开头, $开头有特殊含义
* Version<br>
  必须有. 值为整数(0,1) ``Version="1"``
* Comment<br>
  可选. Cookie的含义, 必须使用UTF-8编码
* CommentURL<br>
  可选. 提供一个URL链接来面熟Cookie的含义
* Discard<br>
  可选. 如果指定, 表明client app关闭时清除cookie
* Domain<br>
  可选. 只有指定的域名(后缀匹配)才返回cookie
* Path<br>
  可选. 只有指定的路径(后缀匹配)才返回cookie
* Port<br>
  可选. 可以是列表, 只有匹配的端口的服务才返回cookie ``Port="80,81,8080"``
* Max-age<br>
  可选. Cookie的存活时间, 整数, 秒数, 0 表示client端立即清除cookie(用于清除client cookie)
* Secure<br>
  同 Version 0

Version 1版本的 Cookie返回时, $开始的NAME是在其前面的Cookie的限定属性, 如 ``$Version="1"`` ``￥Domain="aaa.com"`` ``$Path=/bbb``
