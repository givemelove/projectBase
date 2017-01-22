# -*- coding: utf-8 -*-
# @Author: givemelove
# @Date:   2016-11-30 09:56:10
# @Last Modified by:   Nicky Parseghian
# @Last Modified time: 2017-01-22 12:35:57

import webapp2
import share
import logging
import zlib

class MainHandler(webapp2.RequestHandler):
	def get(self):
		pass

app = webapp2.WSGIApplication([('.*', MainHandler)],
                              debug=share.wsgiDebug)
