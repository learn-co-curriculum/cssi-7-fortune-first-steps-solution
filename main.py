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
import os
import jinja2
import random

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))#this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py

def getMessage(any_list,specificNumber=0):
    #if there is no second parameter passed, then pick a random index
    if specificNumber == 0:
        index = random.randint(0,len(any_list)-1)
    #if there is a specificNumber, then use that to index the messages
    else:
        index = specificNumber
    return any_list[index]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class CookieHandler(webapp2.RequestHandler):
    def get(self):
        def GetFortune():
            fortune_number = 1
            fortune_list =["People are naturally attracted to you.",
                           "You learn from your mistakes... You will learn a lot today.",
                           "If you have something good in your life, don't let it go!"]
            return getMessage(fortune_list,fortune_number)
        cookie_template = jinja_environment.get_template('templates/cookie.html')
        self.response.write(GetFortune())
        #self.response.out.write(cookie_template.render())


class EightBallHandler(webapp2.RequestHandler):
    def get(self):
        def GetEightAnswer():
            positive_list =["pos1", "pos2", "pos3","pos4", "pos5", "pos6" ]
            negative_list =["neg1", "neg2", "neg3"]
            neutral_list =["neu1", "neu2", "neu3"]
            return getMessage(positive_list)
        userQuestion = "Will I have a good day today?"
        eight_template = jinja_environment.get_template('templates/eightball.html')
        self.response.write(GetEightAnswer())
        #self.response.out.write(eight_template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/eightball', EightBallHandler),
    ('/cookie', CookieHandler)
], debug=True)
