"""HTTP Client module used to make HTTP Request

This module currently depends on python's third party package library named 'requests'.
TODO: Migrate the requests library code to use python's in build library

Example:
from HttpClient import HttpClient
http = HttpClient(base_url='https://api3.codebasehq.com', auth=('username', 'password'))
http.get(endpoint='/projects')
"""
from urllib.parse import urlencode

import requests

class HttpClient:
    """Class to make HTTP(S) requests

    This warper for the third party or In-build HTTP libraries

    Attributes:
    __base_url: Base URL of the Codebase API
    __auth: A dict containing the credentials for basic authentication
    """
    def __init__(self, base_url, auth={}):
        """ Constructor for HttpClient class.

        - This class requires base_url and  auth parameters to be passed in the constructor.

        Args:
            base_url: Fully qualified HTTP(S) API URL
            auth: A dict containing the credentials for basic authentication

        Returns:
            None

        Raises:
            None
         """
        self.__base_url = base_url
        self.__auth = auth

    def get(self, endpoint, header={}, params={}):
        """ Performs HTTP(S) GET request and returns response object

        Args:
            endpoint: endpoint path or api path
            header: A dict containing additional HTTP header data to sent with the request object
            params: Query sting data to sent with the request URL

        Returns:
            HTTP Response object

        Raises:
            Exception: when there is an un-expected error
        """
        return requests.get(
            url=self.__construct_url(endpoint=endpoint, params=params),
            headers=header,
            auth= self.__get_auth_data() if self.__auth else None
        )

    def __construct_url(self, endpoint, params={}):
        """ Constructs the fully qualified api url to make the HTTP(S) request

        Args:
            endpoint: endpoint path or api path
            params: Query sting data to sent with the request URL

        Returns:
            string URL to make the HTTP(S) request

        Raises:
            Exception: when there is an un-expected error
        """
        return self.__base_url + endpoint + ('?' + urlencode(params) if params else '')

    def __get_auth_data(self):
        """ Gets data for HTTP Basic Authentication

        Args:
            None

        Returns:
            tuple containing username and password

        Raises:
            Exception: when there is an un-expected error
        """
        return (self.__auth['username'], self.__auth['password'])