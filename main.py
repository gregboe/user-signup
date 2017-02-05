#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

header = """
<!DOCTYPE html>
<html>
<head>
	<title> user-signup </title>
        <style>
        .error { color: red;
        }
        </style>
</head>
	<body>
"""
body = """
<h1>Signup</h1>

<form method="post">
<table>
<tbody>
    <tr>
        <td><label for="username">Username</label></td>
            <td>
                <input name="username" type="text" value="%(username)s" required>
                <span class="error"></span>
            </td>
    </tr>
    <br>
    <tr>
        <td><label for="password">Password</label></td>
            <td>
                <input name="password" type="password" value="%(password)s" required>
                <span class="error"></span>
            </td>
    </tr>
    <br>
    <tr>
        <td><label for="v_password">Verify Password</label></td>
            <td>
                <input name="v_password" type="password" value="%(v_password)s" required>
                <span class="error"></span>
            </td>
    </tr>
    <br>
    <tr>
        <td><label for="email">E-mail (optional)</label></td>
            <td>
                <input name="username" type="text" value="%(email)s">
                <span class="error"></span>
            </td>
    </tr>

</tbody>
</table>
<input type="submit" name="submit">
</form>
"""
footer = """
</body>

</html>
"""

def excape_html(s):
    return cgi.escape(s, quote = True)

def valid_username(username):
    pass

def valid_password(password):
    pass

def valid_v_password(v_password):
    pass

def valid_email(email):
    pass

class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="",password="",v_password="",email=""):

        parameters = {
        'username':username,
        'password':password,
        'v_password':v_password,
        'email':email,
        }

        form = header + body + footer

        self.response.out.write(form % parameters)

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        v_password = self.request.get('v_password')
        email = self.request.get('email')

        self.write_form(username,password,v_password,email)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
