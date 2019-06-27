#!python3
#requests_login.py is a code snippet/script you can customise to do a request get of a site behind a login.
#For this example file I'm pulling down my home page post listing on freecycle.org.

import requests

#This URL will be the URL that your login form points to with the "action" tag.
post_url='https://access02.dwp.accenture.com/SecureAuth1/SecureAuth.aspx'

#This URL is the page you actually want to pull down with requests.
request_url='https://access02.dwp.accenture.com/SecureAuth1/SecureAuth.aspx'


#username-input-name is the "name" tag associated with the username input field of the login form.
#password-input-name is the "name" tag associated with the password input field of the login form.
payload = {
    'username-input-name': 'sbhatter',
      }

with requests.Session() as session:
    post = session.post(post_url, data=payload)
    r = session.get(request_url)
    print(r.text)
