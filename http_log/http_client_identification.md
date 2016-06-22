
# HTTP - The Definitive guide

start at 20160415 14:04

### Client Identification
HTTP是无状态的协议, 每次请求都是孤立的. 而服务端想要根据用户与网站上的交互, 提供给用户独特的体验; 实现着种功能首先需要识别用户, 才能记录用户行为.

可以通过以下几个方面进行分析:
* 包含用户信息的 HTTP headers
* client ip
* 用户登录认证
* Fat URL (在url中包含用户标识)
* Cookies (已经说过了)


#### HTTP Headers
Header Name | Header type | Desc
From | Request | user email
User-Agent | Request | user browser software (客户端app的信息, 通常会包含客户的操作系统信息)
Referer | Request | Page user came from by following link (用户从何URI来到当前URI)
Authorization | Request | username and password
Client-ip | Extension(Request) | client's ip
X-Forwarded-For | Extension(Request) | client's ip
Cookie | Extension(Request) | client's Cookie info set by server


#### User login
HTTP 协议支持用户登录行为, 服务端返回 401(Login Required), Client 将提示用户输入用户名和密码.
一旦登陆验证成功, client 每次请求时都会在Header中携带登陆信息.
1. 客户端请求
  GET /resource HTTP/1.1
  Host: www.xxx.com
2. 服务端相应, 要求登陆
  HTTP/1.1 401 Login required
  WWW-Authenticate: Basic realm="Plumbing and fixtures"
3. 客户端弹出登录提示, 要求用户填写, 后再次发送请求
  GET /resource HTTP/1.1
  Host: www.xxx.com
  Authorization: Basic am12390804asd
4. 服务端验证登陆信息, 返回结果
  HTTP/1.1 200 OK
  Content-type: text/html
  Content-length: 2314
  ...

这需要clientApp根据访问站点记录登陆信息, 每次都返回(Cookie的设计思路相同, 不同的是由服务端自动设置, 用户无感知)


#### Fat URLs
Fat URLs 是利用URL来标识用户, 当用户访问页面时, 服务端在返回时修改URL(需要一次Redirect), 在URL中加入部分信息来标识访问的用户.

这种方式的确可以标识用户, 但存在不少缺点:
* Ugly URL
* Can't share URL
* Breaks caching (缓存的URL内容无效, 保存URL也无效)
* Extra server load (服务端解析URL工作加重)
* Escape hatches (用户轻易可以修改标识)
* Not persistent across sessions (用户再次访问起始页时, 服务端缓存将无法标识)


#### Cookie
比较靠谱的方式, 和User Login机制类似, 更自动, 用户体验更好



### Part 2 TODO:(leoly008) 20160415

### Part 3 TODO:(leoly008) 20150415
