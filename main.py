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
import re


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWPRD_RE = re.compile(r"[a-zA-Z0-9_-]{6,20}$")
EMAIL_RE = re.compile(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+$")

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
<h2>Signup</h2>
<form method="post">
<table>
<tbody>
    <tr>
        <td><label for="username">Username</label></td>
            <td>
                <input name="username" type="text" value="%(username)s" required>
                <span class="error">%(username_error)s</span>
            </td>
    </tr>
    <br>
    <tr>
        <td><label for="password">Password</label></td>
            <td>
                <input name="password" type="password" value="%(password)s" required>
                <span class="error">%(password_error)s</span>
            </td>
    </tr>
    <br>
    <tr>
        <td><label for="v_password">Verify Password</label></td>
            <td>
                <input name="v_password" type="password" value="%(v_password)s" required>
                <span class="error">%(v_password_error)s</span>
            </td>
    </tr>
    <br>
    <tr>
        <td><label for="email">E-mail (optional)</label></td>
            <td>
                <input name="email" type="text" value="%(email)s">
                <span class="error">%(email_error)s</span>
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

def escape_html(s):
    return cgi.escape(s, quote = True)

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWPRD_RE.match(password)

def valid_v_password(password, v_password):
    if password == v_password:
        return True

def valid_email(email):
    if not email:
        return True

    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):

    def write_form(
        self, username="",
        password="",
        v_password="",
        email="",
        username_error="",
        password_error="",
        v_password_error="",
        email_error=""
        ):

        parameters = {
        'username':username,
        'password':password,
        'v_password':v_password,
        'email':email,
        'username_error':username_error,
        'password_error':password_error,
        'v_password_error':v_password_error,
        'email_error':email_error
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

        username_error=""
        password_error=""
        v_password_error=""
        email_error=""

        validUsername = valid_username(username)
        if not validUsername:
            username_error += "Invalid username"

        validPassword = valid_password(password)
        if not validPassword:
            password_error += "Invalid password"

        validV_password = valid_v_password(password,v_password)

        if not validV_password:
            v_password_error += "Passwords do not match"

        validEmail = valid_email(email)

        if not validEmail:
            email_error += "Invalid email"

        if not (validUsername and validPassword and validV_password and validEmail):
            self.write_form(username,password,v_password,email,username_error,password_error,v_password_error,email_error)

        else:
            self.response.out.write("Those are valid parameters! Thank you!")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
