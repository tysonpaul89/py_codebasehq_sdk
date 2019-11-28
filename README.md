# py_codebasehq_sdk
[CodebaseHQ API](https://support.codebasehq.com/kb) wrapper for Python 3+

## Installation
```
virtualenv env -p python3.6
source env/bin/activate
pip install -r requirement.txt 
```

## Running
Open python shell
```
>>> from CodeBaseAPI import CodeBaseAPI
>>> codebase_api = CodeBaseAPI(account_name='xxx', username='yyy', api_key='zzz')
>>> codebase_api.get_all_projects()
```
