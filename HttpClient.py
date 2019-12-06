"""HTTP Client module used to make HTTP Request

## Example:
```
from HttpClient import HttpClient
http = HttpClient(
    base_url='https://api3.codebasehq.com',
    auth={'username': 'xxx', 'password': 'xxx'}
)
res = http.get(endpoint='/projects')
print(res.content)
```
"""
from urllib.parse import urlparse
from base64 import b64encode
from http.client import HTTPSConnection

class HttpClient:
    """Class to make HTTP(S) requests

    * This warper for the third party or In-build HTTP libraries

    Attributes:
    __base_url: Base URL of the Codebase API
    __auth: A dict containing the credentials for basic authentication
    """
    def __init__(self, base_url, **options):
        """ Constructor for HttpClient class.

        * This class requires base_url and  auth parameters to be passed in 
        the constructor.

        Args:
            base_url: Fully qualified HTTP(S) API URL.
            auth: A dict containing the credentials for basic authentication.
                  Example: {'username': 'xxx', 'password': 'xxx'}
            timeout: An interger timeout value for all HTTP requests.
                    Unit of the timeout is seconds. If get() or post() method recives timeout
                    value in their options, then this value will be ignored in those methods.
         """
        self.__base_url = self.__get_network_location_part(base_url)
        self.__basic_auth_header = {}

        # ====> Parsing options <====

        # Gets authentication credentials for perform HTTP Basic authentication
        # Ref: https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication
        if 'auth' in options:
            self.__auth = options['auth']
            self.__set_auth_data() # Sets the basic auth header data
        else:
            self.__auth = None

        # Setting global timeout for all HTTP requests
        if 'timeout' in options:
            self.__timeout = options['timeout']
        else:
            self.__timeout = 60 # 60 Sec

        

    def get(self, endpoint, headers={}, params={}, **options):
        """ Performs HTTP(S) GET request and returns response object

        Args:
            endpoint: endpoint path or api path
            headers: A dict containing additional HTTP header data to sent with 
            the request object
            params: Query sting data to sent with the request URL
            timeout: An interger timeout for this HTTP request. If exists, then
                the global __timeout value will be ignored in this method.

        Returns:
            HTTPSResponse: HTTP Response object

        Raises:
            Exception: when there is an un-expected error
        """
        response = HTTPSResponse()

        timeout = self.__timeout
        if 'timeout' in options:
            timeout = options['timeout']
        
        # merges the input header data with the basic auth header
        headers = { **headers, **self.__basic_auth_header }

        connection = HTTPSConnection(
            host=self.__base_url,
            port=443,
            timeout=timeout
        )
        connection.request(
            method='GET',
            url=endpoint,
            headers=headers
        )
        http_response = connection.getresponse()
        # Extracting https response
        response.status = http_response.status
        response.content = http_response.read()
        response.headers = http_response.getheaders()
        connection.close()

        return response

    def __get_network_location_part(self, url):
        """ Parses the given URL to get the network location part

        Args:
            url: URL to parse

        Returns:
            string URL to make the HTTP(S) request

        Raises:
            Exception: when there is an un-expected error
        """
        return urlparse(url).netloc

    def __set_auth_data(self):
        """ Gets data for HTTP Basic Authentication

        Args:
            None

        Returns:
            tuple containing username and password

        Raises:
            Exception: when there is an un-expected error
        """
        auth_string = self.__auth['username'] + ':' + self.__auth['password']
        auth_string = b64encode(bytes(auth_string, 'utf-8'))
        auth_string = auth_string.decode('ascii')
        self.__basic_auth_header = { 'Authorization' : 'Basic %s' % auth_string }

class HTTPSResponse:
    def __init__(self):
        self.content = None
        self.status = None
        self.headers = None