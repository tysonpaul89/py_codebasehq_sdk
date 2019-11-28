"""Python warper for Codebase API

CodebaseHQ API doesn't provide an SDK for python instead it provide and API.
This module contains methods for accessing some of those API calls.

Usage example:
from CodeBaseAPI import CodeBaseAPI
codebase_api = CodeBaseAPI(account_name='xxx', username='xxx', api_key='xxx')
# Returns all project details
all_projects = codebase_api.get_all_projects()
"""
from HttpClient import HttpClient


class CodeBaseAPI:
    """Class to access Codebase API

    This warper for to access the CodebaseHQ API

    Attributes:
    __auth: Dict to hold codebaseHQ authentication credentials
    __config: Dict to hold codebase configuration data
    __endpoints: Dict to hold the codebase api endpoint/path data
    __http: Contains instance of the HttpClient class
    """

    def __init__(self, account_name, username, api_key):
        """ Constructor for CodeBaseAPI class.

        -
        - This class requires account_name, username, api_key parameters to be passed
            in the constructor.
        - To get these credentials, click the Settings icon in the top-right of your
            Codebase HQ page (the one that looks like a wrench) and then click 'My Profile'.
            Go to the 'API Credentials' section at the bottom of the page

        Args:
            account_name: Account name of the CodebaseHQ user
            username: Username of the CodebaseHQ user
            api_key: API Key of the CodebaseHQ user

        Returns:
            None

        Raises:
            CredentialError: when any on of the input params are empty
            Exception: when there is an un-expected error
         """
        if account_name and username and api_key:
            self.__auth = self.__get_auth_data(account_name, username, api_key)
        else:
            raise CredentialError()

        self.__config = self.__get_config()
        self.__endpoints = self.__config['endpoints']
        self.__http = HttpClient(
            base_url=self.__config['base_url'],
            auth=self.__auth
        )

    def __get_config(self):
        """ Gets the configuration data

        If there any changes in the CodebaseHQ API URL or endpoints, then
        these change the value in this dict

        Args:
            None

        Returns:
            dict containing the CodebaseHQ configuration data

        Raises:
            None
        """
        return {
            'base_url': 'https://api3.codebasehq.com',
            'endpoints': {
                'all_projects': '/projects',
                'project': '/project',
                'tickets': '/tickets'
            }
        }

    def get_all_projects(self):
        """Gets all the projects details

        Makes an HTTP GET request to the /projects endpoint to get all project data
        Api URL: https://api3.codebasehq.com/projects
        Doc Link: https://support.codebasehq.com/kb/projects
        Sample Output:
        <projects type="array">
            <project>
                <group-id type="integer" nil="true"></group-id>
                <icon type="integer">1</icon>
                <name>Codebase</name>
                <account-name>aTech Media</account-name>
                <overview></overview>
                <permalink>codebase</permalink>
                <start-page>overview</start-page>
                <status>active</status>
                <total-tickets>100</total-tickets>
                <open-tickets>36</open-tickets>
                <closed-tickets>64</closed-tickets>
            </project>
            <project>
            ...
            </project>
        </projects>

        Args:
            None

        Returns:


        Raises:
            Error when there is an error
        """
        response = self.__http.get(
            endpoint=self.__endpoints['all_projects'],
            header=self.__get_common_headers(),
        )
        print(response.text)

    def __get_common_headers(self):
        """Gets common header to be sent with the HTTP request object

        Args:
            None

        Returns:
            Dict containing custom header data

        Raises:
            None
        """
        return {
            'Content-type': "application/xml"
        }

    def __get_auth_data(self, account_name, username, api_key):
        """ Gets data for HTTP Basic Authentication

        Args:
            account_name: Account name of the CodebaseHQ user
            username: Username of the CodebaseHQ user
            api_key: API Key of the CodebaseHQ user

        Returns:
            dict containing username and password

        Raises:
            Exception: when there is an un-expected error
        """
        return {
            'username': account_name + '/' + username,
            'password': api_key
        }


class CredentialError(Exception):
    """ Custom error class raised when CodebaseHQ credentials are empty

    Raised when the account_name or username or api_key  is empty in the
    CodeBaseAPI class constructor is empty

    Step to reproduce this exception:
    from CodeBaseAPI import CodeBaseAPI
    CodeBaseAPI(account_name='', username='', api_key='')
    """

    def __str__(self):
        return (
            "One or more CodeBaseAPI class constructor parameter is empty.\n"
            "Syntax is CodeBaseAPI(account_name='xxx', username='xxx', api_key='xxx')"
        )
