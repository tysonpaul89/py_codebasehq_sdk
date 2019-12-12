# py_codebasehq_sdk
[CodebaseHQ API](https://support.codebasehq.com/kb) wrapper for Python 3+

* CodebaseHQ API doesn't provide an SDK for python instead it provide and API.
* This module contains methods for accessing some of those API calls.



## Usage
Open python shell
```
>>> from CodeBaseAPI import CodeBaseAPI
>>> codebase_api = CodeBaseAPI(account_name='xxx', username='yyy', api_key='zzz')
>>> res = codebase_api.get_all_projects()
>>> print(res.status)
>>> print(res.content)
```
