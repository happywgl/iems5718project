from google.appengine.ext import ndb    
from lessons.dom_injection import DomInjection, DomInjectionCheck
from lessons.sql_injection_1 import SqlInjection1
from lessons.concurrency import *
import json
import webapp2

# import users api
import os

# for logging message to server log
import logging


        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello!<br><br>')
        self.response.write('Lessons list:<br><br>')
        self.response.write('&nbsp;&nbsp;&nbsp;&nbsp;<a style="font-size:28;" href="/dom_injection">dom_injection</a><br>')
        self.response.write('&nbsp;&nbsp;&nbsp;&nbsp;<a style="font-size:28;" href="/concurrency">concurrency</a><br>')
        
app = webapp2.WSGIApplication([    
    ('/', MainHandler),  
    ('/dom_injection',DomInjection),
    ('/sql_injection_1',SqlInjection1),
    ('/dom_injection/check',DomInjectionCheck),
    ('/concurrency',Concurrency),
    ('/concurrency/check',ConcurrencyCheck),
    ('/concurrency/lock',ConcurrencyLock),
    ('/concurrency/buy',ConcurrencyBuy),
    ('*.', MainHandler)
    ], debug=True)
