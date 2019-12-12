"""Python warper for Codebase API

CodebaseHQ API doesn't provide an SDK for python instead it provide and API.
This module contains methods for accessing some of those API calls.

Usage example:
from CodeBaseAPI import CodeBaseAPI
codebase_api = CodeBaseAPI(account_name='xxx', username='xxx', api_key='xxx')
# Returns all project details
all_projects = codebase_api.get_all_projects()
"""
# Ignores env/* directory when the pdoc3 generates documentation.
# Ref: https://pdoc3.github.io/pdoc/doc/pdoc/#overriding-docstrings-with-__pdoc__
__pdoc__ = {}
__pdoc__["env"] = False
