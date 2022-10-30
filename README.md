
## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


# XSS Shield

The primary objective of xss shield is to find the possible xss attack and block the request or return None.
As xss is one the most common bug in web applications security researchers a finding ways to prevent it and hackers are creating more advanced payloads. most modern frameworks prevents xss by escaping special characters but still xss can be found.
as react and djangos jinja2 tamplate engine does escapes the special characters
but injecting user inputs in href attr {{ }} can be possible to exploit xss.



## Usages

You can use the shield as a middleware by adding it into the settings.py middleware list

MIDDLEWARE = [

    'shield.middleware.XssShieldMiddleware',

]

Or you can use it as filter to where you want to senitize

`{% load shield_tag %}`

it has two filters one to senitize the value for not injecting as javascript: or data: URI variables

`{{ data|protect }}`

The other process bruteforcess through a list of event handlers which is possible to lead into xss

`{{ data|bruter }}`
Thats much simple it is :)