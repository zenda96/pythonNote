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