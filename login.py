import urllib
import webbrowser
import json
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.storage.dictstore import DictStore
from utils import *

store = DictStore('aa')
class LoginPage(MDScreen):
    def on_success(self, req, result, chagoler3no):
        print("request succed")
        print(result)
        response_json = json.loads(result)
        client_id = response_json['client_id']
        client_secret = response_json['client_secret']
        store.store_put('client_id', client_id)
        store.store_put('client_secret', client_secret)
        # Define the URL for the new request
        url = req.url.rstrip("api/v1/apps")
        store.store_put('url', url)
        webbrowser.open("https://{0}/oauth/authorize?client_id={1}&scope=read+write+push&redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=code").format(url, client_id)
        self.manager.current = 'code'

    def on_failure(req, result):
        print("Request failed!")
        print(result)
    
    def check_instance(self):
        url = self.ids.instname.text
        url=normalize_url(url)
        print(url)

        if(not (is_valid_url(url))):
            self.ids.instname.required=True
            return 0

        self.ids.loader.size = "100dp" , "100dp"
        url+="api/v1/apps"
        print(url)
        params = urllib.parse.urlencode({
            'client_name': 'Test Application',
            'redirect_uris': 'urn:ietf:wg:oauth:2.0:oob',
            'scopes': 'read write push',
            'website': 'https://myapp.example'
        })

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        UrlRequest(
            url,
            req_body=params,
            req_headers=headers,
            method='POST',
            on_success=self.on_success,
            on_failure=self.on_failure
        ).wait()

class codeEntryPage(MDScreen):
    def on_success(self, req, result, chagoler3no):
        print("request succed")
        print(result)
        response_json = json.loads(result)
        access_token = response_json['access_token']
        store.store_put('access_token', access_token)
        self.manager.current = 'home'

    def on_failure(req, result):
        print("Request failed!")
        print(result)
    def check_instance(self):
        url = store.store_get('url')
        code = self.ids.instname.text

        self.ids.loader.size = "100dp" , "100dp"
        url+="/oauth/token"
        print(url)

        client_id = store.store_get('client_id')
        client_secret = store.store_get('client_secret')

        params = urllib.parse.urlencode({
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uris': 'urn:ietf:wg:oauth:2.0:oob',
            'grant_type': 'authorization_code',
            'code': code,
            'scopes': 'read write push'
        })

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        UrlRequest(
            url,
            req_body=params,
            req_headers=headers,
            method='POST',
            on_success=self.on_success,
            on_failure=self.on_failure
        ).wait()