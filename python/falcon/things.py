import falcon

class ThingsResource(object):
	"""REST resources"""
	def __init__(self):
		super(ThingsResource, self).__init__()

	def on_get(self, req, resp):
		"""Handles GET requests"""
		resp.status = falcon.HTTP_200
		resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')


app = falcon.API()

things = ThingsResource()

app.add_route('/things', things)
