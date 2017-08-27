# python -- urllib

```sh
urllib.request for opening and reading URLs
urllib.error containing the exceptions raised by urllib.request
urllib.parse for parsing URLs
urllib.robotparser for parsing robots.txt files
```

### urllib.request
[urllib.request](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request)

functions :
* urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

* urllib.request.install_opener(opener)

* urllib.request.build_opener([handler, …])

* urllib.request.pathname2url(path)

* urllib.request.url2pathname(path)

* urllib.request.getproxies()

classes : 
* class urllib.request.Request(url, data=None, headers={}, origin_req_host=None,unverifiable=False, method=None)

* class urllib.request.OpenerDirector

* class urllib.request.BaseHandler

* class urllib.request.HTTPDefaultErrorHandler¶

* class urllib.request.HTTPRedirectHandler

* class urllib.request.HTTPCookieProcessor(cookiejar=None)

* class urllib.request.ProxyHandler(proxies=None)

* class urllib.request.HTTPPasswordMgr

* class urllib.request.HTTPPasswordMgrWithDefaultRealm

* class urllib.request.HTTPPasswordMgrWithPriorAuth

* class urllib.request.AbstractBasicAuthHandler(password_mgr=None)

* class urllib.request.HTTPBasicAuthHandler(password_mgr=None)

* class urllib.request.ProxyBasicAuthHandler(password_mgr=None)

* class urllib.request.AbstractDigestAuthHandler(password_mgr=None)

* class urllib.request.HTTPDigestAuthHandler(password_mgr=None)

* class urllib.request.ProxyDigestAuthHandler(password_mgr=None)

* class urllib.request.HTTPHandler

* class urllib.request.HTTPSHandler(debuglevel=0, context=None, check_hostname=None)

* class urllib.request.FileHandler

* class urllib.request.DataHandler

* class urllib.request.FTPHandler

* class urllib.request.CacheFTPHandler

* class urllib.request.UnknownHandler

* class urllib.request.HTTPErrorProcessor
### urllib.parse
[urllib.parse](https://docs.python.org/3.6/library/urllib.parse.html#module-urllib.parse) = URL parsing + URL quoting

##### URL parsing
functions:
* urllib.parse.urlparse(urlstring, scheme=”, allow_fragments=True)

* urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding=’utf-8’, errors=’replace’)

* urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding=’utf-8’, errors=’replace’)¶

* urllib.parse.urlunparse(parts)

* urllib.parse.urlsplit(urlstring, scheme=”, allow_fragments=True)

* urllib.parse.urlunsplit(parts)

* urllib.parse.urljoin(base, url, allow_fragments=True)

* urllib.parse.urldefrag(url)

##### URL Quoting

* urllib.parse.quote(string, safe=’/’, encoding=None, errors=None)

* urllib.parse.quote_plus(string, safe=”, encoding=None, errors=None)

* urllib.parse.quote_from_bytes(bytes, safe=’/’)

* urllib.parse.unquote(string, encoding=’utf-8’, errors=’replace’)

* urllib.parse.unquote_plus(string, encoding=’utf-8’, errors=’replace’)

* urllib.parse.unquote_to_bytes(string)

* urllib.parse.urlencode(query, doseq=False, safe=”, encoding=None, errors=None, quote_via=quote_plus)

### urllib.error

* exception urllib.error.URLError

* exception urllib.error.HTTPError

* exception urllib.error.ContentTooShortError(msg, content)

### urllib.robotparser

* class urllib.robotparser.RobotFileParser(url=”)

        set_url(url)
        read()
        parse(lines)
        can_fetch(useragent, url)
        mtime()
        modified()
        crawl_delay(useragent)
        request_rate(useragent)

# python --[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id11) 

将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象, 可以传入一段字符串或一个文件句柄
```sh 
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup("<html>data</html>")
```
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: 
* Tag 
* NavigableString 
* BeautifulSoup 
* Comment 

### Tag 
Tag 对象与XML或HTML原生文档中的tag相同，Tag中最重要的属性是: name和attributes
### NavigableString
字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串
```sh
tag.string
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>
```
通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串.如果想在Beautiful Soup之外使用 NavigableString 对象,需要调用 unicode() 方法,将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存.
```sh
unicode_string = unicode(tag.string)
unicode_string
# u'Extremely bold'
type(unicode_string)
# <type 'unicode'>
```
tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法
```sh
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>
```
### BeautifulSoup
BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法.

因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name
```sh
soup.name
# u'[document]'
```
### Comment
Comment 对象是一个特殊类型的 NavigableString 对象
```sh
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>
```
但是当它出现在HTML文档中时, Comment 对象会使用特殊的格式输出

```sh
print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>
```
#### 遍历文档树
* 子节点
* 父节点
* 兄弟节点
* 回退和前进
#### 搜索文档树
#### 修改文档树
#### 输出
#### 解析部分文档

# [requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

### 发送请求

        requests.get(url)
        requests.post(url)
        requests.delete(url)
        requests.head(url)
        requests.options(url)

### 传递 URL 参数
使用 params 关键字参数，以一个字符串字典来提供这些参数

r = requests.get(url, params={'key1': 'value1', 'key2': 'value2'})




