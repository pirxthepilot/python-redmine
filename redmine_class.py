# Redmine Module
# For querying the Redmine API

import requests
import urllib
import json
import sys
import re


class Redmine:

    def __init__(self, baseurl, api_key, ca_cert=None):
        self.baseurl = baseurl
        self.headers = {"Content-Type": "application/json",
                        "X-Redmine-API-Key": api_key}
        self.verify = True if ca_cert is None else ca_cert

    def query(self, uri, jsondata=None):
        try:
            # If no jsondata, it is a GET request
            if jsondata is None:
                response = requests.get(self.baseurl + uri,
                                        headers=self.headers,
                                        verify=self.verify)
            else:
                response = requests.post(self.baseurl + uri,
                                         data=jsondata,
                                         headers=self.headers,
                                         verify=self.verify)
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.TooManyRedirects) as e:
            print 'requests error: ' + str(e)
            sys.exit(1)
        self.http_error_check(response)
        return response.json()

    def get_issue(self, issue_id):
        req = self.query("/issues/%s.json" % issue_id)
        return json.dumps(req)

    def create_issue(self, jsondata):
        req = self.query("/issues.json", jsondata)
        return json.dumps(req)

    def http_error_check(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print str(e)
            sys.exit(1)
