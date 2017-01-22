# -*- coding: utf-8 -*-
# @Author: givemelove
# @Date:   2016-11-30 09:56:10
# @Last Modified by:   givemelove
# @Last Modified time: 2016-11-30 11:07:48

import webapp2
import share
import logging
import zlib

class MainHandler(webapp2.RequestHandler):
	def delete(self):
		self.response.set_status(200)
		self.response.out.write(' ')

	def get(self):
		# logging.info(self.request.url)
		# logging.info(self.request.query_string)
		# logging.info(self.request.headers)
		# logging.info(self.request.cookies)

		self.response.out.write('{ "id": "com.google.enterprise.springboard.glossary.Glossary||A: Glossary", "readers": [ { "kind": "customer" } ], "createdTime": "2016-11-30T18:07:11.233Z", "itemUpdatedTime": "2016-11-30T18:07:11.672Z"}')

	def put(self):
		logging.info('--- Receiving a PUT request ---')
		logging.info('')
		logging.info('')
		logging.info('')
		logging.info('')
		logging.info(self.request.url)
		# logging.info(self.request.query_string)
		logging.info(self.request.headers)
		# logging.info(self.request.cookies)
		logging.info(zlib.decompress(self.request.body, 16+zlib.MAX_WBITS))



app = webapp2.WSGIApplication([('.*', MainHandler)],
                              debug=share.wsgiDebug)
