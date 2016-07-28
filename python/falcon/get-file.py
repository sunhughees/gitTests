import falcon

import mimetypes
import os

class Files(object):

	def __init__(self, storage_path):
		self.storage_path = storage_path

	def on_get(self, req, resp, name):
		resp.content_type = mimetypes.guess_type(name)[0]
		image_path = os.path.join(self.storage_path, name)
		resp.stream = open(image_path, 'rb')
		resp.stream_len = os.path.getsize(image_path)
		
		print name


api = falcon.API()

storage_path = '/home/sven/Desktop'

image = Files(storage_path)

api.add_route('/files/{name}', image)